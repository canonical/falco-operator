# Copyright 2025 Canonical Ltd.
# See LICENSE file for licensing details.

variables {
  channel = "2/edge"
  model_uuid = "1d10a751-02c1-43d5-b46b-d84fe04d6fde"
  # renovate: depName="falcosidekick-k8s"
  revision = 1
}

run "basic_deploy" {
  assert {
    condition     = module.falcosidekick-k8s.app_name == "falcosidekick-k8s"
    error_message = "falcosidekick-k8s app_name did not match expected"
  }
}
