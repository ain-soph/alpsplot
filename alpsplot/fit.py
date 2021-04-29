#!/usr/bin/env python3

import numpy as np
from scipy.interpolate import UnivariateSpline
# from scipy.optimize import curve_fit


def poly_fit(x: np.ndarray, y: np.ndarray, x_grid: np.ndarray, degree: int = 1) -> np.ndarray:
    z = np.polyfit(x, y, degree)
    y_grid = np.polyval(z, x_grid)
    return y_grid


def tanh_fit(x: np.ndarray, y: np.ndarray, x_grid: np.ndarray,
             degree: int = 1, mean_bias: float = 0.0, scale_multiplier: float = 1.0) -> np.ndarray:
    mean = (max(y) + min(y)) / 2 + mean_bias
    scale = max(abs(y - mean)) * scale_multiplier
    fit_data = np.arctanh((y - mean) / scale)
    z = np.polyfit(x, fit_data, degree)
    y_grid = np.tanh(np.polyval(z, x_grid)) * scale + mean
    return y_grid


def atan_fit(x: np.ndarray, y: np.ndarray, x_grid: np.ndarray,
             degree: int = 1, mean_bias: float = 0.0, scale_multiplier: float = 1.0) -> np.ndarray:
    mean = (max(y) + min(y)) / 2 + mean_bias
    scale = max(abs(y - mean)) * scale_multiplier
    fit_data = np.tan((y - mean) / scale)
    z = np.polyfit(x, fit_data, degree)
    y_grid = np.tanh(np.polyval(z, x_grid)) * scale + mean
    return y_grid


def exp_fit(x: np.ndarray, y: np.ndarray, x_grid: np.ndarray,
            degree: int = 1, increase: bool = True, eps: float = 0.01) -> np.ndarray:
    y_max = max(y)
    y_min = min(y)
    if increase:
        fit_data = np.log(y + eps - y_min)
    else:
        fit_data = np.log(y_max + eps - y)

    z = np.polyfit(x, fit_data, degree)
    y_grid = np.exp(np.polyval(z, x_grid))
    if increase:
        y_grid += y_min - eps
    else:
        y_grid = y_max + eps - y_grid
    return y_grid


def inverse_fit(x: np.ndarray, y: np.ndarray, x_grid: np.ndarray,
                degree: int = 1, y_lower_bound: float = 0.0) -> np.ndarray:
    fit_data = 1 / (y - y_lower_bound)
    z = np.polyfit(x, fit_data, degree)
    y_grid = 1 / (np.polyval(z, x_grid)) + y_lower_bound
    return y_grid


def interp_fit(x: np.ndarray, y: np.ndarray, x_grid: np.ndarray, interp_num: int = 20) -> np.ndarray:
    func = UnivariateSpline(x, y, s=interp_num)
    y_grid = func(x_grid)
    return y_grid
