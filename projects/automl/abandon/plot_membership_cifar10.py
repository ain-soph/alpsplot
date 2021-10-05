#!/usr/bin/env python3

from alpsplot import ting_color, Figure
import numpy as np

color_dict = {
    'Manual': ting_color['blue'],
    'NAS': ting_color['red'],
}


data = {
    'Manual': {
        'BiT': 0.49206349206349204,
        'DenseNet': 0.5357142857142857,
        'DLA': 0.5426356589147288,
        'MobileNet': 0.5042016806722689,
        'ResNet': 0.4423076923076923,
        'ResNext': 0.6447368421052632,
        'VGG': 0.5942028985507247,
        'WideResnet': 0.6447368421052632,
    },
    'NAS': {
        'AmoebaNet': 0.6936416184971099,
        'DARTS': 0.679245283018868,
        'DrNAS': 0.7,
        'ENAS': 0.7023809523809524,
        'NASNet': 0.6951219512195121,
        'PC-DARTS': 0.6540880503144655,
        'PDARTS': 0.6486486486486486,
        'ProxylessNAS': 0.6,
        'SGAS': 0.60431654676259,
        'SNAS': 0.5409836065573771,
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
    fig = Figure('cifar10_membership')
    fig.set_axis_label('y', 'F1 Score')
    fig.set_axis_lim('x', labels=x_labels, rotation='vertical',
                     lim=[0, len(x_labels)-1], piece=len(x_labels)-1, margin=[1.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[0.4, 0.7], piece=3, margin=[0.0, 0.0],
                     _format='%.1f')
    for key in reversed(data.keys()):
        x = np.array(x_data[key])
        y = np.array(list(data[key].values()))
        fig.bar(x, y, color=color_dict[key],
                width=1, align='center', label=key)
    fig.set_legend(edgecolor=None)
    fig.save(folder_path='./result')
