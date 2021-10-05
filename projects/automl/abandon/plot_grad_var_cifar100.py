#!/usr/bin/env python3

from alpsplot import ting_color, Figure
import numpy as np

color_dict = {
    'Manual': ting_color['blue'],
    'NAS': ting_color['red'],
}

data = {
    'Manual': {
        'BiT': 0.001516,
        'DenseNet': 0.001477,
        'DLA': 0.001612,
        'MobileNet': 0.001608,
        'ResNet': 0.001796,
        'ResNext': 0.001451,
        'VGG': 0.001622,
        'WideResnet': 0.001659,
    },
    'NAS': {
        'AmoebaNet': 0.001750,
        'DARTS': 0.001379,
        'DrNAS': 0.001459,
        'ENAS': 0.001721,
        'NASNet': 0.001667,
        'PC-DARTS': 0.001788,
        'PDARTS': 0.001508,
        'ProxylessNAS': 0.001615,
        'SGAS': 0.001457,
        'SNAS': 0.001546,
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
    fig = Figure('grad_var_cifar100')
    fig.set_axis_label('y', 'Normalized Gradient Variance')
    fig.set_axis_lim('x', labels=x_labels, rotation='vertical',
                     lim=[0, len(x_labels)-1], piece=len(x_labels)-1, margin=[1.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[1.3, 1.8], piece=5, margin=[0.0, 0.0],
                     _format='%.1f')
    for key in reversed(data.keys()):
        x = np.array(x_data[key])
        y = np.array(list(data[key].values()))
        fig.bar(x, y*1000, color=color_dict[key],
                width=1, align='center', label=key)
    fig.set_legend(edgecolor=None)
    fig.ax.get_legend().remove()
    fig.save(folder_path='./result')
