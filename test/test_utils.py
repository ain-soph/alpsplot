
#!/usr/bin/env python3

from alpsplot.utils import *
import numpy as np


def test_get_roc_curve():
    label = np.arange(10.0)
    pred = np.arange(10.0)
    pred[5:] += 1
    get_roc_curve(label, pred)


def test_normalize():
    x = np.arange(10.0)
    normalize(x)


def test_avg_smooth():
    x = np.arange(10.0)
    avg_smooth(x)


def test_monotone():
    x = np.arange(10.0)
    monotone(x, increase=True)
    monotone(x, increase=False)


def test_gaussian_kde():
    x = np.random.randn(32)
    x_grid = np.arange(-3.0, 3.0)
    gaussian_kde(x, x_grid)


def test_groups_err_bar():
    x = np.array([1, 2, 3, 4, 5]*3)
    y = np.arange(15.0)
    groups_err_bar(x, y)


def test_flatten_err_bar():
    x = np.array([1, 2, 3, 4, 5]*3)
    y = np.arange(15.0)
    y_dict = groups_err_bar(x, y)
    flatten_err_bar(y_dict)


def test_adjust_err_bar():
    x = np.array([1, 2, 3, 4, 5]*3)
    y = np.arange(15.0)
    y_dict = groups_err_bar(x, y)
    adjust_err_bar(y_dict, mean=0.3, std=0.4)


def test_normalize_err_bar():
    x = np.array([1, 2, 3, 4, 5]*3)
    y = np.arange(15.0)
    normalize_err_bar(x, y)


def test_avg_smooth_err_bar():
    x = np.array([1, 2, 3, 4, 5]*3)
    y = np.arange(15.0)
    avg_smooth_err_bar(x, y)
