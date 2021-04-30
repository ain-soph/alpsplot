#!/usr/bin/env python3

from alpsplot import *
import numpy as np

color_dict = {
    'Manual': ting_color['blue'],
    'AutoML': ting_color['red'],
}
mark_dict = {
    'Manual': ['o', '^', '8', 's', 'p', 'P', '*', 'X', 'D'],
    'AutoML': ['o', '^', '8', 's', 'p', 'P', '*', 'X', 'D', '2', 'P', 'H'],
}

model_acc = {
    'Manual': [95.06, 96.58, 96.73, 96.75, 96.73, 96.34, 96.45, 95.53, 94.26],
    'AutoML': [96.92, 96.77, 97.00, 96.93, 97.04, 95.58, 97.07, 96.86, 96.87, 97.15, 97.18, 97.15]
}
succ_rate = {
    'Manual': [86.59, 91.06, 93.88, 87.43, 92.08, 85.26, 92.16, 85.98, 79.83],
    'AutoML': [91.43, 95.53, 93.84, 91.38, 94.07, 91.01, 93.42, 94.53, 92.53, 91.43, 93.64, 92.64]
}
poison_acc = {
    'Manual': [91.72, 93.13, 93.81, 93.51, 93.98, 93.78, 93.42, 91.92, 91.10],
    'AutoML': [94.04, 93.94, 94.11, 93.96, 93.82, 92.32, 94.31, 94.34, 94.01, 94.80, 95.16, 94.31]
}


if __name__ == '__main__':
    fig = Figure('cifar10_badnet')
    fig.set_axis_label('x', 'Attack Success Rate (%)')
    fig.set_axis_label('y', 'Model Accuracy Drop (%)')
    fig.set_axis_lim('x', lim=[80, 100], piece=4, margin=[1.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[2, 4], piece=4, margin=[0.1, 0.1],
                     _format='%d')
    for key in reversed(succ_rate.keys()):
        x = np.array(succ_rate[key])
        y = np.array(model_acc[key]) - np.array(poison_acc[key])
        for i in range(len(x)):
            fig.scatter(x=x[i], y=y[i], color=color_dict[key],
                        marker=mark_dict[key][i])
        fig.scatter([], [], color=color_dict[key], marker='s', label=key)
    fig.set_legend(edgecolor=None)
    fig.save(folder_path='./result')
