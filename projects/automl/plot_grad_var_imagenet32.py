#!/usr/bin/env python3

from alpsplot import ting_color, Figure
import numpy as np

color_dict = {
    'Manual': ting_color['blue'],
    'NAS': ting_color['red'],
}

data_before = {
    'Manual': {
        'BiT': 9452.143359375,
        'DenseNet': 4251.89833984375,
        'DLA': 33.16884841918945,
        'ResNet': 8152.391015625,
        'ResNext': 2670.86748046875,
        'VGG': 1433.4701416015625,
        'WideResnet': 10883.23515625,
    },
    'NAS': {
        'AmoebaNet': 51.74474945068359,
        'DARTS': 44.5401107788086,
        'DrNAS': 43.552686309814455,
        'ENAS': 52.26239242553711,
        'NASNet': 62.67582550048828,
        'PC-DARTS': 44.70255966186524,
        'PDARTS': 43.96416015625,
        'SGAS': 43.7796875,
        'SNAS': 50.07753143310547,
        # 'Random': 51.8597915649414,
    }
}

data_after = {
    'Manual': {
        'BiT': 13769.44921875,
        'DenseNet': 7897.20732421875,
        'DLA': 11399.5103515625,
        'ResNet': 10671.3685546875,
        'ResNext': 8090.85888671875,
        'VGG': 8898.114453125,
        'WideResnet': 22239.776953125,
    },
    'NAS': {
        'AmoebaNet': 4787.5173828125,
        'DARTS': 5111.29033203125,
        'DrNAS': 5267.53154296875,
        'ENAS': 5322.66806640625,
        'NASNet': 5232.12841796875,
        'PC-DARTS': 5309.467578125,
        'PDARTS': 4971.6212890625,
        'SGAS': 5109.27861328125,
        'SNAS': 4823.9138671875,
        # 'Random': 4828.262890625,
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
    fig = Figure('grad_var_imagenet32_1', figsize=(5, 2.5))
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

    fig2 = Figure('grad_var_imagenet32_2', figsize=(5, 2.5))
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
