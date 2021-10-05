#!/usr/bin/env python3

from alpsplot import ting_color, Figure
import numpy as np

color_dict = {
    'Manual': ting_color['blue'],
    'NAS': ting_color['red'],
}


data = {
    'Manual': {
        'BiT': 0.5244140625,
        'DenseNet': 0.51171875,
        'DLA': 0.5185546875,
        # 'MobileNet': 0.5322265625,
        'ResNet': 0.5029296875,
        'ResNext': 0.50537109375,
        'VGG': 0.52392578125,
        'WideResnet': 0.513671875,
    },
    'NAS': {
        'AmoebaNet': 0.5798828125,
        'DARTS': 0.562060546875,
        'DrNAS': 0.59921875,
        'ENAS': 0.5767578125,
        'NASNet': 0.57119140625,
        'PC-DARTS': 0.574365234375,
        'PDARTS': 0.54404296875,
        'SGAS': 0.58603515625,
        'SNAS': 0.583544921875,
        'Random': 0.51044921875,
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
    fig = Figure('membership_cifar10')
    fig.set_axis_label('y', 'AUC')
    fig.set_axis_lim('x', labels=x_labels, rotation='vertical',
                     lim=[0, len(x_labels)-1], piece=len(x_labels)-1, margin=[1.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[0.5, 0.6], piece=5, margin=[0.0, 0.0],
                     _format='%.2f')
    for key in reversed(data.keys()):
        x = np.array(x_data[key])
        y = np.array(list(data[key].values()))
        fig.bar(x, y, color=color_dict[key],
                width=1, align='center', label=key)
    fig.set_legend(edgecolor=None)
    fig.save(folder_path='./result')
