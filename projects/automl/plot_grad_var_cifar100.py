#!/usr/bin/env python3

from alpsplot import ting_color, Figure
import numpy as np

color_dict = {
    'Manual': ting_color['blue'],
    'NAS': ting_color['red'],
}

data_before = {
    'Manual': {
        'BiT': 9349.903125,
        'DenseNet': 4220.412890625,
        'DLA': 36.87966079711914,
        'ResNet': 7653.75341796875,
        'ResNext': 2732.621533203125,
        'VGG': 1403.14736328125,
        'WideResnet': 11851.6431640625,
    },
    'NAS': {
        'AmoebaNet': 54.30771408081055,
        'DARTS': 46.83208389282227,
        'DrNAS': 45.8362060546875,
        'ENAS': 54.65050277709961,
        'NASNet': 65.664306640625,
        'PC-DARTS': 47.06336517333985,
        'PDARTS': 46.26331100463867,
        'SGAS': 46.0373031616211,
        'SNAS': 52.73821182250977,
        # 'Random': 54.38636856079101,
    }
}

data_after = {
    'Manual': {
        'BiT': 12783.839453125,
        'DenseNet': 7234.1712890625,
        'DLA': 11110.340234375,
        'ResNet': 9416.2421875,
        'ResNext': 8598.9416015625,
        'VGG': 7892.79521484375,
        'WideResnet': 23642.093359375,
    },
    'NAS': {
        'AmoebaNet': 4753.26904296875,
        'DARTS': 5003.597265625,
        'DrNAS': 4782.4583984375,
        'ENAS': 5392.33564453125,
        'NASNet': 5401.28525390625,
        'PC-DARTS': 5171.75146484375,
        'PDARTS': 4918.6455078125,
        'SGAS': 4817.7599609375,
        'SNAS': 4322.32646484375,
        # 'Random': 4592.9845703125,
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
    fig = Figure('grad_var_cifar100_1', figsize=(5, 2.5))
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

    fig2 = Figure('grad_var_cifar100_2', figsize=(5, 2.5))
    fig2.set_axis_label('y', 'After Training')
    fig2.set_axis_lim('x', labels=x_labels, rotation='vertical',
                      lim=[0, len(x_labels)-1], piece=len(x_labels)-1, margin=[1.0, 1.0],
                      _format='%d')
    fig2.set_axis_lim('y', lim=[0, 4], piece=4, margin=[0.0, 0.5],
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
