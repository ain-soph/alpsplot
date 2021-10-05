#!/usr/bin/env python3

from alpsplot import ting_color, Figure
import numpy as np

color_dict = {
    'Manual': ting_color['blue'],
    'NAS': ting_color['red'],
}
marker_list = ['o', '^', 'd', 's', 'p', '+', 'v', 'x', '8', '2']

model_dict = {
    'Manual': ['BiT', 'DenseNet', 'DLA', 'ResNet', 'ResNext', 'VGG', 'WideResNet'],
    'NAS': ['AmoebaNet', 'DARTS', 'DrNAS', 'ENAS', 'NASNet', 'PC-DARTS', 'pDARTS', 'SGAS', 'SNAS', 'Random'],
}

model_indices = ['BiT', 'DenseNet', 'DLA', 'ResNet', 'ResNext', 'VGG', 'WideResNet',
                 'AmoebaNet', 'DARTS', 'DrNAS', 'ENAS', 'NASNet', 'PC-DARTS', 'pDARTS', 'SGAS', 'SNAS', 'Random']
succ_rate = [39.14, 45.12, 45.22, 44.17, 39.01, 42.19, 38.28,
             35.46, 41.74, 31.82, 35.56, 43.29, 33.58, 42.39, 39.50, 41.06, 36.30]
org_acc = [96.62, 96.73, 96.45, 96.58, 96.73, 95.06, 96.75,
           96.92, 97.04, 96.87, 96.77, 97.00, 96.86, 97.07, 97.15, 96.93, 96.74]
after_acc = [85.93, 87.58, 87.81, 87.08, 81.36, 82.77, 80.47,
             78.98, 89.27, 79.93, 74.48, 88.05, 76.69, 89.47, 86.39, 88.74, 79.10]
acc_drop = np.array(org_acc) - np.array(after_acc)

if __name__ == '__main__':
    fig = Figure('adv_train_cifar10', figsize=(5, 2.5))
    fig.set_axis_label('x', 'Attack Success Rate (%)')
    fig.set_axis_label('y', 'Clean Accuracy Drop (%)')
    fig.set_axis_lim('x', lim=[55, 70], piece=3, margin=[1.0, 0.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[5, 25], piece=4, margin=[0.0, 0.0],
                     _format='%d')
    for model_type, model_list in model_dict.items():
        color = color_dict[model_type]
        fig.scatter([], [], color=color, marker='s', label=model_type)
        for i, model in enumerate(model_list):
            idx = model_indices.index(model)
            x = 100-succ_rate[idx]
            y = acc_drop[idx]
            marker = marker_list[i]
            kwargs = {}
            if marker in ['P', 'x', '2', '+']:
                kwargs['facecolor'] = color_dict[model_type]
                kwargs['color'] = None
            else:
                kwargs['color'] = color_dict[model_type]
                kwargs['facecolor'] = 'none'
            fig.scatter(x=x, y=y, marker=marker,
                        linewidth=1.5, s=64, **kwargs)
    fig.set_legend(edgecolor=None, loc='lower left')
    fig.ax.get_legend().remove()
    fig.save(folder_path='./result')
