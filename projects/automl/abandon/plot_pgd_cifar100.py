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

succ_rate = {
    'Manual': [0.379, 0.625, 0.515, 0.672, 0.355, 0.498, 0.233, 0.398],
    'NAS': [0.689, 0.579, 0.445, 0.655, 0.627, 0.606, 0.554, 0.708, 0.473, 0.804]
}
succ_iter = {
    'Manual': [9.176, 8.369, 8.787, 8.033, 9.241, 8.869, 9.445, 9.161],
    'NAS': [7.887, 8.563, 8.968, 8.038, 8.202, 8.232, 8.542, 7.871, 8.872, 7.186]
}


if __name__ == '__main__':
    fig = Figure('cifar100_pgd')
    fig.set_axis_label('x', 'Attack Success Rate (%)')
    fig.set_axis_label('y', 'Average Attack Iter')
    fig.set_axis_lim('x', lim=[20, 80], piece=3, margin=[4.0, 4.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[7, 9.5], piece=5, margin=[0.2, 0.2],
                     _format='%.1f')
    for key in reversed(succ_rate.keys()):
        x = np.array(succ_rate[key])*100
        y = np.array(succ_iter[key])
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
    fig.set_legend(edgecolor=None, loc='lower left')
    fig.ax.get_legend().remove()
    fig.save(folder_path='./result')
