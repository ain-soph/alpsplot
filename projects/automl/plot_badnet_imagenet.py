#!/usr/bin/env python3

from alpsplot import ting_color, Figure
import numpy as np

color_dict = {
    'Manual': ting_color['blue'],
    'NAS': ting_color['red'],
}
mark_dict = {
    'Manual': ['o', '^', 'd', 's', 'p', '+', 'x'],
    'NAS': ['o', '^', 'd', 's', 'p', '+', 'v', 'x', '8', '2'],
}

model_acc = {
    'Manual': [51.517, 55.083, 50.383, 47.150, 53.200, 52.800, 52.283],
    'NAS': [55.383, 56.417, 55.050, 54.533, 54.750, 54.817, 55.617, 53.783, 57.050, 53.933]
}
succ_rate = {
    'Manual': [92.933, 95.400, 94.100, 92.467, 94.050, 90.500, 93.133],
    'NAS': [95.600, 98.600, 96.550, 93.767, 89.883, 95.650, 98.233, 95.367, 95.367, 99.383]
}
poison_acc = {
    'Manual': [43.400, 47.033, 43.833, 41.217, 44.467, 47.267, 44.083],
    'NAS': [48.333, 50.117, 45.067, 49.300, 50.067, 49.150, 49.100, 51.183, 50.017, 48.717]
}


if __name__ == '__main__':
    fig = Figure('badnet_imagenet')
    fig.set_axis_label('x', 'Attack Success Rate (%)')
    fig.set_axis_label('y', 'Clean Accuracy Drop (%)')
    fig.set_axis_lim('x', lim=[90, 100], piece=5, margin=[0.3, 0.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[2, 10], piece=4, margin=[0.1, 0.3],
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
