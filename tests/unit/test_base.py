# Copyright 2025 Canonical Ltd.
# See LICENSE file for licensing details.

"""Unit tests for Falco charm."""

import ops
import ops.testing

from charm import Charm


def test_install():
    """Test the install event handler."""
    context = ops.testing.Context(
        charm_type=Charm,
    )
    state_in = ops.testing.State()
    state_out = context.run(context.on.install(), state_in)
    assert state_out.unit_status == ops.testing.ActiveStatus()


def test_config_changed():
    """Test the config_changed event handler."""
    context = ops.testing.Context(
        charm_type=Charm,
    )
    state_in = ops.testing.State()
    state_out = context.run(context.on.config_changed(), state_in)
    assert state_out.unit_status == ops.testing.ActiveStatus()
