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
        'bit': [572, 797, 894, 950],
        'densenet': [608, 851, 939, 973],
        'dla': [576, 776, 899, 950],
        'resnet': [640, 813, 888, 937],
        'resnext': [703, 912, 970, 991],
        'vgg': [633, 878, 953, 971],
        'wideresnet': [527, 813, 921, 962],
    },
    'NAS': {
        'amoebanet': [617, 828, 929, 974],
        'darts': [617, 828, 929, 974],
        'drnas': [678, 897, 957, 977],
        'enas': [677, 891, 952, 979],
        'nasnet': [677, 879, 947, 981],
        'pc_darts': [617, 818, 909, 956],
        'pdarts': [577, 828, 927, 974],
        'sgas': [615, 842, 919, 952],
        'snas_mild': [665, 850, 932, 963],
    },
}

for k1 in y.keys():
    for k2 in y[k1].keys():
        for i in range(len(y[k1][k2])):
            if y[k1][k2][i] > 1:
                y[k1][k2][i] = y[k1][k2][i]/10

if __name__ == '__main__':
    fig = Figure('eps_nes')
    fig.set_axis_label('x', r'Perturbation threshold $\varepsilon$ (/255)')
    fig.set_axis_label('y', 'Attack Success Rate (%)')
    fig.set_axis_lim('x', lim=[4, 16], piece=3, margin=[1.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[55, 100], piece=3, margin=[1.0, 1.0],
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
