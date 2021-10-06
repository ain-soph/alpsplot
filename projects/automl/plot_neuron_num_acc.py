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

model_acc = {
    'Manual': [96.62, 96.73, 96.45, 96.58, 96.73, 95.06, 96.75],
    'NAS': [96.92, 97.04, 96.87, 96.77, 97.00, 96.86, 97.07, 97.15, 96.93, 96.74]
}

x = [1, 2, 4, 8]
y = {
    'Manual': {
        'bit': [92.17, 92.08, 92.10, 91.73],
        'densenet': [93.64, 93.83, 92.77, 92.69],
        'dla': [91.87, 93.17, 92.16, 91.59],
        'resnet': [93.42, 92.94, 92.48, 91.76],
        'resnext': [94.35, 93.31, 92.39, 91.74],
        'vgg': [91.72, 92.25, 91.77, 90.00],
        'wideresnet': [93.54, 92.99, 92.85, 92.57],
    },
    'NAS': {
        'amoebanet': [93.48, 94.16, 93.26, 93.98],
        'darts': [93.35, 94.34, 94.15, 93.77],
        'drnas': [93.44, 94.25, 93.37, 93.22],
        'enas': [93.26, 93.84, 93.20, 93.41],
        'nasnet': [93.35, 94.71, 93.11, 93.42],
        'pc_darts': [93.80, 94.42, 94.15, 94.21],
        'pdarts': [94.08, 94.25, 94.33, 94.12],
        'sgas': [94.03, 94.34, 94.34, 93.91],
        'snas_mild': [94.38, 94.07, 94.12, 93.85],
    },
}

if __name__ == '__main__':
    fig = Figure('neuron_num_acc')
    fig.set_axis_label('x', 'Neuron Number')
    fig.set_axis_label('y', 'Clean Accuracy Drop (%)')
    fig.set_axis_lim('x', lim=[0, 8], piece=4, margin=[0.1, 0.1],
                     _format='%d')
    fig.set_axis_lim('y', lim=[2, 6], piece=4, margin=[1.0, 1.0],
                     _format='%d')

    for key, sub_dict in y.items():
        x_list = []
        y_list = []
        y_mean_list = []
        for j, value in enumerate(sub_dict.values()):
            value = np.array(value)
            x_list.append(x[:len(value)])
            y_list.append(model_acc[key][j]-value)
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
