#!/usr/bin/env python3

from .basic import avg_smooth, normalize
import numpy as np

from typing import Union, Optional

__all__ = ['group_err_bar', 'flatten_err_bar', 'adjust_err_bar',
           'normalize_err_bar', 'avg_smooth_err_bar']


def group_err_bar(x: np.ndarray, y: np.ndarray) -> dict[float, np.ndarray]:
    r"""Group (:attr:`x`, :attr:`y`) to be a dict. ``y_dict[x0] = [y0, y1, ...]``.

    Args:
        x (numpy.ndarray): The x array.
        y (numpy.ndarray): The y array.

    Returns:
        dict[float, numpy.ndarray]: The result dict.

    :Example:
        >>> import numpy as np
        >>> from alpsplot.utils import group_err_bar
        >>>
        >>> x = np.array([1., 2., 3.] * 2)
        >>> x
        array([1., 2., 3., 1., 2., 3.])
        >>> y = np.arange(6.0)
        >>> y
        array([0., 1., 2., 3., 4., 5.])
        >>> group_err_bar(x, y)
        {1.0: array([0., 3.]), 2.0: array([1., 4.]), 3.0: array([2., 5.])}
    """
    y_dict: dict[float, np.ndarray] = {}
    for _x in sorted(list(set(x))):
        y_dict[_x] = np.array([y[t] for t in range(len(y)) if x[t] == _x])
    return y_dict


def flatten_err_bar(y_dict: dict[float, np.ndarray]
                    ) -> tuple[np.ndarray, np.ndarray]:
    r"""Flatten :attr:`y_dict` to be data list ``(x, y)``.

    Args:
        y_dict (dict[float, numpy.ndarray]): The dict to flatten.

    Returns:
        (numpy.ndarray, numpy.ndarray): The x, y array.

    :Example:
        >>> import numpy as np
        >>> from alpsplot.utils import group_err_bar, flatten_err_bar
        >>>
        >>> x = np.array([1., 2., 3.] * 2)
        >>> x
        array([1., 2., 3., 1., 2., 3.])
        >>> y = np.arange(6.0)
        >>> y
        array([0., 1., 2., 3., 4., 5.])
        >>> y_dict = group_err_bar(x, y)
        >>> y_dict
        {1.0: array([0., 3.]), 2.0: array([1., 4.]), 3.0: array([2., 5.])}
        >>> flatten_err_bar(y_dict)
        (array([1., 1., 2., 2., 3., 3.]), array([0., 3., 1., 4., 2., 5.]))
    """
    x: list[float] = []
    y: list[float] = []
    for _x in y_dict.keys():
        for _y in y_dict[_x]:
            x.append(_x)
            y.append(_y)
    return np.array(x), np.array(y)


def adjust_err_bar(y_dict: dict[float, np.ndarray],
                   mean: Optional[Union[float, np.ndarray]] = None,
                   std: Optional[Union[float, np.ndarray]] = None
                   ) -> dict[float, np.ndarray]:
    r"""Adjust :attr:`y_dict` with :attr:`mean` and :attr:`std`.

    .. math::
        \frac{std[i]}{y\_dict[x_i].std()}
        \left(y\_dict[x_i] - y\_dict[x_i].mean()\right) + mean[i]

    Args:
        y_dict (dict[float, numpy.ndarray]): The dict to adjust.
        mean (numpy.ndarray]): The new mean values for :attr:`y_dict`.
            ``None`` means keeping the original mean values
            ``[y_dict[x].mean() for x in y_dict.keys()]``.
            Defaults to ``None``.
        std (numpy.ndarray]): The new std values for :attr:`y_dict`.
            ``None`` means keeping the original std values
            ``[y_dict[x].std() for x in y_dict.keys()]``.
            Defaults to ``None``.

    Returns:
        dict[float, numpy.ndarray]: The new dict.

    :Example:
        >>> import numpy as np
        >>> from alpsplot.utils import group_err_bar, adjust_err_bar
        >>>
        >>> x = np.array([1., 2., 3.] * 2)
        >>> x
        array([1., 2., 3., 1., 2., 3.])
        >>> y = np.arange(6.0)
        >>> y
        array([0., 1., 2., 3., 4., 5.])
        >>> y_dict = group_err_bar(x, y)
        >>> y_dict
        {1.0: array([0., 3.]), 2.0: array([1., 4.]), 3.0: array([2., 5.])}
        >>> adjust_err_bar(y_dict)
        {1.0: array([0., 3.]), 2.0: array([1., 4.]), 3.0: array([2., 5.])}
        >>> adjust_err_bar(y_dict, mean=0.3, std=0.4)
        {1.0: array([-0.1,  0.7]), 2.0: array([-0.1,  0.7]), 3.0: array([-0.1,  0.7])}
        >>> adjust_err_bar(y_dict, mean=np.zeros(3), std=np.ones(3))
        {1.0: array([-1.,  1.]), 2.0: array([-1.,  1.]), 3.0: array([-1.,  1.])}

    """  # noqa: E501
    y_dict = y_dict.copy()
    if isinstance(mean, float):
        mean = mean * np.ones(len(y_dict))
    if isinstance(std, float):
        std = std * np.ones(len(y_dict))
    for i, _x in enumerate(y_dict.keys()):
        org_mean = y_dict[_x].mean()
        org_std = y_dict[_x].std()
        new_mean = org_mean if mean is None else mean[i]
        new_std = org_std if std is None else std[i]
        y_dict[_x] = (y_dict[_x] - org_mean) / org_std * new_std + new_mean
    return y_dict


def normalize_err_bar(x: np.ndarray, y: np.ndarray
                      ) -> tuple[np.ndarray, np.ndarray]:
    r"""Normalize :attr:`x` and :attr:`y` into range ``[0, 1]``.

    each :attr:`x` might correspond to multiple :attr:`y` values
    and therefore generate an error band on y-axis.
    The mean of :attr:`y` is normalized into ``[0, 1]``.

    Args:
        x (numpy.ndarray): The x array.
        y (numpy.ndarray): The y array.

    Returns:
        (numpy.ndarray, numpy.ndarray): The normalized x, y array.

    :Example:
        >>> import numpy as np
        >>> from alpsplot.utils import group_err_bar, normalize_err_bar
        >>>
        >>> x = np.array([1., 2., 3.] * 2)
        >>> x
        array([1., 2., 3., 1., 2., 3.])
        >>> y = np.arange(6.0)
        >>> y
        array([0., 1., 2., 3., 4., 5.])
        >>> normalize_err_bar(x, y)
        (array([0. , 0. , 0.5, 0.5, 1. , 1. ]), array([-1.5,  1.5, -1. ,  2. , -0.5,  2.5]))
    """  # noqa: E501
    y_dict = group_err_bar(normalize(x), y)
    y_mean = np.array([y_dict[_x].mean() for _x in y_dict.keys()])
    y_dict = adjust_err_bar(y_dict, normalize(y_mean))
    return flatten_err_bar(y_dict)


def avg_smooth_err_bar(x: np.ndarray, y: np.ndarray,
                       window: int = 3) -> tuple[np.ndarray, np.ndarray]:
    r"""Average smooth :attr:`x` and :attr:`y` using window size :attr:`window`.

    Each :attr:`x` might correspond to multiple :attr:`y` values
    and therefore generate an error band on y-axis.
    The mean of :attr:`y` is smoothed.

    Args:
        x (numpy.ndarray): The x array.
        y (numpy.ndarray): The y array.
        window (int): the :attr:`window` argument passed to
            :func:`alpsplot.utils.avg_smooth`. Defaults to ``3``.

    Returns:
        (numpy.ndarray, numpy.ndarray): The smoothed x, y array.

    :Example:
        >>> import numpy as np
        >>> from alpsplot.utils import group_err_bar, avg_smooth_err_bar
        >>>
        >>> x = np.array([1., 2., 3.] * 2)
        >>> x
        array([1., 2., 3., 1., 2., 3.])
        >>> y = np.arange(6.0)
        >>> y
        array([0., 1., 2., 3., 4., 5.])
        >>> avg_smooth_err_bar(x, y)
        (array([1., 1., 2., 2., 3., 3.]), array([0.33333333, 3.33333333, 1.        , 4.        , 1.66666667, 4.66666667]))
        >>> avg_smooth_err_bar(x, y, window=5)
        (array([1., 1., 2., 2., 3., 3.]), array([0.6, 3.6, 0.3, 3.3, 1.4, 4.4]))
    """  # noqa: E501
    y_dict = group_err_bar(x, y)
    y_mean = np.array([y_dict[_x].mean() for _x in y_dict.keys()])
    y_dict = adjust_err_bar(y_dict, avg_smooth(y_mean, window=window))
    return flatten_err_bar(y_dict)
