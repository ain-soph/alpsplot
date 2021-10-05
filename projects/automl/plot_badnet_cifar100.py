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
    'Manual': [80.63, 80.72, 78.02, 75.87, 78.10, 80.41, 73.87, 80.95],
    'NAS': [78.37, 81.67, 80.41, 79.11, 78.84, 77.39, 81.00, 82.80, 81.78, 79.92]
}
succ_rate = {
    'Manual': [92.52, 86.08, 85.75, 91.29, 91.88, 75.37, 85.65, 87.54],
    'NAS': [91.36, 74.65, 86.41, 87.27, 90.27, 86.16, 86.60, 91.22, 90.08, 89.58]
}
poison_acc = {
    'Manual': [73.34, 75.09, 73.08, 69.22, 78.40, 76.45, 67.01, 76.36],
    'NAS': [72.49, 75.11, 74.36, 73.62, 72.77, 72.07, 75.26, 83.84, 75.48, 78.29]
}


if __name__ == '__main__':
    fig = Figure('badnet_cifar100')
    fig.set_axis_label('x', 'Attack Success Rate (%)')
    fig.set_axis_label('y', 'Clean Accuracy Drop (%)')
    fig.set_axis_lim('x', lim=[75, 95], piece=4, margin=[1.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[0, 8], piece=4, margin=[0.5, 0.0],
                     _format='%.1f')
    for key in reversed(succ_rate.keys()):
        x = np.array(succ_rate[key])
        y: np.ndarray = np.array(model_acc[key]) - np.array(poison_acc[key])
        y = y.clip(min=0.0)
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
