# zipload

![circleci](https://img.shields.io/circleci/build/github/seemethere/zipload)
![netlify](https://img.shields.io/netlify/af039a9f-56ee-4f75-a42e-968f22ab6126)
[![docs](https://img.shields.io/badge/docs-goto-informational)](https://zipload.terriblecode.com)

## Overview
A simply python module to load zip archives into your python path

zipimport isn't the best module in the world to work with so this module tries
to overcome its shortcomings by providing easy to use functions that allow you
to do the things you'd expect zipimport to do in a way that actually makes
sense.

How this actually works:
1. Unzip archive into a temporary directory
2. Add that temporary directory to your Python Path
3. Cleanup python path and temporary directory at exit

## Installation

Install simply with pip:

```
pip install zipload
```

Or add to your project with `poetry`:

```
poetry add zipload
```

## Compatability

This is a Python 3 only module, there are no current plans on making it Python 2
compatible.

## Usage

Load a zip file into your python path, then unload it after use

```python
import zipload

with zipload.load("example.zip", "lib/python3.8/site-packages"):
    import numpy
```

Load a zip file into your python path for the duration of execution

```python
import zipload
# Must go above libraries you would want to load
zipload.global_load("example.zip", "lib/python3.8/site-packages")

import numpy
```

## Development

Developers can load all dev dependencies using:

```
poetry install
```

Tests can be run with

```
poetry run pytest
```
