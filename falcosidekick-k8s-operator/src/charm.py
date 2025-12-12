#!/usr/bin/env python3

# Copyright 2025 Canonical Ltd.
# See LICENSE file for licensing details.

"""Falcosidekick k8s charm."""

import logging
import typing

import ops

from state import CharmBaseWithState, CharmState
from workload import Falcosidekick

logger = logging.getLogger(__name__)


class FalcosidekickCharm(CharmBaseWithState):
    """Falcosidekick k8s charm.

    This charm deploys and manages Falcosidekick, an open-source daemon for connecting Falco to
    your ecosystem.
    """

    def __init__(self, *args: typing.Any):
        """Charm the service."""
        super().__init__(*args)

        self._state = None

        self.falcosidekick = Falcosidekick(self)

        self.framework.observe(self.on.install, self._install)
        self.framework.observe(self.on.falcosidekick_pebble_ready, self.reconcile)

    @property
    def state(self) -> CharmState:
        """The charm state."""
        if self._state is None:
            self._state = CharmState.from_charm(self)
        return self._state

    def _install(self, _: ops.EventBase) -> None:
        """Handle the install event."""
        self.unit.status = ops.MaintenanceStatus("Installing containers")

    def reconcile(self, _: ops.EventBase) -> None:
        """Reconcile the charm state."""
        if not self.falcosidekick.ready:
            logger.warning("Pebble is not ready in '%s'", self.falcosidekick.container_name)
            self.unit.status = ops.WaitingStatus("Workload not ready")
            return

        self.falcosidekick.configure()

        if not self.falcosidekick.health:
            logger.warning("'%s' workload is not healthy", self.falcosidekick.container_name)
            self.unit.status = ops.BlockedStatus("Workload not healthy")
            return

        self.unit.status = ops.ActiveStatus()


if __name__ == "__main__":  # pragma: nocover
    ops.main(FalcosidekickCharm)
