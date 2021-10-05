#!/usr/bin/env python3

from alpsplot import ting_color, Figure
import numpy as np

color_dict = {
    'Manual': ting_color['blue'],
    'NAS': ting_color['red'],
}

data = {
    'Manual': {
        'BiT': 0.001733,
        'DenseNet': 0.001672,
        'DLA': 0.001942,
        'MobileNet': 0.001665,
        'ResNet': 0.001949,
        'ResNext': 0.001679,
        'VGG': 0.001557,
        'WideResnet': 0.002382,
    },
    'NAS': {
        'AmoebaNet': 0.001616,
        'DARTS': 0.001455,
        'DrNAS': 0.001669,
        'ENAS': 0.001588,
        'NASNet': 0.001443,
        'PC-DARTS': 0.001599,
        'PDARTS': 0.001726,
        'ProxylessNAS': 0.001696,
        'SGAS': 0.001638,
        'SNAS': 0.001598,
    }
}

# 200
# data = {
#     'Manual': {
#         'vgg': 0.011106,
#         'resnet': 0.011083,
#         'densenet': 0.012369,
#         'wideresnet': 0.011036,
#         'resnext': 0.011387,
#         'dla': 0.013041,
#         'mobilenet': 0.010690,
#         'bit': 0.009984,
#     },
#     'NAS': {
#         'amoebanet': 0.011000,
#         'enas': 0.010644,
#         'nasnet': 0.010443,
#         'snas_mild': 0.010408,
#         'darts': 0.010552,
#         'pdarts': 0.010181,
#         'pc_darts': 0.009213,
#         'drnas': 0.009743,
#         'sgas': 0.010875,
#         'proxylessnas': 0.011014,
#     }
# }


# def sort(_dict: dict[str, float]):
#     keys = list(_dict.keys())
#     values = list(_dict.values())
#     idx_order = np.argsort(values)
#     new_dict = {}
#     for i in idx_order:
#         new_dict[keys[i]] = values[i]
#     return new_dict


# for k, v in data.items():
#     data[k] = sort(v)


if __name__ == '__main__':
    x_labels = [''] + list(data['Manual'].keys()) \
        + [''] + list(data['NAS'].keys()) + ['']
    x_digits = np.arange(len(x_labels))[1:-1]
    x_data = {
        'Manual': x_digits[:len(data['Manual'].keys())],
        'NAS': x_digits[-len(data['NAS'].keys()):],
    }
    fig = Figure('grad_var_cifar10')
    fig.set_axis_label('y', 'Normalized Gradient Variance')
    fig.set_axis_lim('x', labels=x_labels, rotation='vertical',
                     lim=[0, len(x_labels)-1], piece=len(x_labels)-1, margin=[1.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[1.4, 2.4], piece=5, margin=[0.0, 0.0],
                     _format='%.1f')
    for key in reversed(data.keys()):
        x = np.array(x_data[key])
        y = np.array(list(data[key].values()))
        fig.bar(x, y*1000, color=color_dict[key],
                width=1, align='center', label=key)
    fig.set_legend(edgecolor=None)
    fig.ax.get_legend().remove()
    fig.save(folder_path='./result')
