#!/usr/bin/env python3

from alpsplot import ting_color, Figure

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
best_pgd = [697, 731, 648, 736, 720, 773, 631,
            701, 723, 705, 728, 718, 702, 655, 704, 759, 643]
worst_pgd = [103, 175, 123, 157, 187, 100, 83,
             257, 258, 192, 291, 287, 204, 213, 171, 222, 127]

if __name__ == '__main__':
    fig = Figure('nes_cifar10')
    fig.set_axis_label('x', 'Most Likely Case (%)')
    fig.set_axis_label('y', 'Least Likely Case (%)')
    fig.set_axis_lim('x', lim=[60, 80], piece=4, margin=[1.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[0, 30], piece=3, margin=[1.0, 1.0],
                     _format='%d')
    for model_type, model_list in model_dict.items():
        color = color_dict[model_type]
        fig.scatter([], [], color=color, marker='s', label=model_type)
        for i, model in enumerate(model_list):
            idx = model_indices.index(model)
            x = best_pgd[idx]/10
            y = worst_pgd[idx]/10
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
