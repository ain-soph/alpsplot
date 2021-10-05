#!/usr/bin/env python3

from alpsplot import ting_color, Figure
import numpy as np

color_dict = {
    'Manual': ting_color['blue'],
    'NAS': ting_color['red'],
}


data = {
    'Manual': {
        'BiT': 0.524169921875,
        'DenseNet': 0.540478515625,
        'DLA': 0.5107421875,
        # 'MobileNet': ,
        'ResNet': 0.556787109375,
        'ResNext': 0.527490234375,
        'VGG': 0.530224609375,
        'WideResnet': 0.54345703125,
    },
    'NAS': {
        'AmoebaNet': 0.70244140625,
        'DARTS': 0.65439453125,
        'DrNAS': 0.58427734375,
        'ENAS': 0.66806640625,
        'NASNet': 0.61318359375,
        'PC-DARTS': 0.622900390625,
        'PDARTS': 0.6251953125,
        'SGAS': 0.6244140625,
        'SNAS': 0.62734375,
        'Random': 0.56455078125,
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
    fig = Figure('membership_cifar100')
    fig.set_axis_label('y', 'AUC')
    fig.set_axis_lim('x', labels=x_labels, rotation='vertical',
                     lim=[0, len(x_labels)-1], piece=len(x_labels)-1, margin=[1.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[0.5, 0.7], piece=4, margin=[0.0, 0.01],
                     _format='%.2f')
    for key in reversed(data.keys()):
        x = np.array(x_data[key])
        y = np.array(list(data[key].values()))
        fig.bar(x, y, color=color_dict[key],
                width=1, align='center', label=key)
    fig.set_legend(edgecolor=None)
    fig.save(folder_path='./result')
