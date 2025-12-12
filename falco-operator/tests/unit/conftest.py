# Copyright 2025 Canonical Ltd.
# See LICENSE file for licensing details.


import pytest

from service import FalcoLayout


@pytest.fixture
def mock_charm_dir(tmp_path):
    """Mock charm directory containing Falco directory."""
    return tmp_path


@pytest.fixture
def mock_falco_base_dir(mock_charm_dir):
    """Create a temporary Falco base directory."""
    falco_dir = mock_charm_dir / "falco"
    falco_dir.mkdir()
    yield falco_dir


@pytest.fixture
def mock_falco_layout(mock_falco_base_dir):
    """Create a temporary Falco directory structure."""
    (mock_falco_base_dir / "usr/bin").mkdir(parents=True)
    (mock_falco_base_dir / "usr/bin/falco").touch()
    (mock_falco_base_dir / "usr/share/falco/plugins").mkdir(parents=True)
    (mock_falco_base_dir / "etc/falco/default_rules").mkdir(parents=True)
    yield FalcoLayout(base_dir=mock_falco_base_dir)
