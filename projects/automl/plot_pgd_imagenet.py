#!/usr/bin/env python3

from alpsplot import ting_color, Figure

color_dict = {
    'Manual': ting_color['blue'],
    'NAS': ting_color['red'],
}
marker_list = ['o', '^', 'd', 's', 'p', '+', 'v', 'x', '8', '2']

model_dict = {
    'Manual': ['BiT', 'DenseNet', 'DLA', 'ResNet', 'ResNext', 'WideResNet'],
    'NAS': ['AmoebaNet', 'DARTS', 'DrNAS', 'ENAS', 'NASNet', 'PC-DARTS', 'pDARTS', 'SGAS', 'SNAS', 'Random'],
}

model_indices = ['BiT', 'DenseNet', 'DLA', 'ResNet', 'ResNext', 'WideResNet',
                 'AmoebaNet', 'DARTS', 'DrNAS', 'ENAS', 'NASNet', 'PC-DARTS', 'pDARTS', 'SGAS', 'SNAS', 'Random']
best_pgd = [0.734375, 0.8359375, 0.8046875, 0.7109375, 0.7578125, 0.6796875,
            0.8125, 0.8203125, 0.765625, 0.7578125, 0.8203125, 0.80468755, 0.8125, 0.8359375, 0.8125, 0.8125]
worst_pgd = [0.5859375, 0.7265625, 0.78125, 0.5703125, 0.6640625, 0.6171875,
             0.734375, 0.734375, 0.6953125, 0.734375, 0.7734375, 0.7109375, 0.6796875, 0.7109375, 0.8046875, 0.65625]

if __name__ == '__main__':
    fig = Figure('pgd_imagenet')
    fig.set_axis_label('x', 'Best Success Rate (%)')
    fig.set_axis_label('y', 'Worst Success Rate (%)')
    fig.set_axis_lim('x', lim=[60, 90], piece=3, margin=[1.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[55, 80], piece=5, margin=[1.0, 1.0],
                     _format='%d')
    for model_type, model_list in model_dict.items():
        color = color_dict[model_type]
        fig.scatter([], [], color=color, marker='s', label=model_type)
        for i, model in enumerate(model_list):
            idx = model_indices.index(model)
            x = best_pgd[idx]*100
            y = worst_pgd[idx]*100
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
