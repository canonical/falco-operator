# Copyright 2025 Canonical Ltd.
# See LICENSE file for licensing details.

"""Charm state module."""

import itertools
import logging
from abc import ABC, abstractmethod

import ops
from pydantic import BaseModel, ValidationError

from config import CharmConfig, InvalidCharmConfigError

logger = logging.getLogger(__name__)


class CharmState(BaseModel):
    """The pydantic model for charm state."""

    @classmethod
    def from_charm(cls, charm: ops.CharmBase) -> "CharmState":
        """Create a CharmState from a charm instance.

        Args:
            charm: The charm instance.

        Returns: A CharmState instance.
        """
        try:
            _ = charm.load_config(CharmConfig)
        except ValidationError as e:
            logger.error("Configuration validation error: %s", e)
            error_fields = set(itertools.chain.from_iterable(err["loc"] for err in e.errors()))
            error_field_str = " ".join(f"{f}" for f in error_fields)
            raise InvalidCharmConfigError(f"Invalid charm configuration {error_field_str}") from e

        return cls()


class CharmBaseWithState(ops.CharmBase, ABC):
    """The CharmBase than can build a CharmState."""

    @property
    @abstractmethod
    def state(self) -> CharmState | None:
        """The charm state."""

    @abstractmethod
    def reconcile(self, _: ops.HookEvent) -> None:
        """Reconcile configuration."""
