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
        'BiT': 92.10,
        'DenseNet': 92.77,
        'DLA': 92.16,
        'ResNet': 92.48,
        'ResNext': 92.39,
        'VGG': 91.77,
        'WideResnet': 92.85,
    },
    'NAS': {
        'AmoebaNet': 93.26,
        'DARTS': 94.15,
        'DrNAS': 93.37,
        'ENAS': 93.20,
        'NASNet': 93.11,
        'PC-DARTS': 94.15,
        'PDARTS': 94.33,
        'SGAS': 94.34,
        'SNAS': 94.12,
        # 'Random': 92.86,
    }
}

data_succ = {
    'Manual': {
        'BiT': 96.93,
        'DenseNet': 96.55,
        'DLA': 95.05,
        'ResNet': 98.96,
        'ResNext': 96.65,
        'VGG': 97.99,
        'WideResnet': 99.50,
    },
    'NAS': {
        'AmoebaNet': 99.79,
        'DARTS': 99.59,
        'DrNAS': 99.98,
        'ENAS': 99.43,
        'NASNet': 99.47,
        'PC-DARTS': 99.33,
        'PDARTS': 99.01,
        'SGAS': 98.06,
        'SNAS': 99.21,
        # 'Random': 99.22,
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
