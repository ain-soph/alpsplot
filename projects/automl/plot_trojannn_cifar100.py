#!/usr/bin/env python3

from alpsplot import Figure, ting_color
import numpy as np

color_dict = {
    'Manual': ting_color['blue'],
    'NAS': ting_color['red'],
}
mark_dict = {
    'Manual': ['o', '^', 'd', 's', 'p', '+', 'v', 'x', '8', '2'],
    'NAS': ['o', '^', 'd', 's', 'p', '+', 'v', 'x', '8', '2'],
}

model_acc = {
    'Manual': [80.63, 80.72, 78.02, 78.10, 80.41, 73.87, 80.95],
    'NAS': [78.37, 81.67, 80.41, 79.11, 78.84, 77.39, 81.00, 81.78, 79.92, 78.57]
}
succ_rate = {
    'Manual': [96.13, 96.99, 93.82, 95.54, 95.72, 94.78, 97.55],
    'NAS': [99.57, 99.99, 99.03, 99.54, 99.23, 99.67, 99.92, 99.44, 99.83, 95.56]
}
poison_acc = {
    'Manual': [71.44, 74.13, 72.64, 77.86, 72.59, 65.56, 71.65],
    'NAS': [72.92, 74.29, 74.96, 73.68, 73.39, 72.88, 73.12, 75.03, 78.02, 72.81]
}


if __name__ == '__main__':
    fig = Figure('trojannn_cifar100')
    fig.set_axis_label('x', 'Attack Success Rate (%)')
    fig.set_axis_label('y', 'Clean Accuracy Drop (%)')
    fig.set_axis_lim('x', lim=[92, 100], piece=4, margin=[0.1, 0.1],
                     _format='%d')
    fig.set_axis_lim('y', lim=[0, 12], piece=4, margin=[0.1, 0.1],
                     _format='%.1f')
    for key in reversed(succ_rate.keys()):
        x = np.array(succ_rate[key])
        y = np.array(model_acc[key]) - np.array(poison_acc[key])
        for i in range(len(x)):
            kwargs = {}
            if mark_dict[key][i] in ['P', 'x', '2', '+']:
                kwargs['facecolor'] = color_dict[key]
                kwargs['color'] = None
            else:
                kwargs['color'] = color_dict[key]
                kwargs['facecolor'] = 'none'
            fig.scatter(x=x[i], y=y[i], marker=mark_dict[key][i],
                        linewidth=1.5, s=64, **kwargs)
        fig.scatter([], [], color=color_dict[key], marker='s', label=key)
    fig.set_legend(edgecolor=None)
    fig.ax.get_legend().remove()
    fig.save(folder_path='./result')
