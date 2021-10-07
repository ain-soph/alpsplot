#!/usr/bin/env python3

from alpsplot.utils import *
import numpy as np


def test_group_err_bar():
    x = np.array([1., 2., 3.] * 2)
    y = np.arange(6.0)
    test_dict = group_err_bar(x, y)
    truth_dict = {1.0: [0., 3.], 2.0: [1., 4.], 3.0: [2., 5.]}
    for key in truth_dict.keys():
        assert np.allclose(test_dict[key], truth_dict[key])


def test_flatten_err_bar():
    x = np.array([1., 2., 3.] * 2)
    y = np.arange(6.0)
    flatten_x, flatten_y = flatten_err_bar(group_err_bar(x, y))
    assert np.allclose(flatten_x, [1., 1., 2., 2., 3., 3.])
    assert np.allclose(flatten_y, [0., 3., 1., 4., 2., 5.])


def test_adjust_err_bar():
    x = np.array([1., 2., 3.] * 2)
    y = np.arange(6.0)
    y_dict = group_err_bar(x, y)
    result1 = adjust_err_bar(y_dict)
    result2 = adjust_err_bar(y_dict, mean=0.3, std=0.4)
    result3 = adjust_err_bar(y_dict, mean=np.zeros(3), std=np.ones(3))
    truth1 = {1.0: [0., 3.], 2.0: [1., 4.], 3.0: [2., 5.]}
    truth2 = {1.0: [-0.1, 0.7], 2.0: [-0.1, 0.7], 3.0: [-0.1, 0.7]}
    truth3 = {1.0: [-1., 1.], 2.0: [-1., 1.], 3.0: [-1., 1.]}
    for key in result1.keys():
        assert np.allclose(result1[key], truth1[key])
        assert np.allclose(result2[key], truth2[key])
        assert np.allclose(result3[key], truth3[key])


def test_normalize_err_bar():
    x = np.array([1., 2., 3.] * 2)
    y = np.arange(6.0)
    new_x, new_y = normalize_err_bar(x, y)
    assert np.allclose(new_x, [0., 0., 0.5, 0.5, 1., 1.])
    assert np.allclose(new_y, [-1.5, 1.5, -1., 2., -0.5, 2.5])


def test_avg_smooth_err_bar():
    x = np.array([1., 2., 3.] * 2)
    y = np.arange(6.0)
    x1, y1 = avg_smooth_err_bar(x, y)
    x2, y2 = avg_smooth_err_bar(x, y, window=5)
    assert np.allclose(x1, [1., 1., 2., 2., 3., 3.])
    assert np.allclose(y1, [1 / 3, 10 / 3, 1., 4., 5 / 3, 14 / 3])
    assert np.allclose(x2, [1., 1., 2., 2., 3., 3.])
    assert np.allclose(y2, [0.6, 3.6, 0.3, 3.3, 1.4, 4.4])
