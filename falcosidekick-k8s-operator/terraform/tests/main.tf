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

variable "model_uuid" {
  description = "Reference to the uuid of a `juju_model`."
  type        = string
}

terraform {
  required_version = ">= 1.14.0"
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
  model_uuid = var.model_uuid
  revision   = var.revision
}
