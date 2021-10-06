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

x = [0, 2.5, 5, 10, 20, 40]
y = {
    'Manual': {
        'resnet': [75.36, 74.43, 73.74, 72.08, 67.41, 55.29],
        'densenet': [76.58, 75.64, 74.44, 72.38, 67.65, 59.17],
        'wideresnet': [76.81, 75.24, 75.17, 73.52, 69.76, 57.14],
        'resnext': [76.34, 75.87, 74.26, 71.89, 68.82, 59.21],
        'dla': [75.82, 74.49, 73.62, 72.73, 69.26, 60.08],
        'mobilenet': [72.41, 71.14, 70.36, 67.76, 62.45, 51.62],
        'vgg': [70.27, 69.01, 68.20, 66.80, 62.29, 51.13],
        'bit': [77.84, 76.39, 75.51, 74.07, 70.62, 62.31],
    },
    'NAS': {
        'amoebanet': [74.70, 73.43, 71.22, 67.86, 62.76, 49.33],
        'darts': [73.69, 72.37, 69.92, 67.73, 61.83, 50.40],
        'enas': [73.84, 72.58, 70.47, 67.68, 63.31, 48.30],
        'nasnet': [73.94, 72.86, 70.65, 68.89, 63.49, 51.05],
        'snas_mild': [74.38, 72.65, 71.64, 68.20, 63.63, 51.69],
        'pdarts': [73.10, 71.42, 69.71, 68.26, 61.45, 45.64],
        'pc_darts': [73.81, 71.83, 70.44, 67.86, 62.97, 50.37],
        'drnas': [69.35, 68.40, 64.20, 62.10, 55.99, 40.73],
        'sgas': [71.75, 69.57, 69.46, 65.29, 58.69, 44.67],
        # 'proxylessnas': [],
    },
}

if __name__ == '__main__':
    fig = Figure('cifar100_poison')
    fig.set_axis_label('x', 'Poisoning Percentage (%)')
    fig.set_axis_label('y', 'Clean Accuracy Drop (%)')
    fig.set_axis_lim('x', lim=[0, 40], piece=4, margin=[1.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[0, 28], piece=4, margin=[1.0, 1.0],
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
        print(y_mean_list)
    fig.set_legend(edgecolor=None)
    fig.save(folder_path='./result')
