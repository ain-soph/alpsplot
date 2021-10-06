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

x = [4, 8, 12, 16]
y = {
    'Manual': {
        'bit': [680, 834, 899, 939],
        'densenet': [834, 962, 985, 994],
        'dla': [729, 889, 957, 978],
        'resnet': [723, 858, 915, 949],
        'resnext': [879, 975, 995, 998],
        'vgg': [887, 984, 998, 1000],
        'wideresnet': [735, 914, 963, 974],
    },
    'NAS': {
        'amoebanet': [760, 907, 945, 965],
        'darts': [881, 959, 987, 992],
        'drnas': [881, 969, 985, 989],
        'enas': [878, 963, 972, 984],
        'nasnet': [833, 946, 979, 986],
        'pc_darts': [754, 907, 952, 969],
        'pdarts': [760, 933, 972, 990],
        'sgas': [780, 917, 953, 967],
        'snas_mild': [813, 937, 963, 981],
    },
}

for k1 in y.keys():
    for k2 in y[k1].keys():
        for i in range(len(y[k1][k2])):
            if y[k1][k2][i] > 1:
                y[k1][k2][i] = y[k1][k2][i]/10

if __name__ == '__main__':
    fig = Figure('eps_pgd')
    fig.set_axis_label('x', r'Perturbation threshold $\varepsilon$ (/255)')
    fig.set_axis_label('y', 'Attack Success Rate (%)')
    fig.set_axis_lim('x', lim=[4, 16], piece=3, margin=[1.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[70, 100], piece=3, margin=[1.0, 1.0],
                     _format='%d')

    for key, sub_dict in y.items():
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
