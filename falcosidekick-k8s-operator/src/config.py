# Copyright 2025 Canonical Ltd.
# See LICENSE file for licensing details.

"""Charm config option module."""

import logging

from pydantic import BaseModel

logger = logging.getLogger(__name__)


class InvalidCharmConfigError(Exception):
    """Exception raised when the charm configuration is invalid."""


class CharmConfig(BaseModel):
    """The pydantic model for charm config.

    Note that the charm config should be loaded via ops.CharmBase.load_config().
    """
