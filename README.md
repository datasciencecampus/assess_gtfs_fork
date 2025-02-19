<!--- Badges start --->
<img src="https://img.shields.io/badge/repo%20status-in%20development%20(caution)-red?style=plastic" alt="Repository status is still in development (caution required)"/><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/assess-gtfs?style=plastic"><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/assess-gtfs?style=plastic&logo=pypi&logoColor=white&label=PyPI%20downloads"><img src="https://github.com/datasciencecampus/assess_gtfs/actions/workflows/python-package-mac.yml/badge.svg" alt="Build status badge on mac"/><img src="https://github.com/datasciencecampus/assess_gtfs/actions/workflows/python-package-windows.yml/badge.svg" alt="Build status badge on windows"/><img src="https://github.com/datasciencecampus/assess_gtfs/actions/workflows/build-deploy.yml/badge.svg" alt="Deploy PYPI"/><img src="https://codecov.io/github/datasciencecampus/assess_gtfs/graph/badge.svg?token=iEWElAdksI" alt="Codecov coverage result"/>

<!--- Badges end --->

<img src="https://github.com/datasciencecampus/awesome-campus/blob/master/ons_dsc_logo.png">

# assess-gtfs

> :warning: This repository is still in the development phase. Caution should
be taken before using or referencing this work in any way - use it at your own
risk.

## Introduction
<!-- *Describe what this repo contains and what the project is.* -->

`assess-gtfs` provides a method for inspecting and validating General Transit
Feed Specification.

## Developers
We welcome contributions from others. Please check out our
[code of conduct](CODE_OF_CONDUCT.md) and
[contributing guidance](CONTRIBUTING.md###Set-up).

## Usage
<!-- *Explain how to use the things in the repo.* -->

### Installation

This package is designed to work with python 3.9, 3.10 and 3.11.

We recommend running the package with a virtual environment such as
[conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
or [venv](https://docs.python.org/3/library/venv.html).

With conda:
```
conda create -n assess-gtfs python=3.11 -y
```
Once completed, activate the environment:
```
conda activate assess-gtfs
```
Install the python package with required dependencies:

```
pip install assess-gtfs
```

Additional Java dependencies are required for full functionality. See the
[contributing guidance](./CONTRIBUTING.md) for assistance.

### Required Data

You will need
[Public Transport Schedule data](https://data.bus-data.dft.gov.uk/downloads/)
in GTFS format, appropriate to the territory that you wish to analyse.

## Data Science Campus
At the [Data Science Campus](https://datasciencecampus.ons.gov.uk/about-us/) we
apply data science, and build skills, for public good across the UK and
internationally. Get in touch with the Campus at
[datasciencecampus@ons.gov.uk](datasciencecampus@ons.gov.uk).

## License
<!-- Unless stated, the codebase is released under [the MIT Licence][mit]. -->

The code, unless otherwise stated, is released under [the MIT Licence][mit].

The documentation for this work is subject to [© Crown copyright][copyright]
and is available under the terms of the [Open Government 3.0][ogl] licence.

[mit]: LICENCE
[copyright]: http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/
[ogl]: http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
