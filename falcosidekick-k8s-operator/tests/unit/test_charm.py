# Copyright 2025 Canonical Ltd.
# See LICENSE file for licensing details.

"""Unit tests for Falco charm."""

import ops
from ops import testing

from charm import FalcosidekickCharm
from workload import Falcosidekick


class TestCharm:
    """Test Charm class."""

    def test_on_falcosidekick_pebble_ready_can_connect(self):
        """Test on falcosidekick pebble ready event when container can connect."""
        # Arrange: Set up the mock container to simulate a successful connection
        ctx = testing.Context(FalcosidekickCharm)
        # mypy thinks this can_connect argument does not exist.
        container = testing.Container(Falcosidekick.container_name, can_connect=True)  # type: ignore
        state_in = testing.State(containers=[container])

        # Act: Create a testing context and run the event
        state_out = ctx.run(ctx.on.pebble_ready(container=container), state_in)

        # Assert: Verify that the unit status is set to ActiveStatus
        assert state_out.unit_status == ops.ActiveStatus()

    def test_on_falcosidekick_pebble_ready_cannot_connect(self):
        """Test on falcosidekick pebble ready event when container cannot connect."""
        # Arrange: Set up the mock container to simulate a successful connection
        ctx = testing.Context(FalcosidekickCharm)
        # mypy thinks this can_connect argument does not exist.
        container = testing.Container(Falcosidekick.container_name, can_connect=False)  # type: ignore
        state_in = testing.State(containers=[container])

        # Act: Create a testing context and run the event
        state_out = ctx.run(ctx.on.pebble_ready(container=container), state_in)

        # Assert: Verify that the unit status is set to ActiveStatus
        assert state_out.unit_status == ops.WaitingStatus("Workload not ready")
