#!/usr/bin/env python3

from alpsplot import ting_color, Figure
import os

color_dict = {
    'Manual': ting_color['blue'],
    'NAS': ting_color['red'],
}
data = {
    'Manual': [2, 22, 119, 259, 299, 227, 63, 9],
    'NAS': [0, 0, 2, 14, 38, 137, 247, 311, 198, 53],
}


if __name__ == '__main__':
    for k, v in data.items():
        fig = Figure(os.path.splitext(os.path.basename(__file__).removeprefix('plot_'))[0]+'_'+k, figsize=(5, 3.75))
        fig.set_axis_label('x', 'Number of Successfully Attacked Models')
        fig.set_axis_label('y', 'Number of Inputs')
        fig.set_axis_lim('x', lim=[0, len(v)-1], piece=len(v)-1, margin=[1.0, 1.0],
                         _format='%d')
        fig.set_axis_lim('y', lim=[0, 350], piece=5, margin=[0.0, 0.0],
                         _format='%d')
        x = list(range(len(v)))
        y = v
        print(x, y)
        fig.bar(x, y, color=color_dict[k],
                width=1, align='center', label=k)
        fig.set_legend(edgecolor=None)
        fig.ax.get_legend().remove()
        fig.save(folder_path='./result')
