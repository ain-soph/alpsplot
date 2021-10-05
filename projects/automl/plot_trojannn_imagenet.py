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
    'Manual': [99.96, 98.53, 99.71, 99.92, 98.07, 99.92, 99.45],
    'NAS': [99.57, 98.21, 99.03, 99.54, 99.23, 99.67, 99.92, 99.44, 99.83, 99.52]
}
poison_acc = {
    'Manual': [74.03, 75.20, 72.07, 78.71, 76.34, 66.76, 76.45],
    'NAS': [72.92, 75.41, 74.96, 73.68, 73.39, 72.88, 73.12, 75.03, 78.02, 73.14]
}


if __name__ == '__main__':
    fig = Figure('trojannn_imagenet')
    fig.set_axis_label('x', 'Attack Success Rate (%)')
    fig.set_axis_label('y', 'Clean Accuracy Drop (%)')
    fig.set_axis_lim('x', lim=[94, 100], piece=3, margin=[0.1, 0.1],
                     _format='%d')
    fig.set_axis_lim('y', lim=[2, 3.5], piece=3, margin=[0.02, 0.02],
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
