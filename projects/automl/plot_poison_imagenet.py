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
        'resnet': [52.000, 51.333, 49.367, 47.167, 42.450, 35.500],
        'densenet': [53.733, 52.350, 51.183, 49.267, 45.383, 37.033],
        'wideresnet': [53.950, 52.517, 51.350, 48.750, 46.150, 38.783],
        'resnext': [52.817, 51.967, 50.950, 48.550, 44.300, 36.050],
        'dla': [51.583, 50.050, 48.633, 47.283, 42.683, 33.517],
        'mobilenet': [45.700, 44.883, 43.483, 42.517, 38.583, 31.250],
        # 'vgg': [],
        'bit': [52.483, 51.350, 50.100, 47.817, 43.817, 34.533],
    },
    'NAS': {
        'amoebanet': [52.717, 51.917, 51.150, 49.467, 45.483, 38.183],
        'darts': [52.417, 51.117, 50.400, 48.633, 44.000, 36.217],
        'enas': [52.367, 51.083, 50.967, 48.150, 45.000, 37.350],
        'nasnet': [52.617, 52.183, 50.467, 49.300, 46.133, 36.583],
        'snas_mild': [52.717, 51.200, 49.983, 48.183, 43.317, 34.450],
        'pdarts': [51.700, 51.050, 49.150, 46.200, 43.350, 35.467],
        'pc_darts': [52.200, 50.417, 49.517, 48.383, 44.300, 36.550],
        'drnas': [46.033, 45.433, 47.433, 42.933, 39.433, 31.200],
        'sgas': [51.650, 51.000, 48.633, 46.633, 44.033, 36.117],
        # 'proxylessnas': [],
    },
}

if __name__ == '__main__':
    fig = Figure('imagenet_poison')
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
