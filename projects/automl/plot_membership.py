#!/usr/bin/env python3

from alpsplot import *
import numpy as np

color_dict = {
    'Manual': ting_color['blue'],
    'AutoML': ting_color['red'],
}

model_acc = {
    'Manual': [95.06, 96.58, 96.73, 96.75, 96.73, 96.34, 96.45, 95.53, 94.26],
    'AutoML': [96.92, 96.77, 97.00, 96.93, 97.04, 95.58, 97.07, 96.86, 96.87, 97.15, 97.18, 97.15]
}
data = {
    'Manual': {
        'vgg': 0.5942028985507247,
        'resnet': 0.4423076923076923,
        'densenet': 0.5357142857142857,
        'wideresnet': 0.6447368421052632,
        'resnext': 0.6447368421052632,
        'dla': 0.5426356589147288,
        'mobilenet': 0.5042016806722689,
    },
    'AutoML': {
        'amoebanet': 0.6936416184971099,
        'enas': 0.7023809523809524,
        'nasnet': 0.6951219512195121,
        'snas_mild': 0.5409836065573771,
        'darts': 0.679245283018868,
        'pdarts': 0.6486486486486486,
        'pc_darts': 0.6540880503144655,
        'drnas': 0.7,
        'sgas': 0.60431654676259,
        'proxylessnas': 0.6,
        # 'lanet':,
    }
}


if __name__ == '__main__':
    x_labels = [''] + list(data['Manual'].keys()) \
        + [''] + list(data['AutoML'].keys()) + ['']
    x_digits = np.arange(len(x_labels))[1:-1]
    x_data = {
        'Manual': x_digits[:len(data['Manual'].keys())],
        'AutoML': x_digits[-len(data['AutoML'].keys()):],
    }
    fig = Figure('cifar10_membership')
    fig.set_axis_label('x', 'Model')
    fig.set_axis_label('y', 'F1 Score')
    fig.set_axis_lim('x', labels=x_labels, rotation='vertical',
                     lim=[0, len(x_labels)-1], piece=len(x_labels)-1, margin=[1.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[0.4, 0.8], piece=4, margin=[0.0, 0.0],
                     _format='%.1f')
    for key in reversed(data.keys()):
        x = np.array(x_data[key])
        y = np.array(list(data[key].values()))
        fig.bar(x, y, color=color_dict[key],
                width=1, align='center', label=key)
    fig.set_legend(edgecolor=None)
    fig.save(folder_path='./result')
