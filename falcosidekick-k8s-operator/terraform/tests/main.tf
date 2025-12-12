# Copyright 2025 Canonical Ltd.
# See LICENSE file for licensing details.

variable "channel" {
  description = "The channel to use when deploying a charm."
  type        = string
  default     = "2.32.0/edge"
}

variable "revision" {
  description = "Revision number of the charm."
  type        = number
  default     = null
}

terraform {
  required_providers {
    juju = {
      version = "~> 0.20.0"
      source  = "juju/juju"
    }
  }
}

provider "juju" {}

module "falcosidekick-k8s" {
  source   = "./.."
  app_name = "falcosidekick-k8s"
  channel  = var.channel
  model    = "prod-falcosidekick-k8s-example"
  revision = var.revision
}
