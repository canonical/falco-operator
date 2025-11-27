<!-- vale Canonical.007-Headings-sentence-case = NO -->
# Falco operator
<!-- vale Canonical.007-Headings-sentence-case = YES -->

A [Juju](https://juju.is/) [charm](https://documentation.ubuntu.com/juju/3.6/reference/charm/)
deploying and managing [Falco](https://falco.org/) on physical or virtual machines. Falco is a
open-source cloud native security tool that provides runtime security across hosts, containers,
Kubernetes, and cloud environments.

Like any Juju charm, this charm supports one-line deployment, configuration, integration, scaling, and more.

This charm will make operating Falco simple and straightforward for DevOps or SRE teams through
Juju's clean interface. For information about how to deploy, integrate, and manage this charm, see
the Official [Falco Operator Documentation](https://charmhub.io/falco/docs).

## In this documentation

| | |
|--|--|
|  [Tutorials](https://charmhub.io/falco/docs/tutorial-getting-started)</br>  Get started - a hands-on introduction to using the charm for new users </br> |  [How-to guides](https://charmhub.io/falco/docs/how-to-contribute) </br> Step-by-step guides covering key operations and common tasks |
| [Reference](https://charmhub.io/falco/docs/reference-actions) </br> Technical information - specifications, APIs, architecture | [Explanation](https://charmhub.io/falco/docs/explanation-charm-architecture) </br> Concepts - discussion and clarification of key topics  |
| | |

## Contributing to this documentation

Documentation is an important part of this project, and we take the same open-source approach
to the documentation as the code. As such, we welcome community contributions, suggestions, and
constructive feedback on our documentation.
See [How to contribute](https://github.com/canonical/falco-operator/blob/main/CONTRIBUTING.md) for more information.


If there's a particular area of documentation that you'd like to see that's missing, please
[file a bug](https://github.com/canonical/falco-operator/issues).

## Project and community

The Falco Operator is a member of the Ubuntu family. It's an open-source project that warmly welcomes community
projects, contributions, suggestions, fixes, and constructive feedback.

- [Code of conduct](https://ubuntu.com/community/code-of-conduct)
- [Get support](https://discourse.charmhub.io/)
- [Join our online chat](https://matrix.to/#/#charmhub-charmdev:ubuntu.com)
- [Contribute](https://github.com/canonical/falco-operator/blob/main/CONTRIBUTING.md)

Thinking about using the falco Operator for your next project?
[Get in touch](https://matrix.to/#/#charmhub-charmdev:ubuntu.com)!

# Contents

1. [Tutorial](tutorial/getting-started.md)
1. [How to](how-to)aa
  1. [Contribute](how-to/contribute.md)
1. [Reference](reference)
  1. [Actions](reference/actions.md)
  1. [Configurations](reference/configurations.md)
  1. [Integrations](reference/integrations.md)
  1. [Metrics](reference/metrics.md)
1. [Explanation](explanation)
  1. [Architecture](explanation/architecture.md)
  1. [Charm design](explanation/charm-design.md)
  1. [Security](explanation/security.md)
1. [Changelog](changelog.md)
