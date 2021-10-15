#!/usr/bin/env python3

import numpy as np
# scipy.stats.gaussian_kde


def normalize(x: np.ndarray,
              _min: float = None, _max: float = None,
              tgt_min: float = 0.0, tgt_max: float = 1.0
              ) -> np.ndarray:
    r"""
    normalize a `numpy.ndarray` into desired range.

    .. math::
        \frac{tgt\_max - tgt\_min}{\_max - \_min}(x - \_min) + tgt\_min

    Args:
        x (numpy.ndarray): the unnormalized array.
        _min (float): the lower bound of original :attr:`x`.
            Default: `min(x)`.
        _max (float): the upper bound of original :attr:`x`.
            Default: `max(x)`.
        tgt_min (float): the lower bound of original :attr:`x`. Default: `0.0`.
        tgt_max (float): the upper bound of original :attr:`x`. Default: `1.0`.

    Returns:
        numpy.ndarray: a normalized array.

    :Example:

        >>> import numpy as np
        >>> from alpsplot.utils import normalize
        >>> x = np.array([-10, -5, 0, 5, 10])
        >>> normalize(x)
        array([0.  , 0.25, 0.5 , 0.75, 1.  ])
        >>> normalize(x, _min=-100, _max=100)
        array([0.45 , 0.475, 0.5  , 0.525, 0.55 ])
        >>> normalize(x, tgt_min=-1, tgt_max=1)
        array([-1. , -0.5,  0. ,  0.5,  1. ])

    """
    _min = float(min(x)) if _min is None else _min
    _max = float(max(x)) if _max is None else _max
    x = (x - _min) / (_max - _min) * (tgt_max - tgt_min) + tgt_min
    return x


def avg_smooth(x: np.ndarray, window: int = 3) -> np.ndarray:
    r"""
    average smooth a `numpy.ndarray` using a given window size.
    Paddings are added at head and tail.

    Args:
        x (numpy.ndarray): the unsmoothed array.
        window (int): the window size (number of points). Default: `3`.

    Returns:
        numpy.ndarray: a smoothed array.

    :Example:
        .. code-block:: python
            :emphasize-lines: 7, 8

            import numpy as np
            import matplotlib.pyplot as plt
            from alpsplot.utils import avg_smooth

            x = np.arange(10, step=1)
            y = x + 3 * np.sin(x)
            y2 = avg_smooth(y)
            y3 = avg_smooth(y, window=5)

            plt.plot(x, y, color='red', label='original')
            plt.plot(x, y2, color='green', label='window = 3')
            plt.plot(x, y3, color='blue', label='window = 5')
            plt.legend()
            plt.show()

        .. image:: /images/utils/avg_smooth.svg
            :width: 60%

    """
    new_x = np.zeros_like(x)
    for i in range(len(x)):
        if i < window // 2:
            new_x[i] = (x[0] * (window // 2 - i) +
                        np.sum(x[: i + (window + 1) // 2])) / window
        elif i >= len(x) - (window - 1) // 2:
            new_x[i] = (x[-1] * ((window + 1) // 2 - len(x) + i) +
                        np.sum(x[i - window // 2:])) / window
        else:
            new_x[i] = np.mean(x[i - window // 2: i + 1 + (window - 1) // 2])
    return new_x


def monotone(x: np.ndarray, increase: bool = True) -> np.ndarray:
    r"""
    monotonize a `numpy.ndarray`.
    All non-monotonic points would be clipped as previous value.

    Args:
        x (numpy.ndarray): the non-monotonic array.
        increase (bool): monotonically increase or decrease. Default: `True`.

    Returns:
        numpy.ndarray: a monotonic array.

    :Example:
        .. code-block:: python
            :emphasize-lines: 7

            import numpy as np
            import matplotlib.pyplot as plt
            from alpsplot.utils import monotone

            x = np.arange(10, step=0.1)
            y = x + 3 * np.sin(x)
            y2 = monotone(y)

            plt.plot(x, y, color='blue', label='original')
            plt.plot(x, y2, color='red', label='monotone')
            plt.legend()
            plt.show()

        .. image:: /images/utils/monotone.svg
            :width: 60%

    """
    y = np.copy(x)
    temp: float = min(x) if increase else max(x)
    for i in range(len(x)):
        if ((increase and x[i] < temp) or (not increase and x[i] > temp)):
            y[i] = temp
        else:
            temp = x[i]
    return y
