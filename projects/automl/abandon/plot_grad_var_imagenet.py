#!/usr/bin/env python3

from alpsplot import ting_color, Figure
import numpy as np

color_dict = {
    'Manual': ting_color['blue'],
    'NAS': ting_color['red'],
}

data = {
    'Manual': {
        'BiT': 0.003524,
        'DenseNet': 0.003377,
        'DLA': 0.003520,
        'MobileNet': 0.004060,
        'ResNet': 0.003452,
        'ResNext': 0.003396,
        'WideResnet': 0.003368,
    },
    'NAS': {
        'AmoebaNet': 0.004287,
        'DARTS': 0.003748,
        'DrNAS': 0.004199,
        'ENAS': 0.003716,
        'NASNet': 0.004229,
        'PC-DARTS': 0.003395,
        'PDARTS': 0.004126,
        'ProxylessNAS': 0.003877,
        'SGAS': 0.003732,
        'SNAS': 0.003762,
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
    fig = Figure('grad_var_imagenet')
    fig.set_axis_label('y', 'Normalized Gradient Variance')
    fig.set_axis_lim('x', labels=x_labels, rotation='vertical',
                     lim=[0, len(x_labels)-1], piece=len(x_labels)-1, margin=[1.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[3.3, 4.3], piece=5, margin=[0.0, 0.0],
                     _format='%.1f')
    for key in reversed(data.keys()):
        x = np.array(x_data[key])
        y = np.array(list(data[key].values()))
        fig.bar(x, y*1000, color=color_dict[key],
                width=1, align='center', label=key)
    fig.set_legend(edgecolor=None)
    fig.ax.get_legend().remove()
    fig.save(folder_path='./result')
