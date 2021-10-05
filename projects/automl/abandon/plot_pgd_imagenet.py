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

succ_rate = {
    'Manual': [0.3893333333333333, 0.31066666666666665, 0.22266666666666668, 0.112, 0.46, 0.496, 0.32],
    'NAS': [0.388, 0.532, 0.274, 0.552, 0.44266666666666665, 0.4013333333333333, 0.4146666666666667, 0.532, 0.444, 0.49066666666666664]
}
succ_iter = {
    'Manual': [9.150666666666666, 9.349333333333334, 9.553333333333333, 9.809333333333333, 8.964, 8.82, 9.392],
    'NAS': [9.166, 8.721333333333334, 9.382, 8.529333333333334, 8.978666666666667, 9.092, 9.064, 8.63, 9.028, 8.770666666666667]
}


if __name__ == '__main__':
    fig = Figure('imagenet_pgd')
    fig.set_axis_label('x', 'Attack Success Rate (%)')
    fig.set_axis_label('y', 'Average Attack Iter')
    fig.set_axis_lim('x', lim=[10, 60], piece=5, margin=[2.0, 2.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[8, 10], piece=4, margin=[0.2, 0.2],
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
