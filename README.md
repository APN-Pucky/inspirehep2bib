# inspirehep2bib

[![PyPI - Version](https://img.shields.io/pypi/v/inspirehep2bib.svg)](https://pypi.org/project/inspirehep2bib)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/inspirehep2bib.svg)](https://pypi.org/project/inspirehep2bib)

-----

## Table of Contents

- [Installation](#installation)
- [License](#license)
- [Examples](#examples)

## Installation

```console
pip install inspirehep2bib
```

## License

`inspirehep2bib` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

## Examples

```console
$ inspirehep2bib 'arXiv:1908.06987'
@article{Monni:2019whf,
    author = "Monni, Pier Francesco and Nason, Paolo and Re, Emanuele and Wiesemann, Marius and Zanderighi, Giulia",
    title = "{MiNNLO$_{PS}$: a new method to match NNLO QCD to parton showers}",
    eprint = "1908.06987",
    archivePrefix = "arXiv",
    primaryClass = "hep-ph",
    reportNumber = "CERN-TH-2019-117, LAPTH-042/19, MPP-2019-177",
    doi = "10.1007/JHEP05(2020)143",
    journal = "JHEP",
    volume = "05",
    pages = "143",
    year = "2020",
    note = "[Erratum: JHEP 02, 031 (2022)]"
}
```

```console
$ inspirehep2bib "Bierlich:2019rhm"
@article{Bierlich:2019rhm,
    author = "Bierlich, Christian and others",
    title = "{Robust Independent Validation of Experiment and Theory: Rivet version 3}",
    eprint = "1912.05451",
    archivePrefix = "arXiv",
    primaryClass = "hep-ph",
    reportNumber = "MCnet-19-26",
    doi = "10.21468/SciPostPhys.8.2.026",
    journal = "SciPost Phys.",
    volume = "8",
    pages = "026",
    year = "2020"
}
```
