#!/usr/bin/env python3

from alpsplot import ting_color, Figure
import numpy as np

color_dict = {
    'Manual': ting_color['blue'],
    'NAS': ting_color['red'],
}


data = {
    'Manual': {
        'BiT': 0.5107421875,
        'DenseNet': 0.540478515625,
        'DLA': 0.527490234375,
        # 'MobileNet': ,
        'ResNet': 0.530224609375,
        'ResNext': 0.54345703125,
        # 'VGG': ,
        'WideResnet': 0.556787109375,
    },
    'NAS': {
        'AmoebaNet': 0.63671875,
        'DARTS': 0.63603515625,
        'DrNAS': 0.59130859375,
        'ENAS': 0.66865234375,
        'NASNet': 0.61376953125,
        'PC-DARTS': 0.7109375,
        'PDARTS': 0.6166015625,
        'SGAS': 0.60966796875,
        'SNAS': 0.62646484375,
        'Random': 0.54853515625,
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
    fig = Figure('membership_imagenet')
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
