#!/usr/bin/env python3

# Copyright 2025 Canonical Ltd.
# See LICENSE file for licensing details.

"""Falco subordinate charm."""

import logging
import typing

import ops

# Log messages can be retrieved using juju debug-log
logger = logging.getLogger(__name__)


class Charm(ops.CharmBase):
    """Falco subordinate charm.

    This charm deploys and manages Falco, an open-source runtime security tool.
    As a subordinate charm, it runs alongside a principal charm.
    """

    def __init__(self, *args: typing.Any):
        """Charm the service.

        Arguments:
            args: Arguments passed to the CharmBase parent constructor.
        """
        super().__init__(*args)
        self.framework.observe(self.on.install, self._on_install)
        self.framework.observe(self.on.config_changed, self._on_config_changed)

    def _on_install(self, _: ops.InstallEvent) -> None:
        """Handle install event."""
        logger.info("Installing Falco")
        self.unit.status = ops.MaintenanceStatus("Installing Falco")
        # TODO: Add Falco installation logic
        self.unit.status = ops.ActiveStatus()

    def _on_config_changed(self, _: ops.ConfigChangedEvent) -> None:
        """Handle config changed event."""
        logger.info("Configuring Falco")
        # TODO: Add Falco configuration logic
        self.unit.status = ops.ActiveStatus()


if __name__ == "__main__":  # pragma: nocover
    ops.main(Charm)
