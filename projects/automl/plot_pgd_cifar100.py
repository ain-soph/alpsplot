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
best_pgd = [0.859375, 0.7578125, 0.8203125, 0.9140625, 0.7734375, 0.6875, 0.8046875,
            0.9296875, 0.875, 0.828125, 0.9296875, 0.921875, 0.9296875, 0.8671875, 0.828125, 0.984375, 0.8828125]
worst_pgd = [0.40625, 0.7109375, 0.7578125, 0.8828125, 0.6953125, 0.4375, 0.609375,
             0.84375, 0.7890625, 0.6953125, 0.9140625, 0.875, 0.875, 0.7265625, 0.609375, 0.953125, 0.703125]
# best_pgd = [0.8734999999999999, 0.7845, 0.8222499999999999, 0.909, 0.8194999999999999, 0.7455, 0.784, 0.9642499999999999,
#             0.92425, 0.869, 0.785, 0.9095, 0.90075, 0.919, 0.84075, 0.794, 0.9655, 0.82]
# worst_pgd = [0.6964999999999999, 0.855, 0.84975, 0.92425, 0.8025, 0.477, 0.728, 0.926,
#              0.921, 0.86275, 0.716, 0.9025, 0.91175, 0.90075, 0.8285, 0.75125, 0.96775, 0.783]


if __name__ == '__main__':
    fig = Figure('pgd_cifar100')
    fig.set_axis_label('x', 'Best Success Rate (%)')
    fig.set_axis_label('y', 'Worst Success Rate (%)')
    fig.set_axis_lim('x', lim=[60, 100], piece=4, margin=[1.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[40, 100], piece=3, margin=[1.0, 1.0],
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
