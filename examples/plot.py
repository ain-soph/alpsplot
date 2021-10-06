#!/usr/bin/env python3

from alpsplot import Figure, ting_color

x = [0, 2.5, 5, 10, 20, 30, 40]
y = [93.78, 93.79, 93.30, 92.16, 90.58, 88.77, 86.13]

if __name__ == '__main__':
    fig = Figure('poison_percent_cifar10')
    fig.set_axis_label('x', 'Poison Percent (%)')
    fig.set_axis_label('y', 'Model Accuracy Drop (%)')
    fig.set_axis_lim('x', lim=[0, 40], piece=4, margin=[1.0, 1.0],
                     _format='%d')
    fig.set_axis_lim('y', lim=[0, 100], piece=5, margin=[1.0, 1.0],
                     _format='%d')

    fig.lineplot(x=x, y=y, color=ting_color['red'])
    fig.scatter(x=x, y=y, color=ting_color['red'],
                marker='H', label='resnet', curve_legend=True)
    fig.set_legend()
    fig.save(folder_path='./result')
