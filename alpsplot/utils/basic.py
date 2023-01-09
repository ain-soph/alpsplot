#!/usr/bin/env python3

import numpy as np
# scipy.stats.gaussian_kde

__all__ = ['normalize', 'avg_smooth', 'monotone']


def normalize(x: np.ndarray,
              _min: float = None, _max: float = None,
              tgt_min: float = 0.0, tgt_max: float = 1.0
              ) -> np.ndarray:
    r"""Normalize a :any:`numpy.ndarray` into desired range.

    .. math::
        \frac{tgt\_max - tgt\_min}{\_max - \_min}(x - \_min) + tgt\_min

    Args:
        x (numpy.ndarray): The unnormalized array.
        _min (float): The lower bound of original :attr:`x`.
            Defaults to ``min(x)``.
        _max (float): The upper bound of original :attr:`x`.
            Defaults to ``max(x)``.
        tgt_min (float): The lower bound of original :attr:`x`.
            Defaults to ``0.0``.
        tgt_max (float): The upper bound of original :attr:`x`.
            Defaults to ``1.0``.

    Returns:
        numpy.ndarray: A normalized array.

    :Example:
        >>> import numpy as np
        >>> from alpsplot.utils import normalize
        >>>
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


def avg_smooth(x: np.ndarray, window: int = 3,
               method: str = 'mean') -> np.ndarray:
    r"""Average smooth a :any:`numpy.ndarray` using a given window size.

    Paddings are added at head and tail.

    Args:
        x (numpy.ndarray): The unsmoothed array.
        window (int): The window size (number of points). Defaults to ``3``.
        method (str): Choose from ``['mean', 'median', 'min', 'max']``.
            Defaults to ``'mean'``.

    Returns:
        numpy.ndarray: A smoothed array.

    :Example:
        .. code-block:: python
            :emphasize-lines: 7-8

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
    start = window//2
    expand_x = np.interp(np.arange(len(x) + window), np.arange(len(x)) + start,
                         x)
    for i in range(len(x)):
        value = expand_x[i: i + window]
        match method:
            case 'mean':
                new_x[i] = np.mean(value)
            case 'median':
                new_x[i] = np.median(value)
            case 'min':
                new_x[i] = np.min(value)
            case 'max':
                new_x[i] = np.max(value)
            case _:
                raise NotImplementedError(f'{method} not supported yet.')
    return new_x


def monotone(x: np.ndarray, increase: bool = True,
             reverse: bool = False) -> np.ndarray:
    r"""Monotonize a :any:`numpy.ndarray`.

    All non-monotonic points would be clipped as previous value.

    Args:
        x (numpy.ndarray): The non-monotonic array.
        increase (bool): Monotonically increase or decrease.
            Defaults to ``True``.
        reverse (bool): Enable to clip from right to left.
            Defaults to ``False``.

    Returns:
        numpy.ndarray: A monotonic array.

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
    ascend = increase != reverse
    temp: float = min(x) if ascend else max(x)
    for i in range(len(x)):
        if reverse:
            i = -i-1
        if ((ascend and x[i] < temp) or (not ascend and x[i] > temp)):
            y[i] = temp
        else:
            temp = x[i]
    return y
