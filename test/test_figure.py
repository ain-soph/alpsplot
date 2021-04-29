#!/usr/bin/env python3

from alpsplot.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import shutil


def test_save():
    fig = Figure('test_set_title')
    fig.save()
    fig.save(path='./output/abc/c.pdf')
    shutil.rmtree('./output/abc')


def test_set_title():
    fig = Figure('test_set_title')
    fig.set_title()
    fig.set_title('test2')
    fig.save()


def test_set_axis_label():
    fig = Figure('test_set_axis_label')
    fig.set_axis_label('x', r'x - $\alpha$')
    fig.set_axis_label('y', r'y - $\beta$')
    fig.save()


def test_set_axis_lim():
    fig = Figure('test_set_axis_lim')
    fig.set_axis_lim('x')
    fig.set_axis_lim('y', _format='integer')
    fig.save()


def test_plot():
    fig = Figure('test_plot')
    x = np.arange(0, 1, 0.1)
    fig.plot(x, x, label='plot')
    fig.save()


def test_scatter():
    fig = Figure('test_scatter')
    x = np.arange(0, 1, 0.1)
    fig.scatter(x, x, label='scatter')
    fig.save()


def test_bar():
    fig = Figure('test_bar')
    x = np.arange(0, 1, 0.1)
    fig.bar(x, x, width=0.1, label='bar')
    fig.set_legend()
    fig.save()


def test_bar3d():
    _fig = plt.figure(figsize=(5, 2.5))
    _ax = _fig.add_subplot(111, projection='3d')
    fig = Figure('test_bar', fig=_fig, ax=_ax)

    _x = np.arange(0, 1, 0.1)
    _y = np.arange(0, 1, 0.1)
    _xx, _yy = np.meshgrid(_x, _y)
    _xx: np.ndarray
    _yy: np.ndarray
    x, y = _xx.ravel(), _yy.ravel()

    z = (x + y) / 2
    fig.bar3d(x, y, z, size=0.1, label='bar3d')
    fig.save()


def test_set_legend():
    fig = Figure('test_set_legend')
    x = np.arange(0, 1, 0.1)
    fig.plot(x, x, label='plot')
    fig.scatter(x, x, label='scatter')
    fig.set_legend()
    fig.save()


def test_hist():
    fig = Figure('test_hist')
    x = np.arange(0, 1, 0.01)
    fig.hist(x, 5)
    fig.save()


def test_autolabel():
    fig = Figure('test_hist')
    x = np.arange(0, 1, 0.1)
    rects = fig.bar(x, x, width=0.1, label='bar')
    fig.autolabel(rects)
    fig.autolabel(rects, above=False)
    fig.set_legend()
    fig.save()
