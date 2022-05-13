# FitOLS


[![Build Status](https://github.com/berleon/fitols/actions/workflows/dev.yml/badge.svg)](https://github.com/berleon/fitols/actions/workflows/dev.yml)
[![codecov](https://codecov.io/gh/berleon/fitols/branch/main/graphs/badge.svg)](https://codecov.io/github/berleon/fitols)



Examplary realization of the savethat_cookiecutter template


* Documentation: <https://berleon.github.io/fitols>
* GitHub: <https://github.com/berleon/fitols>
* PyPI: <https://pypi.org/project/fitols/>
* Free software: MIT



## Setup


### Get it running


To install this project, run:

```bash
mkdir fitols                   # this directory will hold the code, data and venv
cd fitols
python3 -m venv venv                                    # create and load the virtual environment
source venv/bin/activate
# create the data folder
mkdir data
git clone https://github.com/berleon/fitols.git
cd fitols
pip install -U pip wheel poetry
poetry install
python -m fitols nodes         # now you can list the available nodes
make test                                               # or run the tests
```

## Command line interface

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

All failed runs from the last 3 hours can be deleted with:

```
python -m fitols rm FitOLS --failed --last 3h
```
The CLI would ask for confirmation before deleting all completed runs in the last 3 hours.
You can use the `--force` flag to skip the confirmation.
See `python -m fitols rm  --help ` for more information.

## Features

* TODO

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/berleon/savethat_cookiecutter/) project template.
