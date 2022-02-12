#!/usr/bin/env python3

from alpsplot import Figure
from alpsplot.colormap import ting_color


if __name__ == '__main__':
    name = f'bar'
    fig = Figure(name, figsize=(5, 2.5))
    fig.set_axis_label('x', r'Trigger Size')
    fig.set_axis_label('y', 'ASR (%)')
    fig.set_axis_lim('x', lim=[2, 5], piece=3, margin=[0.5, 0.5],
                     _format='%d')
    fig.set_axis_lim('y', lim=[0, 100], piece=5, margin=[0.0, 5.0],
                     _format='%d')
    fig.set_title('')
    x = [2, 3, 4, 5]
    y = [20, 30, 40, 50]
    fig.bar(x=x, y=y, color=ting_color['yellow'], yerr=[10, 20, 30, 40], ecolor=ting_color['blue'], capsize=3)

    fig.save(folder_path='./result/', ext='.pdf')
