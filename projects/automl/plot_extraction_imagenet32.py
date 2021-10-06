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
            'bit': [6.653, 6.515, 6.590, 5.974, 5.348],
            'densenet': [6.369, 6.480, 6.108, 5.305, 4.957],
            'dla': [6.725, 7.598, 7.664, 6.307, 5.745],
            'resnet': [6.428, 6.368, 6.079, 5.036, 4.305],
            'resnext': [4.100, 4.056, 4.067, 3.726, 3.395],
            'vgg': [4.244, 4.200, 4.003, 4.003, 3.812],
            'wideresnet': [4.132, 4.120, 3.946, 3.929, 3.344],
        },
        'NAS': {
            'amoebanet': [4.549, 4.736, 4.660, 4.295, 3.139],
            'darts': [4.746, 4.864, 3.984, 4.120, 3.475],
            'drnas': [4.124, 4.059, 3.980, 3.900, 3.626],
            'enas': [4.094, 4.090, 4.003, 3.764, 3.396],
            # 'nasnet': [6.780, 6.302, 4.122, 3.888, 3.945],
            'pc_darts': [4.471, 4.488, 4.115, 3.687, 3.411],
            'pdarts': [4.556, 4.271, 3.962, 3.585, 3.537],
            'sgas': [4.129, 4.230, 3.975, 3.702, 3.506],
            # 'snas_mild': [9.269, 9.199, 8.219, 6.977, 5.663],
            'random': [4.415, 4.296, 4.013, 3.737, 3.318],
        },
    },
}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--metric', choices=['loss', 'acc'], default='loss')
    args = parser.parse_args()
    metric: str = args.metric

    fig = Figure(f'extraction_imagenet32_{metric}')
    fig.set_axis_label('x', 'Query Number (k)')
    fig.set_axis_label('y', 'Cross Entropy' if metric == 'loss'
                       else 'Thieved Model Acc (%)')
    fig.set_axis_lim('x', lim=[0, 16], piece=4, margin=[0.0, 1.0],
                     _format='%d')
    if metric == 'loss':
        fig.set_axis_lim('y', lim=[3.5, 6.5], piece=3, margin=[0.0, 0.0],
                         _format='%.1f')
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
