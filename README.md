
# ML-Ops

[![Build Status](https://travis-ci.com/kbrezinski/ML-Ops.svg?branch=master)](https://travis-ci.com/kbrezinski/ML-Ops)
[![Documentation Status](https://readthedocs.org/projects/ml-ops/badge/?version=latest)](https://ml-ops.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/kbrezinski/ML-Ops/branch/master/graph/badge.svg)](https://codecov.io/gh/kbrezinski/ML-Ops)
[![PyPI version](https://badge.fury.io/py/ml-ops.svg)](https://badge.fury.io/py/ml-ops)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ml-ops.svg)](https://pypi.python.org/pypi/ml-ops/)
[![PyPI license](https://img.shields.io/pypi/l/ml-ops.svg)](https://pypi.python.org/pypi/ml-ops/)

# Overview

ML-Ops is a Python package for managing machine learning models. It provides a framework for managing the entire machine learning lifecycle, from data collection to model deployment. It is designed to be used in conjunction with other machine learning packages, such as [scikit-learn](https://scikit-learn.org/stable/), [TensorFlow](https://www.tensorflow.org/), and [PyTorch](https://pytorch.org/).

## Table of Contents

- [ML-Ops](#ml-ops)
- [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [Package Installation](#package-installation)
  - [Docstring Generation](#docstring-generation)

## Package Installation

Git clone from source:
```bash
git clone https://github.com/kbrezinski/ML-Ops 
```

Install from source using either standard or dev mode:

```bash
python3 -m pip install -e .            # installs required packages only
```

```bash
python3 -m pip install -e .[dev]       # installs required packages and dev packages
```

## Docstring Generation

```bash
python3 -m pip install -e .[docs]       # installs documentation packages
```

Initialize `mkdocs` uisng `python3 -m mkdocs new .` and edit `mkdocs.yml` to include the following:

```yaml
site_name: ML-Ops
theme: readthedocs
nav:
  - Home: index.md
  - API Reference: api.md
```


