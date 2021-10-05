#!/usr/bin/env python3

from alpsplot import ting_color, Figure
import numpy as np

color_dict = {
    'Manual': ting_color['blue'],
    'NAS': ting_color['red'],
}

data_before = {
    'Manual': {
        'BiT': 9258.7197265625,
        'DenseNet': 3408.630810546875,
        'DLA': 25.4749454498291,
        'ResNet': 7243.9482421875,
        'ResNext': 2194.926220703125,
        'VGG': 1522.9010009765625,
        'WideResnet': 12016.6359375,
    },
    'NAS': {
        'AmoebaNet': 44.140673828125,
        'DARTS': 38.237647247314456,
        'DrNAS': 36.8227180480957,
        'ENAS': 45.32197723388672,
        'NASNet': 55.45033416748047,
        'PC-DARTS': 37.88999633789062,
        'PDARTS': 37.44239959716797,
        'SGAS': 37.185237884521484,
        'SNAS': 43.3796142578125,
        # 'Random': 44.29513320922852,
    }
}

data_after = {
    'Manual': {
        'BiT': 4388.4134765625,
        'DenseNet': 2901.10009765625,
        'DLA': 4945.35,
        'ResNet': 4109.7419921875,
        'ResNext': 3920.418798828125,
        'VGG': 3075.23828125,
        'WideResnet': 7701.83427734375,
    },
    'NAS': {
        'AmoebaNet': 1577.0595703125,
        'DARTS': 1758.313134765625,
        'DrNAS': 1426.05947265625,
        'ENAS': 1792.3064453125,
        'NASNet': 1561.93515625,
        'PC-DARTS': 1590.1905029296875,
        'PDARTS': 1543.452734375,
        'SGAS': 1476.8668212890625,
        'SNAS': 1622.675146484375,
        # 'Random': 1536.04921875,
    }
}

if __name__ == '__main__':
    x_labels = [''] + list(data_before['Manual'].keys()) \
        + [''] + list(data_before['NAS'].keys()) + ['']
    x_digits = np.arange(len(x_labels))[1:-1]
    x_data = {
        'Manual': x_digits[:len(data_before['Manual'].keys())],
        'NAS': x_digits[-len(data_before['NAS'].keys()):],
    }
    fig = Figure('grad_var_cifar10_1', figsize=(5, 2.5))
    fig.set_axis_label('y', 'Before Training')
    fig.set_axis_lim('x', labels=x_labels, rotation='vertical',
                     lim=[0, len(x_labels)-1], piece=len(x_labels)-1, margin=[1.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[0, 4], piece=4, margin=[0.0, 0.2],
                     _format='%d')
    for key in reversed(data_before.keys()):
        x = np.array(x_data[key])
        y = np.log10(np.array(list(data_before[key].values())))
        fig.bar(x, y, color=color_dict[key],
                width=1, align='center', label=key)
    fig.set_legend(edgecolor=None)
    fig.ax.get_legend().remove()
    fig.save(folder_path='./result')

    fig2 = Figure('grad_var_cifar10_2', figsize=(5, 2.5))
    fig2.set_axis_label('y', 'After Training')
    fig2.set_axis_lim('x', labels=x_labels, rotation='vertical',
                      lim=[0, len(x_labels)-1], piece=len(x_labels)-1, margin=[1.0, 1.0],
                      _format='%d')
    fig2.set_axis_lim('y', lim=[0, 4], piece=4, margin=[0.0, 0.2],
                      _format='%d')
    fig2.ax.invert_yaxis()
    fig2.ax.xaxis.tick_top()
    for key in reversed(data_after.keys()):
        x = np.array(x_data[key])
        y = np.log10(np.array(list(data_after[key].values())))
        fig2.bar(x, y, edgecolor=color_dict[key], color='white',
                 width=0.85, align='center', label=key)
    fig2.set_legend(edgecolor=None)
    fig2.ax.get_legend().remove()
    fig2.save(folder_path='./result')
