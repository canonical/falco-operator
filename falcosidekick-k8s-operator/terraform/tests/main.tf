# Copyright 2025 Canonical Ltd.
# See LICENSE file for licensing details.

variable "channel" {
  description = "The channel to use when deploying a charm."
  type        = string
  default     = "2/edge"
}

variable "revision" {
  description = "Revision number of the charm."
  type        = number
  default     = null
}

terraform {
  required_providers {
    juju = {
      version = "~> 1.1.1"
      source  = "juju/juju"
    }
  }
}

provider "juju" {}

module "falcosidekick-k8s" {
  source     = "./.."
  app_name   = "falcosidekick-k8s"
  channel    = var.channel
  model_uuid = "prod-falcosidekick-k8s-example"
  revision   = var.revision
}
