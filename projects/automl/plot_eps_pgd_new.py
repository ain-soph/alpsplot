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

x = [1, 2, 3, 4]
y = {
    'Manual': {
        'bit': [395, 632, 776, 933],
        'densenet': [462, 745, 862, 992],
        'dla': [407, 713, 850, 950],
        'resnet': [483, 740, 846, 941],
        'resnext': [486, 749, 850, 995],
        'vgg': [418, 737, 869, 991],
        'wideresnet': [394, 678, 800, 980],
    },
    'NAS': {
        'amoebanet': [443, 654, 750, 974],
        'darts': [508, 712, 798, 998],
        'drnas': [447, 669, 790, 997],
        'enas': [504, 722, 816, 996],
        'nasnet': [458, 668, 782, 992],
        'pc_darts': [462, 680, 783, 986],
        'pdarts': [395, 641, 752, 985],
        'sgas': [469, 705, 798, 986],
        'snas_mild': [464, 709, 811, 983],
    },
}

for k1 in y.keys():
    for k2 in y[k1].keys():
        for i in range(len(y[k1][k2])):
            if y[k1][k2][i] > 1:
                y[k1][k2][i] = y[k1][k2][i]/10

if __name__ == '__main__':
    fig = Figure('eps_pgd_new')
    fig.set_axis_label('x', r'Perturbation threshold $\varepsilon$ (/255)')
    fig.set_axis_label('y', 'Attack Success Rate (%)')
    fig.set_axis_lim('x', lim=[1, 4], piece=3, margin=[1.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[40, 100], piece=3, margin=[1.0, 1.0],
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
