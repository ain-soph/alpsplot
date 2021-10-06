#!/usr/bin/env python3

from alpsplot import Figure, ting_color
from alpsplot.utils import avg_smooth, avg_smooth_err_bar
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
    'loss': {
        'Manual': {
            # 'vgg': [4.805, 4.704, 4.637, 3.896, 3.545],
            # 'resnet': [4.612, 4.454, 4.256, 3.816, 2.987],
            # 'densenet': [4.968, 4.867, 4.252, 3.437, 2.501],
            'wideresnet': [7.281, 7.234, 6.217, 6.386, 4.863],
            'resnext': [6.142, 6.054, 5.756, 5.598, 3.869],
            'dla': [5.189, 4.666, 4.478, 4.006, 3.310],
            'mobilenet': [5.838, 5.645, 5.517, 4.650, 3.756]
        },
        'NAS': {
            # 'amoebanet': [6.544, 6.109, 5.628, 4.609, 3.289],
            'darts': [5.608, 5.250, 5.077, 4.784, 3.844],
            'enas': [5.344, 5.128, 4.992, 4.549, 4.235],
            # 'nasnet': [7.898, 7.455, 6.452, 5.317, 3.940],
            # 'snas_mild': [7.365, 6.045, 5.531, 4.900, 3.827],
            'pdarts': [4.772, 4.510, 4.392, 4.125, 3.786],
            'pc_darts': [5.828, 5.262, 5.180, 4.613, 4.157],
            'sgas': [5.601, 4.645, 4.362, 4.337, 3.870],
            'drnas': [4.694, 4.691, 4.261, 4.014, 3.248],
        },
    },
}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--metric', choices=['loss', 'acc'], default='loss')
    args = parser.parse_args()
    metric: str = args.metric

    fig = Figure(f'extraction_cifar100_{metric}')
    fig.set_axis_label('x', 'Query Number (k)')
    fig.set_axis_label('y', 'Cross Entropy' if metric == 'loss'
                       else 'Thieved Model Acc (%)')
    fig.set_axis_lim('x', lim=[0, 16], piece=4, margin=[0.0, 1.0],
                     _format='%d')
    if metric == 'loss':
        fig.set_axis_lim('y', lim=[4, 7], piece=3, margin=[0.2, 0.0],
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
        y_mean_list = avg_smooth(y_mean_list)
        x_list, y_list = avg_smooth_err_bar(x_list, y_list)
        y_mean_list = avg_smooth(y_mean_list)
        x_list, y_list = avg_smooth_err_bar(x_list, y_list)
        fig.lineplot(x=x_list, y=y_list, color=color_dict[key])
        fig.scatter(x=x[:len(y_mean_list)], y=y_mean_list, color=color_dict[key],
                    marker=mark_dict[key], label=key)
    fig.set_legend(edgecolor=None)
    fig.save(folder_path='./result')
