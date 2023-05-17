# Versioning strategy

This repository follows a [CalVer](https://calver.org/)-type approach to versioning, in contrast to the majority of
other PyGranta and PyAnsys projects which follow [SemVer](https://semver.org/). 

This package is versioned according to the following scheme: `YYYY.[1,2].MINOR`

The reasons for this are described below.

# Advantages of this approach

This repository only contains code generated from OpenAPI JSON definition files, which themselves are versioned 
with Granta MI. Granta MI follows a CalVer-type approach of `YYYY.[1,2]`, with two versions released per year.

These OpenAPI JSON definition files are _backwards-compatible_, but not _forwards-compatible_. In other words,
the API definition from an older version of Granta MI is compatible with a newer version, but not the other way
round.

Given that multiple versions of Granta MI are often used in parallel for a number of releases, a key requirement
of the `ansys-grantami-serverapi-openapi` package and other PyGranta packages is that users can quickly and easily
identify the correct package version for a specific version of Granta MI.

To simplify this relationship between Granta MI version and `ansys-grantami-serverapi-openapi` version, we use the
Granta MI version number as the first two parts of the version number for releases from this repository. For example:

* Granta MI 2023 R2 -> `ansys-grantami-serverapi-openapi` `v2023.2.0`, `v2023.2.1`, etc.
* Granta MI 2024 R1 -> `ansys-grantami-serverapi-openapi` `v2024.1.0`, `v2024.1.1`, etc.

As a result, to install a version that is guaranteed to work with your version of Granta MI, just specify:

`pip install ansys-grantami-serverapi-openapi ~= 2023.1.0`

# Potential alternatives

## SemVer, with a mapping between SemVer versions and Granta MI versions

This approach would follow SemVer guidelines, and so each major version of this package would correspond to a
specific Granta MI version. Using a `0.x` release for this package, the mapping would be as follows:

* Granta MI 2023 R2 -> `ansys-grantami-serverapi-openapi` `v0.1.0`, `v0.1.1`, etc.
* Granta MI 2024 R1 -> `ansys-grantami-serverapi-openapi` `v0.2.0`, `v0.2.1`, etc.

However, this approach doesn't have any significant benefits; there is still only one PATCH version that can be
used to denote different versions compatible with the same Granta MI version. The major drawback would be that
it's not obvious which version of Granta MI a specific version of this package is compatible with.

Alternatively, we could also use the major version as follows:

* Granta MI 2023 R2 -> `ansys-grantami-serverapi-openapi` `v1.0.0`, `v1.0.1`, `v1.1.0`, etc.
* Granta MI 2024 R1 -> `ansys-grantami-serverapi-openapi` `v2.0.0`, `v2.0.1`, `v2.2.0`, etc.

This would have the advantage of allowing MINOR and PATCH releases for this package. However, changes for this
repository are expected to be relatively minor beyond JSON definition updates, and so this advantage does not
seem significant compared to the added overhead of translating between two different version numbers.

## Support multiple Granta MI versions per package version

We could support multiple Granta MI versions by including auto-generated code for different Granta MI versions
in separate submodules. 

This doesn't solve the problem though; at some point we'd have to drop support for older versions of Granta MI
which would trigger a major version change. The only difference between this and the SemVer description above
is that a single version of Granta MI would be supported by a range of package versions.
