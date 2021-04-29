#!/usr/bin/env python3

from alpsplot.fit import *


def test_poly_fit():
    x = np.arange(10)
    y = np.sin(x)
    x_grid = np.arange(10, 2)
    poly_fit(x, y, x_grid, degree=3)


def test_tanh_fit():
    x = np.arange(10)
    y = np.sin(x)
    x_grid = np.arange(10, 2)
    tanh_fit(x, y, x_grid, degree=3)


def test_atan_fit():
    x = np.arange(10)
    y = np.sin(x)
    x_grid = np.arange(10, 2)
    atan_fit(x, y, x_grid, degree=3)


def test_exp_fit():
    x = np.arange(10)
    y = np.sin(x)
    x_grid = np.arange(10, 2)
    exp_fit(x, y, x_grid, degree=3, increase=True)
    exp_fit(x, y, x_grid, degree=3, increase=False)


def test_inverse_fit():
    x = np.arange(1, 10)
    y = np.sin(x)
    x_grid = np.arange(2, 10, 2)
    inverse_fit(x, y, x_grid, degree=3)


def test_interp_fit():
    x = np.arange(10)
    y = np.sin(x)
    x_grid = np.arange(10, 2)
    interp_fit(x, y, x_grid, interp_num=5)
