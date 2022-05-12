# fitols


[![pypi](https://img.shields.io/pypi/v/fitols.svg)](https://pypi.org/project/fitols/)
[![python](https://img.shields.io/pypi/pyversions/fitols.svg)](https://pypi.org/project/fitols/)
[![Build Status](https://github.com/berleon/fitols/actions/workflows/dev.yml/badge.svg)](https://github.com/berleon/fitols/actions/workflows/dev.yml)
[![codecov](https://codecov.io/gh/berleon/fitols/branch/main/graphs/badge.svg)](https://codecov.io/github/berleon/fitols)



Skeleton project created by Cookiecutter PyPackage


* Documentation: <https://berleon.github.io/fitols>
* GitHub: <https://github.com/berleon/fitols>
* PyPI: <https://pypi.org/project/fitols/>
* Free software: MIT



## Setup


### Get it running

The preferred setup is that you have a directory named `fitols` and inside that directory you have a `data` folder, the virtual environment and this repository.
Just follow these steps:


```bash
mkdir fitols
cd fitols
# create and load the virtual environment
python3 -m venv venv
source venv/bin/activate
# create the data folder
mkdir data
# clone the repository
git clone https://github.com/berleon/fitols.git
cd fitols
# Get poetry and update pip
pip install -U pip wheel poetry
poetry install
# now you can list the available nodes
python -m fitols nodes
# or run the tests
make test
```

## Comand line interface

Make sure you have successfully run `poetry install` in the project directory.
You then can list and run the project nodes and also list previously runs.

### List nodes

To list all available nodes execute the following command:
```bash
python -m fitols nodes
```


### Run a node

The following command will run the FitOLS node:
```
python -m fitols run fitols.fit_ols.FitOLS \
    --dataset california_housing --target MedHouseVal
```

### List runs

This will list all runs:
```
python -m fitols ls
```

To list only runs starting with "FitOLS":
```
python -m fitols ls FitOLS
```

You can also select to list only runs completed in the last 3 hours:
```
python -m fitols ls FitOLS --completed --last 3h
```

### Delete runs

The cli to delete runs is similar to the one to list runs:

```
python -m fitols rm FitOLS --failed --last 3h
```
Would ask for confirmation before deleting all completed runs in the last 3 hours.
You can use the `--force` flag to skip the confirmation.

## Features

* TODO

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/berleon/savethat_cookiecutter/) project template.
