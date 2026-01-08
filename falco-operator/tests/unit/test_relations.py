# Copyright 2025 Canonical Ltd.
# See LICENSE file for licensing details.

"""Unit tests for relations module."""

from unittest.mock import MagicMock, patch

import pytest
from charmlibs.interfaces.http_endpoint import HttpEndpointDataModel

from relations import HttpEndpointManager


class TestHttpEndpointManager:
    """Test HttpEndpointManager class."""

    @pytest.mark.parametrize(
        "scenario,setup",
        [
            ("no_relations", lambda: []),
        ],
    )
    def test_get_http_endpoint_returns_none(self, scenario, setup):
        """Test get_http_endpoint returns None for various scenarios.

        Arrange: Set up mock charm according to scenario.
        Act: Call get_http_endpoint.
        Assert: Verify None is returned.
        """
        mock_charm = MagicMock()
        endpoints = setup()

        with patch("relations.HttpEndpointRequirer") as mock_requirer_class:
            mock_requirer = MagicMock()
            mock_requirer.http_endpoints = endpoints
            mock_requirer_class.return_value = mock_requirer

            manager = HttpEndpointManager(mock_charm, "http-output")
            result = manager.get_http_endpoint()

            assert result is None

    @pytest.mark.parametrize(
        "url,description",
        [
            ("http://falcosidekick:2801", "basic HTTP URL"),
            ("https://falcosidekick.example.com:2801/events", "HTTPS with path"),
        ],
    )
    def test_get_http_endpoint_valid_infos(self, url, description):
        """Test get_http_endpoint returns valid URLs.

        Arrange: Set up mock charm with relation containing valid URL.
        Act: Call get_http_endpoint.
        Assert: Verify HttpEndpointDataModel is returned with correct URL.
        """
        mock_charm = MagicMock()
        mock_endpoint = HttpEndpointDataModel(url=url)

        with patch("relations.HttpEndpointRequirer") as mock_requirer_class:
            mock_requirer = MagicMock()
            mock_requirer.http_endpoints = [mock_endpoint]
            mock_requirer_class.return_value = mock_requirer

            manager = HttpEndpointManager(mock_charm, "http-output")
            result = manager.get_http_endpoint()

            assert result is not None
            assert result.url == url
