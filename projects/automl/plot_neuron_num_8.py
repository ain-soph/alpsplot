#!/usr/bin/env python3

from alpsplot import ting_color, Figure
import numpy as np
import os

color_dict = {
    'Manual': ting_color['blue'],
    'NAS': ting_color['red'],
}

model_acc = {
    'Manual': [96.62, 96.73, 96.45, 96.58, 96.73, 95.06, 96.75],
    'NAS': [96.92, 97.04, 96.87, 96.77, 97.00, 96.86, 97.07, 97.15, 96.93, 96.74]
}

data_acc = {
    'Manual': {
        'BiT': 91.73,
        'DenseNet': 92.69,
        'DLA': 91.59,
        'ResNet': 91.76,
        'ResNext': 91.74,
        'VGG': 90.00,
        'WideResnet': 92.57,
    },
    'NAS': {
        'AmoebaNet': 93.98,
        'DARTS': 93.77,
        'DrNAS': 93.22,
        'ENAS': 93.41,
        'NASNet': 93.42,
        'PC-DARTS': 94.21,
        'PDARTS': 94.12,
        'SGAS': 93.91,
        'SNAS': 93.85,
        # 'Random': 93.45,
    }
}

data_succ = {
    'Manual': {
        'BiT': 99.33,
        'DenseNet': 98.80,
        'DLA': 99.63,
        'ResNet': 99.64,
        'ResNext': 97.64,
        'VGG': 99.64,
        'WideResnet': 99.48,
    },
    'NAS': {
        'AmoebaNet': 100.00,
        'DARTS': 99.39,
        'DrNAS': 100.00,
        'ENAS': 99.82,
        'NASNet': 99.03,
        'PC-DARTS': 99.70,
        'PDARTS': 99.95,
        'SGAS': 99.07,
        'SNAS': 99.01,
        # 'Random': 99.54,
    }
}

if __name__ == '__main__':
    x_labels = [''] + list(data_acc['Manual'].keys()) \
        + [''] + list(data_acc['NAS'].keys()) + ['']
    x_digits = np.arange(len(x_labels))[1:-1]
    x_data = {
        'Manual': x_digits[:len(data_acc['Manual'].keys())],
        'NAS': x_digits[-len(data_acc['NAS'].keys()):],
    }
    fig = Figure(os.path.splitext(os.path.basename(__file__).removeprefix('plot_'))[0]+'_succ', figsize=(5, 2.5))
    fig.set_axis_label('y', 'Attack Success Rate (%)')
    fig.set_axis_lim('x', labels=x_labels, rotation='vertical',
                     lim=[0, len(x_labels)-1], piece=len(x_labels)-1, margin=[1.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[85, 100], piece=3, margin=[0.0, 0.2],
                     _format='%d')
    for key in reversed(data_succ.keys()):
        x = np.array(x_data[key])
        y = np.array(list(data_succ[key].values()))
        fig.bar(x, y, color=color_dict[key],
                width=1, align='center', label=key)
    fig.set_legend(edgecolor=None)
    fig.ax.get_legend().remove()
    fig.save(folder_path='./result')

    fig2 = Figure(os.path.splitext(os.path.basename(__file__).removeprefix('plot_'))[0]+'_acc', figsize=(5, 2.5))
    fig2.set_axis_label('y', 'Clean Accuracy Drop (%)')
    fig2.set_axis_lim('x', labels=x_labels, rotation='vertical',
                      lim=[0, len(x_labels)-1], piece=len(x_labels)-1, margin=[1.0, 1.0],
                      _format='%d')
    fig2.set_axis_lim('y', lim=[2, 5], piece=3, margin=[0.0, 0.2],
                      _format='%d')
    fig2.ax.invert_yaxis()
    fig2.ax.xaxis.tick_top()
    for key in reversed(data_acc.keys()):
        x = np.array(x_data[key])
        y = np.array(list(data_acc[key].values()))
        y = np.array(model_acc[key][:len(y)]) - y
        fig2.bar(x, y, edgecolor=color_dict[key], color='white',
                 width=0.85, align='center', label=key)
    fig2.set_legend(edgecolor=None)
    fig2.ax.get_legend().remove()
    fig2.save(folder_path='./result',)
