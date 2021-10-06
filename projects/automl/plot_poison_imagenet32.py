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
        'bit': [72.233, 70.433, 70.233, 67.733, 63.867, 53.333],
        'densenet': [71.900, 70.800, 69.800, 66.700, 62.967, 52.600],
        'dla': [71.167, 70.600, 69.333, 67.533, 63.700, 52.700],
        'resnet': [68.367, 66.433, 65.833, 64.733, 60.033, 50.633],
        'resnext': [71.733, 71.500, 69.867, 68.200, 64.033, 53.700],
        'vgg': [63.100, 61.567, 60.267, 57.800, 52.833, 37.800],
        'wideresnet': [72.667, 71.133, 70.300, 69.167, 65.033, 56.367],
        # 'mobilenet': [68.267, 66.933, 65.433, 63.467, 57.000, 44.767],
    },
    'NAS': {
        'amoebanet': [71.500, 69.933, 67.700, 66.167, 60.200, 50.700],
        # 'darts': [70.667, 68.800, , , , ],  # 2-nas1
        # 'enas': [70.500, 69.267, 67.267, , , ],
        # 'nasnet': [, , , , , ], # TODO
        'pc_darts': [71.533, 68.933, 67.867, 64.400, 59.200, 45.567],
        'pdarts': [71.267, 67.967, 66.267, 63.300, 56.933, 42.033],
        # 'drnas': [66.867, 63.600, 61.033, , , ],
        # 'sgas': [70.633, 68.567, , , , ],
        'snas_mild': [70.700, 68.833, 68.633, 65.500, 58.500, 45.467],
        # 'random': [68.500, 65.100, 64.167, 61.933, 55.567, ],
        # 'proxylessnas': [],
    },
}

if __name__ == '__main__':
    fig = Figure('imagenet_poison')
    fig.set_axis_label('x', 'Poisoning Percentage (%)')
    fig.set_axis_label('y', 'Clean Accuracy Drop (%)')
    fig.set_axis_lim('x', lim=[0, 40], piece=4, margin=[1.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[0, 30], piece=3, margin=[1.0, 1.0],
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
