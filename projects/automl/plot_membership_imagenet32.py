#!/usr/bin/env python3

from alpsplot import Figure
from alpsplot.colormap import ting_color
import numpy as np

color_dict = {
    'Manual': ting_color['blue'],
    'NAS': ting_color['red'],
}


data = {
    'Manual': {
        'BiT': 0.521728515625,
        'DenseNet': 0.60791015625,
        'DLA': 0.593994140625,
        # 'MobileNet': ,
        'ResNet': 0.620380859375,
        'ResNext': 0.571044921875,
        'VGG': 0.620361328125,
        'WideResnet': 0.571044921875,
    },
    'NAS': {
        'AmoebaNet': 0.6205859375,
        'DARTS': 0.63916015625,
        'DrNAS': 0.631103515625,
        'ENAS': 0.6763916015625,
        'NASNet': 0.623291015625,
        'PC-DARTS': 0.65185546875,
        'PDARTS': 0.634033203125,
        'SGAS': 0.6357421875,
        'SNAS': 0.673828125,
        'Random': 0.604736328125,
    }
}


if __name__ == '__main__':
    x_labels = [''] + list(data['Manual'].keys()) \
        + [''] + list(data['NAS'].keys()) + ['']
    x_digits = np.arange(len(x_labels))[1:-1]
    x_data = {
        'Manual': x_digits[:len(data['Manual'].keys())],
        'NAS': x_digits[-len(data['NAS'].keys()):],
    }
    fig = Figure('membership_imagenet32')
    fig.set_axis_label('y', 'AUC')
    fig.set_axis_lim('x', labels=x_labels, rotation='vertical',
                     lim=[0, len(x_labels)-1], piece=len(x_labels)-1, margin=[1.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[0.5, 0.7], piece=5, margin=[0.0, 0.02],
                     _format='%.2f')
    for key in reversed(data.keys()):
        x = np.array(x_data[key])
        y = np.array(list(data[key].values()))
        fig.bar(x, y, color=color_dict[key],
                width=1, align='center', label=key)
    fig.set_legend(edgecolor=None)
    fig.ax.get_legend().remove()
    fig.save(folder_path='./result')
