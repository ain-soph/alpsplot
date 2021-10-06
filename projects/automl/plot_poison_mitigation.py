#!/usr/bin/env python3

from alpsplot import Figure, ting_color
import numpy as np

color_list = [ting_color['red_carrot'], ting_color['yellow'],
              ting_color['green'], ting_color['blue']]
mark_list = ['o', '^', 'd', 's', ]
x = [0, 2.5, 5, 10, 20, 30, 40]
y = {
    'DARTS': [93.76, 92.47, 92.64, 90.67, 87.59, 81.50, 77.56],
    'DARTS-i': [66.00, 63.30, 60.23, 56.33, 46.11, 39.86, 39.10],
    'DARTS-ii': [93.25, 92.61, 91.06, 88.74, 86.04, 80.61, 75.29],
    'DARTS-iii': [52.02, 51.63, 50.00, 46.22, 40.87, 34.51, 27.50],
}

if __name__ == '__main__':
    fig = Figure('mitigation_poison', figsize=(5, 2.5))
    fig.set_axis_label('x', 'Poisoning Percentage (%)')
    fig.set_axis_label('y', 'Clean Accuracy Drop (%)')
    fig.set_axis_lim('x', lim=[0, 40], piece=4, margin=[1.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[0, 40], piece=4, margin=[1.0, 1.0],
                     _format='%d')

    for i, (key, value) in enumerate(y.items()):
        value = np.array(value)
        x_list = x[:len(value)]
        y_list = value[0] - value
        fig.lineplot(x=x_list, y=y_list, color=color_list[i])
        fig.scatter(x=x_list, y=y_list, color=color_list[i],
                    marker=mark_list[i], label=key)
    fig.set_legend(edgecolor=None)
    fig.save(folder_path='./result')
