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
    'Manual': [72.067, 73.567, 70.767, 67.133, 73.367, 62.333, 73.867],
    'NAS': [74.833, 76.567, 75.633, 74.033, 73.000, 74.70, 75.767, 76.80, 75.467, 72.20]
}
succ_rate = {
    'Manual': [91.033, 95.467, 96.033, 92.933, 95.200, 90.433, 94.567],
    'NAS': [97.20, 97.867, 98.267, 98.267, 98.467, 99.500, 99.300, 99.000, 98.233, 97.467]
}
poison_acc = {
    'Manual': [62.767, 67.033, 63.200, 61.833, 67.667, 53.700, 65.667],
    'NAS': [68.30, 69.40, 66.267, 66.267, 67.333, 68.533, 69.333, 68.833, 68.500, 63.600]
}


if __name__ == '__main__':
    fig = Figure('trojannn_imagenet32')
    fig.set_axis_label('x', 'Attack Success Rate (%)')
    fig.set_axis_label('y', 'Clean Accuracy Drop (%)')
    fig.set_axis_lim('x', lim=[90, 100], piece=5, margin=[0.0, 0.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[4, 10], piece=3, margin=[0.0, 0.00],
                     _format='%d')
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
