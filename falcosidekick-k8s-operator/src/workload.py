# Copyright 2025 Canonical Ltd.
# See LICENSE file for licensing details.

"""Charm workload module."""

import logging

import ops

logger = logging.getLogger(__name__)


class Falcosidekick:
    """Falcosidekick workload class.

    See the charmcraft.yaml and rockcraft.yaml for more information about the class attributes.
    """

    command: str = "falcosidekick"  # defined in rockcraft.yaml
    sevice_name: str = "falcosidekick"  # defined in rockcraft.yaml
    container_name: str = "falcosidekick"  # defined in charmcraft.yaml

    def __init__(self, charm: ops.CharmBase) -> None:
        """Initialize the Falcosidekick workload."""
        self.charm = charm

    @property
    def ready(self) -> bool:
        """Determine if the Falcosidekick workload is ready for use."""
        return self.container.can_connect()

    @property
    def health(self) -> bool:
        """Determine if the Falcosidekick workload is healthy."""
        if not self.ready:
            logger.warning("Cannot determine health; container is not ready")
            return False
        checks = self.container.get_checks(level=ops.pebble.CheckLevel.ALIVE)
        return all(check.status == ops.pebble.CheckStatus.UP for check in checks.values())

    @property
    def container(self) -> ops.Container:
        """Get the Falcosidekick container."""
        return self.charm.unit.get_container(self.container_name)

    def configure(self) -> None:
        """Configure the Falcosidekick workload idempotently."""
        if not self.ready:
            logger.warning("Cannot configure; container is not ready")
            return
        for service_name, service in self.container.get_services().items():
            if not service.is_running():
                logger.debug(f"Restarting {service_name} in {self.container_name}")
                self.container.restart(service_name)
                continue
