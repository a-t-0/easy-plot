# Spiking Neural Network Performance Tool

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3106/)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Code Coverage](https://codecov.io/gh/a-t-0/snn/branch/main/graph/badge.svg)](https://codecov.io/gh/a-t-0/snnalgorithms)

Use this pip package to easily and quickly make box- & line-plots, as well
as latex-tables.

## Example
To use this your Python code first install the pip package:
```sh
pip install simplt
```
And in your Python code:
```py
from simplt.line_plot.line_plot import example_create_multi_line_plot
example_create_multi_line_plot("some_dir/sub_dir","example_filename",["png"])
```

## Modify this package
First satisfy the prerequisites:

```sh
conda env create --file environment.yml
conda activate simplt
```

You can run the experiment with command:
```bash
python -m src.simplt
```
For more info, run:

```bash
python -m src.simplt --help
```

And run tests with:

```bash
python -m pytest
```

or to see live output, on any tests filenames containing substring: `results`:

```bash
python -m pytest --capture=tee-sys
```

## Test Coverage

Developers can use:

```bash
conda env create --file environment.yml
python -m pytest
```

Currently the test coverage is `65%`. 

For type checking:

```bash
mypy --disallow-untyped-calls --disallow-untyped-defs tests/*
```

### Releasing pip package update

To udate the Python pip package, one can first satisfy the following requirements:

```bash
pip install --upgrade pip setuptools wheel
pip install twine
```

Followed by updating the package with:

```bash
python3 setup.py sdist bdist_wheel
python -m twine upload dist/\*
```

### Developer pip install

```bash
mkdir -p ~/bin
cp snn_rebuild.sh ~/bin/snnrb
chmod +x ~/bin/snnrb
```

Then you can rebuild and locally re-install all 5 repositories with the command:

```bash
snnrb
```

If you want to quickly test if your changes work, you can go into the root dir
of this project and run:

```bash
python3 setup.py sdist bdist_wheel
pip install -e .
```

that installs the latest changes into the pip package locally (into your conda
environment).

<!-- Un-wrapped URL's (Badges and Hyperlinks) -->
