#!/usr/bin/env python3

from alpsplot import Figure
from alpsplot.colormap import ting_color
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
        'BiT': 92.08,
        'DenseNet': 93.83,
        'DLA': 93.17,
        'ResNet': 92.94,
        'ResNext': 93.31,
        'VGG': 92.25,
        'WideResnet': 92.99,
    },
    'NAS': {
        'AmoebaNet': 94.16,
        'DARTS': 94.34,
        'DrNAS': 94.25,
        'ENAS': 93.84,
        'NASNet': 94.71,
        'PC-DARTS': 94.42,
        'PDARTS': 94.25,
        'SGAS': 94.34,
        'SNAS': 94.07,
        # 'Random': 91.24,
    }
}

data_succ = {
    'Manual': {
        'BiT': 94.96,
        'DenseNet': 94.47,
        'DLA': 94.41,
        'ResNet': 97.64,
        'ResNext': 95.61,
        'VGG': 94.65,
        'WideResnet': 98.68,
    },
    'NAS': {
        'AmoebaNet': 99.74,
        'DARTS': 99.94,
        'DrNAS': 99.64,
        'ENAS': 98.79,
        'NASNet': 99.30,
        'PC-DARTS': 99.98,
        'PDARTS': 99.58,
        'SGAS': 99.90,
        'SNAS': 99.92,
        # 'Random': 99.60,
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
