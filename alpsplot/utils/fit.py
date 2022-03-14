#!/usr/bin/env python3

import numpy as np
from scipy.interpolate import UnivariateSpline
# from scipy.optimize import curve_fit

__all__ = ['poly_fit', 'tanh_fit', 'atan_fit',
           'exp_fit', 'inverse_fit', 'interp_fit']


def poly_fit(x: np.ndarray, y: np.ndarray, x_grid: np.ndarray,
             degree: int = 1) -> np.ndarray:
    r"""Use a polynomial of certain degree
    to fit (:attr:`x`, :attr:`y`) series
    and return :attr:`y_grid` wrt :attr:`x_grid`.

    Args:
        x, y (numpy.ndarray): The data to fit.
        x_grid (numpy.ndarray): The x grid array.
        degree (int): The degree of polynomial to fit. Defaults to ``1``.

    Returns:
        numpy.ndarray: The :attr:`y_grid` array wrt :attr:`x_grid`.

    :Example:
        .. code-block:: python
            :emphasize-lines: 8, 9

            import numpy as np
            import matplotlib.pyplot as plt
            from alpsplot.utils.fit import poly_fit

            x = np.arange(10, step=0.5)
            x_grid = np.arange(10, step=0.1)
            y = x + 3 * np.sin(x)
            y1_grid = poly_fit(x, y, x_grid)
            y2_grid = poly_fit(x, y, x_grid, degree=4)

            plt.scatter(x, y, color='red')
            plt.plot(x_grid, y1_grid, color='green', label='degree = 1')
            plt.plot(x_grid, y2_grid, color='blue', label='degree = 4')
            plt.legend()
            plt.show()

        .. image:: /images/utils/poly_fit.svg
            :width: 60%
    """
    z = np.polyfit(x, y, degree)
    y_grid = np.polyval(z, x_grid)
    return y_grid


def tanh_fit(x: np.ndarray, y: np.ndarray, x_grid: np.ndarray,
             degree: int = 1, mean_offset: float = 0.0,
             eps: float = 1e-5) -> np.ndarray:
    r"""Use a tanh(polynomial) of certain degree
    to fit (:attr:`x`, :attr:`y`) series
    and return :attr:`y_grid` wrt :attr:`x_grid`.

    .. math::
        \begin{cases}
        \mu    &= \frac{min(y) + max(y)}{2} + mean\_offset \\
        \sigma &= \max(|y - \mu|) * (1 + \varepsilon)
        \end{cases} \\

        \hat{y} = \sigma \cdot \tanh(p(x)) + \mu

    Args:
        x, y (numpy.ndarray): The data to fit.
        x_grid (numpy.ndarray): The x grid array.
        degree (int): The degree of polynomial to fit. Defaults to ``1``.
        mean_offset (float): The mean offset. Defaults to ``0.0``.
        eps (float): :math:`\varepsilon` to control the scale. Defaults to ``1e-5``.

    Returns:
        numpy.ndarray: the :attr:`y_grid` array wrt :attr:`x_grid`.

    :Example:
        .. code-block:: python
            :emphasize-lines: 8-10

            import numpy as np
            import matplotlib.pyplot as plt
            from alpsplot.utils.fit import tanh_fit

            x = np.arange(3, 4, step=0.1)
            x_grid = np.arange(3, 4, step=0.02)
            y = 3 * np.tanh(x**3 - 3 * x**2 - 7) + 4
            y1_grid = tanh_fit(x, y, x_grid)
            y2_grid = tanh_fit(x, y, x_grid, mean_offset=0.5)
            y3_grid = tanh_fit(x, y, x_grid, degree=3)

            plt.scatter(x, y, color='red')
            plt.plot(x_grid, y1_grid, color='green', label='degree = 1')
            plt.plot(x_grid, y2_grid, color='orange', label='degree = 1 (offset)')
            plt.plot(x_grid, y3_grid, color='blue', label='degree = 3')
            plt.legend()
            plt.show()

        .. image:: /images/utils/tanh_fit.svg
            :width: 60%
    """  # noqa: E501
    mean = (max(y) + min(y)) / 2 + mean_offset
    std = max(abs(y - mean)) * (1 + eps)
    real_data = np.arctanh((y - mean) / std)
    z = np.polyfit(x, real_data, degree)
    y_grid = np.tanh(np.polyval(z, x_grid)) * std + mean
    return y_grid


def atan_fit(x: np.ndarray, y: np.ndarray, x_grid: np.ndarray,
             degree: int = 1, mean_offset: float = 0.0,
             eps: float = 1e-5) -> np.ndarray:
    r"""Use a tanh(polynomial) of certain degree
    to fit (:attr:`x`, :attr:`y`) series
    and return :attr:`y_grid` wrt :attr:`x_grid`.

    .. math::
        \begin{cases}
        \mu    &= \frac{min(y) + max(y)}{2} + mean\_offset \\
        \sigma &= \max(|y - \mu|) * (1 + \varepsilon)
        \end{cases} \\

        \hat{y} = \sigma \cdot \arctan(p(x)) +\mu

    Args:
        x, y (numpy.ndarray): The data to fit.
        x_grid (numpy.ndarray): The x grid array.
        degree (int): The degree of polynomial to fit. Defaults to ``1``.
        mean_offset (float): The mean offset. Defaults to ``0.0``.
        eps (float): :math:`\varepsilon` to control the scale. Defaults to ``1e-5``.

    Returns:
        numpy.ndarray: The :attr:`y_grid` array wrt :attr:`x_grid`.

    :Example:
        .. code-block:: python
            :emphasize-lines: 8-10

            import numpy as np
            import matplotlib.pyplot as plt
            from alpsplot.utils.fit import atan_fit

            x = np.arange(3, 4, step=0.1)
            x_grid = np.arange(3, 4, step=0.02)
            y = 3 * np.arctan(x**3 - 3 * x**2 - 7) + 4
            y1_grid = atan_fit(x, y, x_grid)
            y2_grid = atan_fit(x, y, x_grid, mean_offset=0.5)
            y3_grid = atan_fit(x, y, x_grid, degree=3)

            plt.scatter(x, y, color='red')
            plt.plot(x_grid, y1_grid, color='green', label='degree = 1')
            plt.plot(x_grid, y2_grid, color='orange', label='degree = 1 (offset)')
            plt.plot(x_grid, y3_grid, color='blue', label='degree = 3')
            plt.legend()
            plt.show()

        .. image:: /images/utils/atan_fit.svg
            :width: 60%
    """  # noqa: E501
    mean = (max(y) + min(y)) / 2 + mean_offset
    std = max(abs(y - mean)) * (1 + eps)
    real_data = np.tan((y - mean) / std)
    z = np.polyfit(x, real_data, degree)
    y_grid = np.tanh(np.polyval(z, x_grid)) * std + mean
    return y_grid


def exp_fit(x: np.ndarray, y: np.ndarray, x_grid: np.ndarray,
            degree: int = 1, sign: bool = None,
            eps: float = 1e-5) -> np.ndarray:
    r"""Use a exp(polynomial) of certain degree
    to fit (:attr:`x`, :attr:`y`) series
    and return :attr:`y_grid` wrt :attr:`x_grid`.

    .. math::
        \hat{y} =
        \begin{cases}
            e^{p(x)} - \varepsilon + \min(y) &\text{if } sign \\
            -e^{p(x)} + \varepsilon + \max(y) &\text{else}
        \end{cases}

    Args:
        x, y (numpy.ndarray): The data to fit.
        x_grid (numpy.ndarray): The x grid array.
        degree (int): The degree of polynomial to fit. Defaults to ``1``.
        sign (bool): whether exp is positive, ``None`` means auto pick.
            Defaults to ``None``.
        eps (float): :math:`\varepsilon`. Defaults to ``1e-5``.

    Returns:
        numpy.ndarray: The :attr:`y_grid` array wrt :attr:`x_grid`.

    :Example:
        .. code-block:: python
            :emphasize-lines: 10-11

            import numpy as np
            import matplotlib.pyplot as plt
            from alpsplot.utils.fit import exp_fit

            fig, (ax1, ax2) = plt.subplots(1,2)

            x = np.arange(1, 2, step=0.1)
            x_grid = np.arange(1, 2, step=0.01)
            y = 0.1 * np.exp(x**3 - 2 * x**2 + 4 * x - 2) + 4
            y1_grid = exp_fit(x, y, x_grid, eps=0.1*np.e)
            y2_grid = exp_fit(x, y, x_grid, degree=3, eps=0.1*np.e)

            ax1.scatter(x, y, color='red')
            ax1.plot(x_grid, y1_grid, color='green', label='degree = 1')
            ax1.plot(x_grid, y2_grid, color='blue', label='degree = 3')
            ax1.legend()

            y1_grid = exp_fit(x, -y, x_grid, eps=0.1*np.e)
            y2_grid = exp_fit(x, -y, x_grid, degree=3, eps=0.1*np.e)

            ax2.scatter(x, -y, color='red')
            ax2.plot(x_grid, y1_grid, color='green', label='degree = 1')
            ax2.plot(x_grid, y2_grid, color='blue', label='degree = 3')
            ax2.legend()

            plt.show()

        .. image:: /images/utils/exp_fit.svg
            :width: 60%
    """
    if sign is None:
        y1 = exp_fit(x, y, x, degree=degree, sign=True, eps=eps)
        y2 = exp_fit(x, y, x, degree=degree, sign=False, eps=eps)
        std1, std2 = np.std(y1-y), np.std(y2-y)
        sign = std1 < std2
    offset = min(y) - eps if sign else max(y) + eps
    real_data = np.log(abs(y - offset))
    z = np.polyfit(x, real_data, degree)
    fit_data = np.exp(np.polyval(z, x_grid))
    fit_data = fit_data if sign else -fit_data
    y_grid = fit_data + offset
    return y_grid


def inverse_fit(x: np.ndarray, y: np.ndarray, x_grid: np.ndarray,
                degree: int = 1, sign: bool = None,
                eps: float = 1e-5) -> np.ndarray:
    r"""Use a tanh(polynomial) of certain degree
    to fit (:attr:`x`, :attr:`y`) series
    and return :attr:`y_grid` wrt :attr:`x_grid`.

    .. math::
        \hat{y} = \frac{1}{p(x)} - \varepsilon +
        \begin{cases}
            \min(y) &\text{if } sign \\
            \max(y) &\text{else}
        \end{cases}

        \hat{y}=\frac{1}{p(x)}+\varepsilon

    Args:
        x, y (numpy.ndarray): The data to fit.
        x_grid (numpy.ndarray): The x grid array.
        degree (int): The degree of polynomial to fit. Defaults to ``1``.
        sign (bool): Whether reciprocal is positive, ``None`` means auto pick.
            Defaults to ``None``.
        eps (float): :math:`\varepsilon`. Defaults to ``1e-5``.

    Returns:
        numpy.ndarray: the :attr:`y_grid` array wrt :attr:`x_grid`.

    :Example:
        .. code-block:: python
            :emphasize-lines: 10-11

            import numpy as np
            import matplotlib.pyplot as plt
            from alpsplot.utils.fit import inverse_fit

            fig, (ax1, ax2) = plt.subplots(1,2)

            x = np.arange(1, 2, step=0.1)
            x_grid = np.arange(1, 2, step=0.01)
            y = 6 / (x**3 - 2 * x**2 + 4 * x - 2) + 4
            y1_grid = inverse_fit(x, y, x_grid, eps=1)
            y2_grid = inverse_fit(x, y, x_grid, degree=3, eps=1)

            ax1.scatter(x, y, color='red')
            ax1.plot(x_grid, y1_grid, color='green', label='degree = 1')
            ax1.plot(x_grid, y2_grid, color='blue', label='degree = 3')
            ax1.legend()

            y1_grid = inverse_fit(x, -y, x_grid, eps=1)
            y2_grid = inverse_fit(x, -y, x_grid, degree=3, eps=1)

            ax2.scatter(x, -y, color='red')
            ax2.plot(x_grid, y1_grid, color='green', label='degree = 1')
            ax2.plot(x_grid, y2_grid, color='blue', label='degree = 3')
            ax2.legend()

            plt.show()

        .. image:: /images/utils/inverse_fit.svg
            :width: 60%
    """
    if sign is None:
        y1 = inverse_fit(x, y, x, degree=degree, sign=True, eps=eps)
        y2 = inverse_fit(x, y, x, degree=degree, sign=False, eps=eps)
        std1, std2 = np.std(y1 - y), np.std(y2 - y)
        sign = std1 < std2
    offset = min(y) - eps if sign else max(y) + eps
    real_data = np.reciprocal(y - offset)
    z = np.polyfit(x, real_data, degree)
    fit_data = np.reciprocal(np.polyval(z, x_grid))
    y_grid = fit_data + offset
    return y_grid


def interp_fit(x: np.ndarray, y: np.ndarray, x_grid: np.ndarray,
               **kwargs) -> np.ndarray:
    r"""Use :any:`scipy.interpolate.UnivariateSpline()
    <scipy.interpolate.UnivariateSpline>`
    to fit (:attr:`x`, :attr:`y`) series
    and return :attr:`y_grid` wrt :attr:`x_grid`.

    Args:
        x, y (numpy.ndarray): The data to fit.
        x_grid (numpy.ndarray): The x grid array.
        **kwargs: The lower bound of y. Defaults to ``0.0``.

    Returns:
        numpy.ndarray: The :attr:`y_grid` array wrt :attr:`x_grid`.

    :Example:
        .. code-block:: python
            :emphasize-lines: 8

            import numpy as np
            import matplotlib.pyplot as plt
            from alpsplot.utils.fit import interp_fit

            x = np.arange(10, step=0.5)
            x_grid = np.arange(10, step=0.1)
            y = x + 3 * np.sin(x)
            y_grid = interp_fit(x, y, x_grid)

            plt.scatter(x, y, color='red')
            plt.plot(x_grid, y_grid, color='green')
            plt.legend()
            plt.show()

        .. image:: /images/utils/interp_fit.svg
            :width: 60%
    """
    func = UnivariateSpline(x, y, **kwargs)
    y_grid = func(x_grid)
    return y_grid
