#!/usr/bin/env python3

import numpy as np
from alpsplot.utils.fit import (poly_fit, tanh_fit, atan_fit,
                                exp_fit, inverse_fit, interp_fit)


def test_poly_fit():
    x = np.arange(10, step=0.5)
    x_grid = np.arange(10, step=0.1)
    y = x + 3 * np.sin(x)
    poly_fit(x, y, x_grid)
    poly_fit(x, y, x_grid, degree=4)


def test_tanh_fit():
    x = np.arange(3, 4, step=0.1)
    x_grid = np.arange(3, 4, step=0.02)
    y = 3 * np.tanh(x**3 - 3 * x**2 - 7) + 4
    tanh_fit(x, y, x_grid)
    tanh_fit(x, y, x_grid, mean_offset=0.5)
    tanh_fit(x, y, x_grid, degree=3)


def test_atan_fit():
    x = np.arange(3, 4, step=0.1)
    x_grid = np.arange(3, 4, step=0.02)
    y = 3 * np.arctan(x**3 - 3 * x**2 - 7) + 4
    atan_fit(x, y, x_grid)
    atan_fit(x, y, x_grid, mean_offset=0.5)
    atan_fit(x, y, x_grid, degree=3)


def test_exp_fit():
    x = np.arange(1, 2, step=0.1)
    x_grid = np.arange(1, 2, step=0.01)
    y = 0.1 * np.exp(x**3 - 2 * x**2 + 4 * x - 2) + 4
    exp_fit(x, y, x_grid, eps=0.1*np.e)
    exp_fit(x, y, x_grid, degree=3, eps=0.1*np.e)
    exp_fit(x, -y, x_grid, eps=0.1*np.e)
    exp_fit(x, -y, x_grid, degree=3, eps=0.1*np.e)


def test_inverse_fit():
    x = np.arange(1, 2, step=0.1)
    x_grid = np.arange(1, 2, step=0.01)
    y = 6 / (x**3 - 2 * x**2 + 4 * x - 2) + 4
    inverse_fit(x, y, x_grid, eps=1)
    inverse_fit(x, y, x_grid, degree=3, eps=1)
    inverse_fit(x, -y, x_grid, eps=1)
    inverse_fit(x, -y, x_grid, degree=3, eps=1)


def test_interp_fit():
    x = np.arange(10, step=0.5)
    x_grid = np.arange(10, step=0.1)
    y = x + 3 * np.sin(x)
    interp_fit(x, y, x_grid)
