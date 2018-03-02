#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from lightDisplay import lightDisplay

__author__ = "SBean92"
__copyright__ = "SBean92"
__license__ = "mit"


def test_lightDisplay():
    grid = lightDisplay(100)
    grid.action("turn on", 0, 10, 0,10)
    assert grid.count() = "There are 100 lights on and 9900 lights off"
