#!/usr/bin/env python3

from alpsplot import Figure, ting_color
import numpy as np

color_dict = {
    'Manual': ting_color['blue'],
    'NAS': ting_color['red'],
}
mark_dict = {
    'NAS': 's',
    'Manual': '^',
}
# color_dict = {
#     'resnet': ting_color['red_carrot'],
#     'densenet': ting_color['yellow'],
#     'wideresnet': ting_color['green'],
#     'amoebanet': ting_color['blue'],
#     'darts': ting_color['red_deep'],
#     'enas': ting_color['purple'],
#     # 'bypass_embed': ting_color['blue_light'],
# }
# mark_dict = {
#     'resnet': 'H',
#     'densenet': '^',
#     'wideresnet': 'o',
#     'amoebanet': 'v',
#     'darts': 's',
#     'enas': 'p',
#     # 'bypass_embed': 'h',
#     # 'imc': 'D',
# }
# batch mode
# x = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# # y = [96.58, 96.23, 94.07, 93.13, 92.03, 91.86, 89.46, 85.32, 65.33, 10.33, 10]  # resnet18_comp 300 (abandon)
# y = {
#     'resnet': [93.78, 93.36, 93.12, 92.28, 90.86, 88.72, 85.16, 75.44, 52.47, 10.79, 0.59],
#     'darts': [93.76, 93.14, 92.18, 91.08, 88.74, 86.05, 80.44, 63.33, 33.90, 10.26, 4.73],
#     'enas': [94.09, 92.86, 92.65, 90.76, 89.74, 86.48, 80.48, 63.18, 40.31, 10.10, 1.02],
# }

x = [0, 2.5, 5, 10, 20, 30, 40]
y = {
    'Manual': {
        'resnet': [93.78, 93.79, 93.30, 92.16, 90.58, 88.77, 86.13],
        'densenet': [94.68, 94.07, 93.56, 92.87, 91.41, 89.10, 86.28],
        'wideresnet': [94.01, 93.64, 93.56, 92.78, 91.31, 89.42, 86.73],
        'resnext': [94.35, 93.71, 91.20, 92.12, 89.93, 87.09, 83.02],
        'dla': [94.50, 93.91, 93.43, 92.61, 91.05, 82.50, 77.84],
        'mobilenet': [92.90, 92.25, 91.46, 89.98, 87.67, 83.65, 80.11],
        # 'vgg': [],
        'bit': [94.88, 94.23, 93.94, 93.36, 91.67, 89.76, 87.61],
    },
    'NAS': {
        'amoebanet': [94.50, 93.29, 93.02, 90.14, 86.97, 83.54, 82.58],
        'darts': [93.76, 92.47, 92.64, 90.67, 87.59, 81.50, 77.56],
        'enas': [94.09, 92.64, 92.13, 90.39, 85.51, 81.67, 78.23],
        'nasnet': [94.26, 93.29, 92.58, 90.88, 87.78, 82.50, 77.84],
        'snas_mild': [94.16, 92.70, 91.89, 90.70, 87.51, 87.09, 83.02],
        'pdarts': [93.19, 91.84, 91.29, 89.65, 86.37, 80.32, 73.95],
        'pc_darts': [93.86, 93.11, 92.11, 90.17, 86.92, 83.70, 78.99],
        # 'drnas': [],
        # 'sgas': [],
        # 'proxylessnas': [94.60, ,93.47, ],
    },
}

if __name__ == '__main__':
    fig = Figure('cifar10_poison')
    fig.set_axis_label('x', 'Poisoning Percentage (%)')
    fig.set_axis_label('y', 'Clean Accuracy Drop (%)')
    fig.set_axis_lim('x', lim=[0, 40], piece=4, margin=[1.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[0, 20], piece=4, margin=[1.0, 1.0],
                     _format='%d')

    for key, sub_dict in y.items():
        x_list = []
        y_list = []
        y_mean_list = []
        for value in sub_dict.values():
            value = np.array(value)
            x_list.append(x[:len(value)])
            y_list.append(value[0] - value)
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
