# Copyright 2025 Canonical Ltd.
# See LICENSE file for licensing details.

variables {
  channel = "2/edge"
  # renovate: depName="falcosidekick-k8s"
  revision = 1
}

run "basic_deploy" {
  assert {
    condition     = module.falcosidekick-k8s.app_name == "falcosidekick-k8s"
    error_message = "falcosidekick-k8s app_name did not match expected"
  }
}
