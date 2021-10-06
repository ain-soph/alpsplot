#!/usr/bin/env python3

from alpsplot import Figure, ting_color
import numpy as np
import argparse

color_list = [ting_color['red_carrot'], ting_color['yellow'],
              ting_color['green'], ting_color['blue']]
mark_list = ['o', '^', 'd', 's', ]
x = [1, 2, 4, 8, 16]
y = {
    'DARTS': [2.341, 2.318, 2.089, 1.575, 1.311],
    'DARTS-i': [2.353, 2.336, 2.303, 2.272, 2.006],
    'DARTS-ii': [2.343, 2.317, 2.185, 1.972, 1.375],
    'DARTS-iii': [2.313, 2.315, 2.305, 2.305, 2.088],
}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--metric', choices=['loss', 'acc'], default='loss')
    args = parser.parse_args()
    metric: str = args.metric

    fig = Figure(f'mitigation_extraction_{metric}', figsize=(5, 2.5))
    fig.set_axis_label('x', 'Query Number (k)')
    fig.set_axis_label('y', 'Cross Entropy' if metric == 'loss'
                       else 'Thieved Model Acc (%)')
    fig.set_axis_lim('x', lim=[0, 16], piece=4, margin=[0.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[1, 2.5], piece=3, margin=[0.0, 0.0],
                     _format='%.1f')

    for i, (key, value) in enumerate(y.items()):
        x_list = x[:len(value)]
        y_list = np.array(value)
        fig.lineplot(x=x_list, y=y_list, color=color_list[i])
        fig.scatter(x=x_list, y=y_list, color=color_list[i],
                    marker=mark_list[i], label=key)
    fig.set_legend(edgecolor=None)
    fig.save(folder_path='./result')
