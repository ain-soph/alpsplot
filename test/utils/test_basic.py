#!/usr/bin/env python3

from alpsplot.utils import *
import numpy as np


def test_normalize():
    x = np.array([-3, -5, -10, 10, 5, 3])
    assert np.allclose(normalize(x),
                       [0.35, 0.25, 0., 1., 0.75, 0.65])
    assert np.allclose(normalize(x, _min=-100, _max=100),
                       [0.485, 0.475, 0.45, 0.55, 0.525, 0.515])
    assert np.allclose(normalize(x, tgt_min=-1, tgt_max=1),
                       [-0.3, -0.5, -1., 1., 0.5, 0.3])


def test_avg_smooth():
    x = np.arange(10, step=0.5)
    y = x + 3 * np.sin(x)
    avg_smooth(y)
    avg_smooth(y, window=10)
    avg_smooth(y, window=100)


def test_monotone():
    x = np.arange(10, step=0.1)
    y = x + 3 * np.sin(x)
    monotone(y)
    monotone(y, increase=False)
