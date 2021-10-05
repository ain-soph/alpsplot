#!/usr/bin/env python3

from alpsplot import ting_color, Figure
import numpy as np

color_dict = {
    'Manual': ting_color['blue'],
    'NAS': ting_color['red'],
}
mark_dict = {
    'Manual': ['o', '^', 'd', 's', 'p', '+', 'v', 'x'],
    'NAS': ['o', '^', 'd', 's', 'p', '+', 'v', 'x', '8', '2'],
}

model_acc = {
    'Manual': [96.62, 96.73, 96.45, 95.53, 96.58, 96.73, 95.06, 96.75],
    'NAS': [96.92, 97.04, 96.87, 96.77, 97.00, 96.86, 97.07, 97.18, 97.15, 96.93]
}
succ_rate = {
    'Manual': [94.58, 93.88, 92.16, 85.98, 91.06, 92.08, 86.59, 87.43],
    'NAS': [91.43, 94.07, 92.53, 95.53, 93.84, 94.53, 93.42, 93.64, 91.43, 91.38]
}
poison_acc = {
    'Manual': [93.69, 93.81, 93.42, 91.92, 93.13, 93.98, 91.72, 93.51],
    'NAS': [94.04, 93.82, 94.01, 93.94, 94.11, 94.34, 94.31, 95.16, 94.80, 93.96]
}


if __name__ == '__main__':
    fig = Figure('badnet_cifar10')
    fig.set_axis_label('x', 'Attack Success Rate (%)')
    fig.set_axis_label('y', 'Clean Accuracy Drop (%)')
    fig.set_axis_lim('x', lim=[80, 100], piece=4, margin=[1.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[2, 4], piece=4, margin=[0.1, 0.1],
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
