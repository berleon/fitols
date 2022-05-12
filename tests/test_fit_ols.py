#!/usr/bin/env python
"""Tests for `fitols` package."""

from pathlib import Path

import savethat

from fitols import fit_ols


def test_fit_ols(env_file: Path) -> None:
    args = fit_ols.FitOLSArgs(
        dataset="california_housing",
        target="MedHouseVal",
    )
    node = savethat.create_node(
        fit_ols.FitOLS,
        env_file,
        args,
    )
    node.run()
