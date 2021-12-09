#!/usr/bin/env python3

from alpsplot.figure import Figure
import numpy as np
import pytest


def test_style():
    fig = Figure('test_style')
    fig.set_title(r'test $\alpha 45$ mathematics')
    fig.set_axis_label('x', r'x axis $\beta$')
    fig.set_axis_lim('x')
    fig.save()


def test_save():
    fig = Figure('test_set_title',
                 folder_path='./output/abc/')
    fig.save()
    fig.save(path='./output/abc/c.pdf')
    fig.save(filename='c.svg')
    fig.save(ext='.png')
    fig.save(ext='jpg')


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
    fig.set_axis_lim('x', lim=(2.0, 3.0),
                     piece=2, _format='%.2f')
    fig.set_axis_lim('y', labels=['l1', 'l2', 'l3'],
                     lim=(0.0, 4.0),
                     margin=(2.0, 2.0),
                     piece=2, _format='%d')
    fig.save()


def test_set_legend():
    fig = Figure('test_set_legend')
    x = np.arange(10, step=0.5)
    y = np.arange(10, step=0.5)
    fig.lineplot(x, y, color='red', label='lineplot')
    fig.scatter(x, y, label='scatter')
    fig.set_legend()
    fig.save()


def test_lineplot():
    fig = Figure('test_lineplot')
    x = np.arange(10, step=0.5)
    y = np.arange(10, step=0.5)
    fig.lineplot(x, y, color='red', label='plain')

    x = np.concatenate((x, x, x))
    noise = np.random.randn(20)
    y_mean = y / 2
    y_err = np.concatenate((y_mean-noise, y_mean, y_mean+noise))
    fig.lineplot(x, y_err, color='green', label='error band')

    x = np.concatenate((x, x, x))
    noise = np.random.randn(20)
    y_mean = y / 2 + 4
    y_err = np.concatenate((y_mean-noise, y_mean, y_mean+noise))
    fig.lineplot(x, y_err, color='blue', label='error bar',
                 err_style='bars')

    with pytest.raises(ValueError):
        fig.lineplot(x, y_err, err_style='wrong')

    fig.set_legend()
    fig.save()


def test_curve_legend():
    fig = Figure('test_curve_legend')
    fig.curve_legend(color='red', marker='D',
                     label='curve_legend')
    fig.set_legend()
    fig.save()


def test_scatter():
    fig = Figure('test_scatter')
    x = np.arange(10, step=0.5)
    y = np.arange(10, step=0.5)
    fig.scatter(x, y, color='red', label='plain')
    fig.scatter(x, y/2, color='green', label='curve_legend',
                marker='s', curve_legend=True)
    fig.set_legend()
    fig.save()


def test_bar():
    fig = Figure('test_bar')
    x = np.arange(10, step=2)
    y = np.arange(10, step=2)
    fig.bar(x, y, width=1, color='red', label='bar1')
    fig.bar(x+1, y+1, width=1, color='green', label='bar2')
    fig.set_legend()
    fig.save()

# def test_bar3d():
#     _fig = plt.figure(figsize=(5, 2.5))
#     _ax = _fig.add_subplot(111, projection='3d')
#     fig = Figure('test_bar', fig=_fig, ax=_ax)

#     _x = np.arange(0, 1, 0.1)
#     _y = np.arange(0, 1, 0.1)
#     _xx, _yy = np.meshgrid(_x, _y)
#     _xx: np.ndarray
#     _yy: np.ndarray
#     x, y = _xx.ravel(), _yy.ravel()

#     z = (x + y) / 2
#     fig.bar3d(x, y, z, size=0.1, label='bar3d')
#     fig.save()


def test_hist():
    fig = Figure('test_hist')
    x = np.random.randn(1000)
    fig.hist(x, range=(-2, 2), bins=8,
             facecolor='red', label='hist')
    fig.set_legend()
    fig.save()


def test_autolabel():
    fig = Figure('test_autolabel')
    x = np.arange(10, step=2)
    y = np.arange(10, step=2)
    rects1 = fig.bar(x, y, width=1, color='red', label='bar1')
    rects2 = fig.bar(x+1, y+1, width=1,
                     color='green', label='bar2')
    fig.autolabel(rects1)
    fig.autolabel(rects2, above=False)
    fig.set_legend()
    fig.save()
