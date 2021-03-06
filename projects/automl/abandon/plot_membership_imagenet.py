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
        'BiT': 0.7412587412587414,
        'DenseNet': 0.626865671641791,
        'DLA': 0.7777777777777778,
        'MobileNet': 0.6356589147286822,
        'ResNet': 0.7012987012987012,
        'ResNext': 0.7785234899328859,
        'WideResnet': 0.7222222222222223,
    },
    'NAS': {
        'AmoebaNet': 0.7792207792207793,
        'DARTS': 0.8235294117647058,
        'DrNAS': 0.6412213740458016,
        'ENAS': 0.8243243243243242,
        'NASNet': 0.8027210884353742,
        'PC-DARTS': 0.8299319727891157,
        'PDARTS': 0.779874213836478,
        'ProxylessNAS': 0.6571428571428571,
        'SGAS': 0.759493670886076,
        'SNAS': 0.8025477707006369,
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
    fig = Figure('imagenet_membership')
    fig.set_axis_label('y', 'F1 Score')
    fig.set_axis_lim('x', labels=x_labels, rotation='vertical',
                     lim=[0, len(x_labels)-1], piece=len(x_labels)-1, margin=[1.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[0.6, 0.85], piece=5, margin=[0.0, 0.0],
                     _format='%.2f')
    for key in reversed(data.keys()):
        x = np.array(x_data[key])
        y = np.array(list(data[key].values()))
        fig.bar(x, y, color=color_dict[key],
                width=1, align='center', label=key)
    fig.set_legend(edgecolor=None)
    fig.ax.get_legend().remove()
    fig.save(folder_path='./result')
