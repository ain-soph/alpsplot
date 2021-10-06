#!/usr/bin/env python3

from alpsplot import Figure, ting_color
import numpy as np
import argparse

color_dict = {
    'Manual': ting_color['blue'],
    'NAS': ting_color['red'],
}
mark_dict = {
    'NAS': 's',
    'Manual': '^',
}

x = [1, 2, 4, 8, 16]
y = {
    # 'acc': {
    #     'Manual': {
    #         'vgg': [29.08, 47.48, 52.41, 62.46, 74.28],
    #         'resnet': [34.85, 42.50, 51.19, 62.41, 71.80],
    #         'densenet': [39.38, 50.21, 56.66, 68.31, 77.14],
    #         'wideresnet': [31.65, 34.44, 41.66, 47.84, 64.86],
    #         'resnext': [26.88, 40.15, 47.12, 47.12, 71.09],
    #         'dla': [37.45, 43.28, 53.44, 66.88, 75.38],
    #         # 'mobilenet': [28.89, 37.86, 44.76, 58.07, 70.50]
    #     },
    #     'NAS': {
    #         'amoebanet': [29.16, 42.88, 46.97, 60.66, 74.43],
    #         'darts': [16.28, 29.00, 40.36, 59.75, 71.65],
    #         'enas': [24.51, 37.09, 45.41, 56.89, 69.49],
    #         'nasnet': [31.99, 40.10, 47.63, 60.09, 72.12],
    #         'snas_mild': [25.59, 38.11, 42.65, 64.65, 74.36],
    #         'pdarts': [28.67, 34.67, 37.30, 51.81, 70.10],
    #         'pc_darts': [26.53, 35.85, 43.46, 58.37, 68.13],
    #         'sgas': [25.03, 27.48, 41.19, 45.00, 58.89],
    #         'drnas': [12.36, 24.80, 38.00, 42.20, 56.95],
    #         # 'proxylessnas': [34.38, 41.79, 56.21, 67.41, 74.31],
    #     },
    # },
    'loss': {
        'Manual': {
            'vgg': [4.683, 2.899, 2.224, 1.682, 1.084],
            'resnet': [3.550, 2.789, 2.368, 1.903, 1.289],
            'densenet': [3.098, 2.431, 1.993, 1.470, 1.005],
            'wideresnet': [2.157, 3.716, 3.372, 3.043, 2.067],
            'resnext': [1.971, 2.071, 1.927, 1.999, 1.427],
            'dla': [2.893, 3.217, 2.451, 1.618, 1.227],
            # 'mobilenet': [3.903, 4.274, 2.993, 2.132, 1.282]
        },
        'NAS': {
            'amoebanet': [2.771, 2.247, 2.138, 1.499, 0.993],
            'darts': [2.341, 2.318, 2.089, 1.575, 1.311],
            'enas': [2.409, 2.108, 1.959, 1.502, 1.220],
            'nasnet': [4.035, 2.816, 2.653, 1.878, 1.189],
            'snas_mild': [4.020, 3.280, 3.425, 1.726, 1.282],
            'pdarts': [2.012, 1.938, 1.829, 1.581, 1.128],
            'pc_darts': [2.294, 2.259, 2.002, 1.443, 1.192],
            'sgas': [2.148, 2.283, 1.829, 2.063, 1.498],
            'drnas': [2.302, 2.261, 1.739, 1.633, 1.354],
            # 'proxylessnas': [2.740, 2.512, 1.968, 1.408, 1.204],
        },
    },
}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--metric', choices=['loss', 'acc'], default='loss')
    args = parser.parse_args()
    metric: str = args.metric

    fig = Figure(f'extraction_cifar10_{metric}')
    fig.set_axis_label('x', 'Query Number (k)')
    fig.set_axis_label('y', 'Cross Entropy' if metric == 'loss'
                       else 'Thieved Model Acc (%)')
    fig.set_axis_lim('x', lim=[0, 16], piece=4, margin=[0.0, 1.0],
                     _format='%d')
    if metric == 'loss':
        fig.set_axis_lim('y', lim=[1, 4], piece=3, margin=[0.0, 0.0],
                         _format='%d')
    else:
        fig.set_axis_lim('y', lim=[20, 80], piece=3, margin=[0.0, 0.0],
                         _format='%d')

    for key, sub_dict in y[metric].items():
        x_list = []
        y_list = []
        y_mean_list = []
        for value in sub_dict.values():
            value = np.array(value)
            x_list.append(x[:len(value)])
            y_list.append(value)
        for i in range(len(x)):
            mean_temp_list = []
            for j in range(len(y_list)):
                if len(y_list[j]) > i:
                    mean_temp_list.append(y_list[j][i])
            y_mean_list.append(np.mean(mean_temp_list))
        x_list = np.concatenate(x_list)
        y_list = np.concatenate(y_list)
        fig.lineplot(x=x_list, y=y_list, color=color_dict[key])
        fig.scatter(x=x[:len(y_mean_list)], y=y_mean_list, color=color_dict[key],
                    marker=mark_dict[key], label=key)
    fig.set_legend(edgecolor=None)
    fig.save(folder_path='./result')
