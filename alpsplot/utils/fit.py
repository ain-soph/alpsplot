#!/usr/bin/env python3

import numpy as np
from scipy.interpolate import UnivariateSpline
# from scipy.optimize import curve_fit

EPS = 1e-5


def poly_fit(x: np.ndarray, y: np.ndarray, x_grid: np.ndarray, degree: int = 1) -> np.ndarray:
    r"""
    use a polynomial of certain degree to fit (:attr:`x`, :attr:`y`) series and return :attr:`y_grid` wrt :attr:`x_grid`.

    Args:
        x, y (numpy.ndarray): the data to fit.
        x_grid (numpy.ndarray): the x grid array.
        degree (int): the degree of polynomial to fit. Default: `1`.

    Returns:
        numpy.ndarray: the :attr:`y_grid` array wrt :attr:`x_grid`.

    Example::

        >>> import numpy as np
        >>> import matplotlib.pyplot as plt
        >>> from alpsplot.utils import poly_fit
        >>> x = np.arange(10, step=0.5)
        >>> x_grid = np.arange(10, step=0.1)
        >>> y = x + 3 * np.sin(x)
        >>> y1_grid = poly_fit(x, y, x_grid)
        >>> y2_grid = poly_fit(x, y, x_grid, degree=4)
        >>> plt.scatter(x, y, color='red')
        >>> plt.plot(x_grid, y1_grid, color='green', label='degree = 1')
        >>> plt.plot(x_grid, y2_grid, color='blue', label='degree = 4')
        >>> plt.legend()
        >>> plt.show()

    .. raw:: html

        <object style="width:60%" data="/alpsplot/_static/img/utils/poly_fit.svg"></object>

    """
    z = np.polyfit(x, y, degree)
    y_grid = np.polyval(z, x_grid)
    return y_grid


def tanh_fit(x: np.ndarray, y: np.ndarray, x_grid: np.ndarray,
             degree: int = 1, mean_offset: float = 0.0, std_multiplier: float = 1.0) -> np.ndarray:
    r"""
    use a tanh(polynomial) of certain degree to fit (:attr:`x`, :attr:`y`) series and return :attr:`y_grid` wrt :attr:`x_grid`.

    .. math::
        \begin{cases}
        \mu&=\frac{min(y)+max(y)}{2}+mean\_offset \\
        \sigma&=\max(|y-\mu|)*std\_multiplier+EPS(1e-5)
        \end{cases} \\

        \hat{y}=\sigma\cdot\tanh(p(x))+\mu

    Args:
        x, y (numpy.ndarray): the data to fit.
        x_grid (numpy.ndarray): the x grid array.
        degree (int): the degree of polynomial to fit. Default: `1`.
        mean_offset (float): the mean offset. Default: `0.0`.
        std_multiplier (float): the std offset. Default: `1.0`.

    Returns:
        numpy.ndarray: the :attr:`y_grid` array wrt :attr:`x_grid`.

    Example::

        >>> import numpy as np
        >>> import matplotlib.pyplot as plt
        >>> from alpsplot.utils import tanh_fit
        >>> x = np.arange(3, 4, step=0.1)
        >>> x_grid = np.arange(3, 4, step=0.02)
        >>> y = 3 * np.tanh(x**3 - 3 * x**2 - 7) + 4
        >>> y1_grid = tanh_fit(x, y, x_grid)
        >>> y2_grid = tanh_fit(x, y, x_grid, mean_offset=0.1, std_multiplier=1.1)
        >>> y3_grid = tanh_fit(x, y, x_grid, degree=3)
        >>> plt.scatter(x, y, color='red')
        >>> plt.plot(x_grid, y1_grid, color='green', label='degree = 1')
        >>> plt.plot(x_grid, y2_grid, color='orange', label='degree = 1 (offset)')
        >>> plt.plot(x_grid, y3_grid, color='blue', label='degree = 3')
        >>> plt.legend()
        >>> plt.show()

    .. raw:: html

        <object style="width:60%" data="/alpsplot/_static/img/utils/tanh_fit.svg"></object>

    """
    mean = (max(y) + min(y)) / 2 + mean_offset
    std = max(abs(y - mean)) * std_multiplier + EPS
    fit_data = np.arctanh((y - mean) / std)
    z = np.polyfit(x, fit_data, degree)
    y_grid = np.tanh(np.polyval(z, x_grid)) * std + mean
    return y_grid


def atan_fit(x: np.ndarray, y: np.ndarray, x_grid: np.ndarray,
             degree: int = 1, mean_offset: float = 0.0, std_multiplier: float = 1.0) -> np.ndarray:
    r"""
    use a tanh(polynomial) of certain degree to fit (:attr:`x`, :attr:`y`) series and return :attr:`y_grid` wrt :attr:`x_grid`.

    .. math::
        \begin{cases}
        \mu&=\frac{min(y)+max(y)}{2}+mean\_offset \\
        \sigma&=\max(|y-\mu|)*std\_multiplier+EPS(1e-5)
        \end{cases} \\

        \hat{y}=\sigma\cdot\arctan(p(x))+\mu

    Args:
        x, y (numpy.ndarray): the data to fit.
        x_grid (numpy.ndarray): the x grid array.
        degree (int): the degree of polynomial to fit. Default: `1`.
        mean_offset (float): the mean offset. Default: `0.0`.
        std_multiplier (float): the std offset. Default: `1.0`.

    Returns:
        numpy.ndarray: the :attr:`y_grid` array wrt :attr:`x_grid`.

    Example::

        >>> import numpy as np
        >>> import matplotlib.pyplot as plt
        >>> from alpsplot.utils import atan_fit
        >>> x = np.arange(3, 4, step=0.1)
        >>> x_grid = np.arange(3, 4, step=0.02)
        >>> y = 3 * np.arctan(x**3 - 3 * x**2 - 7) + 4
        >>> y1_grid = atan_fit(x, y, x_grid)
        >>> y2_grid = atan_fit(x, y, x_grid, mean_offset=0.1, std_multiplier=1.1)
        >>> y3_grid = atan_fit(x, y, x_grid, degree=3)
        >>> plt.scatter(x, y, color='red')
        >>> plt.plot(x_grid, y1_grid, color='green', label='degree = 1')
        >>> plt.plot(x_grid, y2_grid, color='orange', label='degree = 1 (offset)')
        >>> plt.plot(x_grid, y3_grid, color='blue', label='degree = 3')
        >>> plt.legend()
        >>> plt.show()

    .. raw:: html

        <object style="width:60%" data="/alpsplot/_static/img/utils/atan_fit.svg"></object>

    """
    mean = (max(y) + min(y)) / 2 + mean_offset
    std = max(abs(y - mean)) * std_multiplier + EPS
    fit_data = np.tan((y - mean) / std)
    z = np.polyfit(x, fit_data, degree)
    y_grid = np.tanh(np.polyval(z, x_grid)) * std + mean
    return y_grid


def exp_fit(x: np.ndarray, y: np.ndarray, x_grid: np.ndarray,
            degree: int = 1, increase: bool = True, eps: float = 0.01) -> np.ndarray:
    y_max = max(y)
    y_min = min(y)

    fit_data = np.log(y + eps - y_min) if increase else np.log(y_max + eps - y)
    z = np.polyfit(x, fit_data, degree)
    y_grid = np.exp(np.polyval(z, x_grid))
    if increase:
        y_grid += y_min - eps
    else:
        y_grid = y_max + eps - y_grid
    return y_grid


def inverse_fit(x: np.ndarray, y: np.ndarray, x_grid: np.ndarray,
                degree: int = 1, y_lower_bound: float = 0.0) -> np.ndarray:
    r"""
    use a tanh(polynomial) of certain degree to fit (:attr:`x`, :attr:`y`) series and return :attr:`y_grid` wrt :attr:`x_grid`.

    .. math::

        \hat{y}=\frac{1}{p(x)}+y\_lower\_bound

    Args:
        x, y (numpy.ndarray): the data to fit.
        x_grid (numpy.ndarray): the x grid array.
        degree (int): the degree of polynomial to fit. Default: `1`.
        y_lower_bound (float): the lower bound of y. Default: `0.0`.

    Returns:
        numpy.ndarray: the :attr:`y_grid` array wrt :attr:`x_grid`.

    Example::

        >>> import numpy as np
        >>> import matplotlib.pyplot as plt
        >>> from alpsplot.utils import inverse_fit
        >>> x = np.arange(3, 4, step=0.1)
        >>> x_grid = np.arange(3, 4, step=0.02)
        >>> y = 6 / (x**3 - 2 * x**2 + 4 * x - 2) + 4
        >>> y1_grid = inverse_fit(x, y, x_grid)
        >>> y2_grid = inverse_fit(x, y, x_grid, y_lower_bound=4)
        >>> y3_grid = inverse_fit(x, y, x_grid, degree=3, y_lower_bound=4)
        >>> plt.scatter(x, y, color='red')
        >>> plt.plot(x_grid, y1_grid, color='green', label='degree = 1')
        >>> plt.plot(x_grid, y2_grid, color='orange', label='degree = 1 (offset)')
        >>> plt.plot(x_grid, y3_grid, color='blue', label='degree = 3 (offset)')
        >>> plt.legend()
        >>> plt.show()

    .. raw:: html

        <object style="width:60%" data="/alpsplot/_static/img/utils/inverse_fit.svg"></object>

    """
    fit_data = 1 / (y - y_lower_bound)
    z = np.polyfit(x, fit_data, degree)
    y_grid = 1 / (np.polyval(z, x_grid)) + y_lower_bound
    return y_grid


def interp_fit(x: np.ndarray, y: np.ndarray, x_grid: np.ndarray, **kwargs) -> np.ndarray:
    r"""
    use :any:`scipy.interpolate.UnivariateSpline` to fit (:attr:`x`, :attr:`y`) series and return :attr:`y_grid` wrt :attr:`x_grid`.

    Args:
        x, y (numpy.ndarray): the data to fit.
        x_grid (numpy.ndarray): the x grid array.
        **kwargs: the lower bound of y. Default: `0.0`.

    Returns:
        numpy.ndarray: the :attr:`y_grid` array wrt :attr:`x_grid`.

    Example::

        >>> import numpy as np
        >>> import matplotlib.pyplot as plt
        >>> from alpsplot.utils import interp_fit
        >>> x = np.arange(10, step=0.5)
        >>> x_grid = np.arange(10, step=0.1)
        >>> y = x + 3 * np.sin(x)
        >>> y_grid = interp_fit(x, y, x_grid)
        >>> plt.scatter(x, y, color='red')
        >>> plt.plot(x_grid, y_grid, color='green')
        >>> plt.legend()
        >>> plt.show()

    .. raw:: html

        <object style="width:60%" data="/alpsplot/_static/img/utils/interp_fit.svg"></object>

    """
    func = UnivariateSpline(x, y, **kwargs)
    y_grid = func(x_grid)
    return y_grid
