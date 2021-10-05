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
    'Manual': [0.637, 0.84, 0.698, 0.849, 0.752, 0.827, 0.64, 0.796],
    'NAS': [0.892, 0.893, 0.857, 0.946, 0.916, 0.821, 0.895, 0.915, 0.85, 0.867]
}
succ_iter = {
    'Manual': [6.002, 5.428, 5.844, 5.276, 5.721, 5.51, 6.044, 5.58],
    'NAS': [5.068, 5.097, 5.302, 4.865, 4.924, 5.413, 5.149, 5.056, 5.365, 5.284]
}


if __name__ == '__main__':
    fig = Figure('cifar10_pgd')
    fig.set_axis_label('x', 'Attack Success Rate (%)')
    fig.set_axis_label('y', 'Average Attack Iter')
    fig.set_axis_lim('x', lim=[60, 100], piece=4, margin=[1.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[4.5, 6], piece=3, margin=[0.1, 0.1],
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
