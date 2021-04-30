#!/usr/bin/env python3

from alpsplot import *
import numpy as np

color_dict = {
    'Manual': ting_color['blue'],
    'AutoML': ting_color['red'],
}
mark_dict = {
    'Manual': ['o', '^', '8', 's', 'p', '+', 'v', 'x', 'D'],
    'AutoML': ['o', '^', '8', 's', 'p', '+', 'v', 'x', 'D', '2', 'h', 'H'],
}

succ_rate = {
    'Manual': [0.64, 0.752, 0.84, 0.796, 0.827, 0.93, 0.698, 0.849, 0.914],
    'AutoML': [0.892, 0.946, 0.916, 0.867, 0.893, 0.932, 0.895, 0.821, 0.857, 0.85, 0.915, 0.817]
}
succ_iter = {
    'Manual': [6.044, 5.721, 5.428, 5.58, 5.51, 5.105, 5.844, 5.276, 5.041],
    'AutoML': [5.068, 4.865, 4.924, 5.284, 5.097, 4.87, 5.149, 5.413, 5.302, 5.365, 5.056, 5.41]
}


if __name__ == '__main__':
    fig = Figure('cifar10_pgd')
    fig.set_axis_label('x', 'Attack Success Rate (%)')
    fig.set_axis_label('y', 'Attack Success Iter')
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
    fig.save(folder_path='./result')
