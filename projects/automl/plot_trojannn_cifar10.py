#!/usr/bin/env python3

from alpsplot import Figure, ting_color
import numpy as np

color_dict = {
    'Manual': ting_color['blue'],
    'NAS': ting_color['red'],
}
mark_dict = {
    'Manual': ['o', '^', 'd', 's', 'p', '+', 'v'],
    'NAS': ['o', '^', 'd', 's', 'p', '+', 'v', 'x', '8', '2'],
}

model_acc = {
    'Manual': [96.62, 96.73, 96.45, 96.58, 96.73, 95.06, 96.75],
    'NAS': [96.92, 97.04, 96.87, 96.77, 97.00, 96.86, 97.07, 97.15, 96.93, 96.74]
}
succ_rate = {
    'Manual': [94.96, 94.47, 94.41, 97.64, 95.61, 94.65, 98.68],
    'NAS': [99.74, 99.94, 99.64, 98.79, 99.30, 99.98, 99.58, 99.90, 99.92, 99.60]
}
poison_acc = {
    'Manual': [92.08, 93.83, 93.17, 92.94, 93.31, 92.25, 92.99],
    'NAS': [94.16, 94.34, 94.25, 93.84, 94.71, 94.42, 94.25, 94.34, 94.07, 91.24]
}


if __name__ == '__main__':
    fig = Figure('trojannn_cifar10')
    fig.set_axis_label('x', 'Attack Success Rate (%)')
    fig.set_axis_label('y', 'Clean Accuracy Drop (%)')
    fig.set_axis_lim('x', lim=[94, 100], piece=3, margin=[0.1, 0.1],
                     _format='%d')
    fig.set_axis_lim('y', lim=[2, 6], piece=4, margin=[0.02, 0.02],
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
