#!/usr/bin/env python3

from alpsplot import ting_color, Figure
import numpy as np

color_dict = {
    'Manual': ting_color['blue'],
    'NAS': ting_color['red'],
}


data = {
    'Manual': {
        'BiT': 0.670886075949367,
        'DenseNet': 0.7000000000000001,
        'DLA': 0.6323529411764705,
        'MobileNet': 0.5671641791044776,
        'ResNet': 0.6938775510204082,
        'ResNext': 0.637037037037037,
        'VGG': 0.6805555555555556,
        'WideResnet': 0.7044025157232703,
    },
    'NAS': {
        'AmoebaNet': 0.7191011235955056,
        'DARTS': 0.7455621301775147,
        'DrNAS': 0.7169811320754715,
        'ENAS': 0.7515151515151515,
        'NASNet': 0.7425149700598802,
        'PC-DARTS': 0.7317073170731707,
        'PDARTS': 0.7349397590361445,
        'ProxylessNAS': 0.7142857142857143,
        'SGAS': 0.7305389221556886,
        'SNAS': 0.7200000000000001,
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
    fig = Figure('cifar100_membership')
    fig.set_axis_label('y', 'F1 Score')
    fig.set_axis_lim('x', labels=x_labels, rotation='vertical',
                     lim=[0, len(x_labels)-1], piece=len(x_labels)-1, margin=[1.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[0.55, 0.75], piece=4, margin=[0.0, 0.0],
                     _format='%.2f')
    for key in reversed(data.keys()):
        x = np.array(x_data[key])
        y = np.array(list(data[key].values()))
        fig.bar(x, y, color=color_dict[key],
                width=1, align='center', label=key)
    fig.set_legend(edgecolor=None)
    fig.save(folder_path='./result')
