#!/usr/bin/env python3

# Copyright 2025 Canonical Ltd.
# See LICENSE file for licensing details.

"""Falco subordinate charm."""

import logging
import typing

import ops
import pydantic

from config import CharmConfig, GitCloneError, RsyncError, SettingRepoManager, SshKeyScanError
from service import FalcoConfig, FalcoLayout, FalcoService, FalcoServiceFile

logger = logging.getLogger(__name__)


class Charm(ops.CharmBase):
    """Falco subordinate charm.

    This charm deploys and manages Falco, an open-source runtime security tool.
    As a subordinate charm, it runs alongside a principal charm.
    """

    def __init__(self, *args: typing.Any):
        """Charm the service."""
        super().__init__(*args)

        self.falco_layout = FalcoLayout(base_dir=self.charm_dir / "falco")
        self.falco_service_file = FalcoServiceFile(self.falco_layout, self)
        self.managed_falco_config = FalcoConfig(self.falco_layout)
        self.falco_service = FalcoService(self.managed_falco_config, self.falco_service_file)

        self.framework.observe(self.on.remove, self._on_remove)
        self.framework.observe(self.on.install, self._on_install_or_upgrade)
        self.framework.observe(self.on.upgrade_charm, self._on_install_or_upgrade)
        self.framework.observe(self.on.update_status, self._update_status)

        self.framework.observe(self.on.config_changed, self.reconcile)
        self.framework.observe(self.on.secret_changed, self.reconcile)

    def _on_remove(self, _: ops.RemoveEvent) -> None:
        """Handle remove event."""
        self.unit.status = ops.MaintenanceStatus("Removing Falco service")
        self.falco_service.remove()

    def _on_install_or_upgrade(self, event: ops.InstallEvent | ops.UpgradeCharmEvent) -> None:
        """Handle install or upgrade charm event."""
        self.unit.status = ops.MaintenanceStatus("Installing Falco service")
        self.falco_service.install()
        self.reconcile(event)

    def _update_status(self, event: ops.UpdateStatusEvent) -> None:
        """Update the unit status."""
        self.reconcile(event)

    def _configure(self) -> None:
        """Configure the Falco service."""
        charm_config = self.load_config(CharmConfig)
        if not charm_config.setting_repo:
            logger.info("No custom setting repository configured")
            return

        setting_repo_manager = SettingRepoManager(self.model, charm_config)
        setting_repo_manager.sync(self.falco_layout)
        self.falco_service.configure()

    def reconcile(self, _: ops.EventBase) -> None:
        """Reconcile the charm state."""
        try:
            self._configure()
        except pydantic.ValidationError as e:
            logger.exception("Configuration validation error: %s", e)
            self.unit.status = ops.BlockedStatus("Invalid configuration")
            return
        except (ValueError, GitCloneError, SshKeyScanError, RsyncError) as e:
            logger.exception("Failed to clone custom setting repository: %s", e)
            self.unit.status = ops.BlockedStatus("Failed to clone setting repo")
            return

        if not self.falco_service.check_active():
            raise RuntimeError("Falco service is not running")

        self.unit.status = ops.ActiveStatus()


if __name__ == "__main__":  # pragma: nocover
    ops.main(Charm)
