#!/usr/bin/env python3

from alpsplot.utils import group_err_bar

import os
import numpy as np

import matplotlib.figure as figure
from matplotlib import ticker
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.lines import Line2D
from matplotlib.container import BarContainer


# Markers
# '.' point marker
# ',' pixel marker
# 'o' circle marker
# 'v' triangle_down marker
# '^' triangle_up marker
# '<' triangle_left marker
# '>' triangle_right marker
# '1' tri_down marker
# '2' tri_up marker
# '3' tri_left marker
# '4' tri_right marker
# 's' square marker
# 'p' pentagon marker
# '*' star marker
# 'h' hexagon1 marker
# 'H' hexagon2 marker
# '+' plus marker
# 'x' x marker
# 'D' diamond marker
# 'd' thin_diamond marker
# '|' vline marker
# '_' hline marker

# Line Styles
# '-'     solid line style
# '--'    dashed line style
# '-.'    dash-dot line style
# ':'     dotted line style

class Figure:
    """The Figure wrapper class.

    Attributes:
        name (str): Figure name.
        folder_path (str): Figure name. Defaults to `'./output/'`.
        fig (`matplotlib.figure.Figure`, optional): Description of `attr2`.
        ax (`matplotlib.axes.Axes`, optional): Description of `attr2`.
        figsize (tuple[float, float]):
            Passed to :any:`matplotlib.pyplot.figure`
            when :attr:`fig` and :attr:`ax` are not set.
            Recommend to use `(5, 2.5)` for singular plot
            and `(5, 3.75)` for subplots.
            Defaults to `(5, 2.5)`
        **kwargs: Keyword arguments passed to :any:`matplotlib.pyplot.figure`
            when :attr:`fig` and :attr:`ax` are not set.

    """

    def __init__(self, name: str, folder_path: str = './output/',
                 fig: figure.Figure = None, ax: Axes = None,
                 figsize: tuple[float, float] = (5, 2.5), **kwargs):
        self.name: str = name
        self.folder_path: str = folder_path
        self.fig: Figure = fig
        self.ax: Axes = ax
        if fig is None and ax is None:
            self.fig: Figure = plt.figure(figsize=figsize, **kwargs)
            self.ax = self.fig.add_subplot(1, 1, 1)
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['bottom'].set_visible(True)
        self.ax.spines['left'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.ax.grid(axis='y', linewidth=1, alpha=0.5)
        self.ax.set_axisbelow(True)

        self.ax.set_xlim([0.0, 1.0])
        self.ax.set_ylim([0.0, 1.0])

    def save(self, path: str = None, folder_path: str = None,
             ext: str = '.pdf') -> None:
        if path is None:
            if folder_path is None:
                folder_path = self.folder_path
            path = os.path.join(folder_path, f'{self.name}{ext}')
        else:
            folder_path = os.path.dirname(path)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        self.fig.savefig(path, dpi=100, bbox_inches='tight')

    def set_title(self, text: str = None, fontsize: int = 16,
                  fontproperties: str = 'Optima', fontweight: str = 'bold',
                  math_fontfamily: str = 'cm') -> None:
        if text is None:
            text = self.name
        self.ax.set_title(text, fontsize=fontsize,
                          fontproperties=fontproperties, fontweight=fontweight,
                          math_fontfamily=math_fontfamily)

    def set_axis_label(self, axis: str, text: str, fontsize: int = 12,
                       fontproperties: str = 'Optima', fontweight='bold',
                       math_fontfamily: str = 'cm', **kwargs):
        func = getattr(self.ax, f'set_{axis}label')
        func(text, fontsize=fontsize, fontproperties=fontproperties,
             fontweight=fontweight, math_fontfamily=math_fontfamily, **kwargs)

    def set_axis_lim(self, axis: str, labels: list[str] = None,
                     lim: list[float] = [0.0, 1.0],
                     margin: list[float] = [0.0, 0.0],
                     piece: int = 10, _format: str = '%.1f',
                     fontsize: int = 11,
                     fontproperties: str = 'Optima',
                     fontweight: str = 'bold',
                     math_fontfamily: str = 'cm', **kwargs) -> None:
        if _format == 'integer':
            _format = '%d'
        lim_func = getattr(self.ax, f'set_{axis}lim')
        set_ticks_func = getattr(self.ax, f'set_{axis}ticks')

        def format_func(_str):
            getattr(self.ax, f'{axis}axis').set_major_formatter(
                ticker.FormatStrFormatter(_str))
        ticks = np.append(
            np.arange(lim[0], lim[1], (lim[1] - lim[0]) / piece), lim[1])
        final_lim = [lim[0] - margin[0], lim[1] + margin[1]]
        lim_func(final_lim)
        set_ticks_func(ticks)
        set_ticklabels_func = getattr(self.ax, f'set_{axis}ticklabels')
        if labels is None:
            labels = getattr(self.ax, f'get_{axis}ticks')()
            set_ticklabels_func(labels, fontsize=fontsize,
                                fontproperties=fontproperties,
                                fontweight=fontweight,
                                math_fontfamily=math_fontfamily, **kwargs)
            format_func(_format)
        else:
            set_ticklabels_func(labels, fontsize=fontsize,
                                fontproperties=fontproperties,
                                fontweight=fontweight,
                                math_fontfamily=math_fontfamily, **kwargs)

    def set_legend(self, *args, fontsize=11, frameon: bool = True,
                   edgecolor='white', framealpha=1.0,
                   fontproperties: str = 'Optima',
                   fontstyle=None, fontweight='bold',
                   math_fontfamily: str = 'cm', **kwargs) -> None:
        self.ax.legend(*args, frameon=frameon, edgecolor=edgecolor,
                       framealpha=framealpha, **kwargs)
        plt.setp(self.ax.get_legend().get_texts(), fontsize=fontsize,
                 fontproperties=fontproperties,
                 fontstyle=fontstyle, fontweight=fontweight,
                 math_fontfamily=math_fontfamily)

    def lineplot(self, x: np.ndarray, y: np.ndarray,
                 err: np.array = None, err_style: str = 'band',
                 color: str = 'black', alpha: float = 0.0,
                 linewidth: int = 2, linestyle: str = '-',
                 label: str = None, markerfacecolor: str = 'white',
                 zorder: int = 1, **kwargs) -> Line2D:
        # linestyle marker markeredgecolor markeredgewidth
        # markerfacecolor markersize alpha
        if len(set(x)) != len(x):
            assert err is None
            y_dict = group_err_bar(x, y)
            x = np.array(list(y_dict.keys()))
            y = np.array([y_list.mean() for y_list in y_dict.values()])
            err = np.array([y_list.std() for y_list in y_dict.values()])
        if err is not None:
            if err_style == 'band':  # TODO: python 3.10
                self.ax.fill_between(x=x, y1=y-err, y2=y+err,
                                     color=color, alpha=alpha*0.2,
                                     zorder=zorder-0.1)
            elif err_style == 'bars':
                self.ax.errorbar(x=x, y=y, yerr=err,
                                 color=color, alpha=alpha, linestyle="",
                                 zorder=zorder)
        if label is not None:
            self.curve_legend(label=label, color=color,
                              linewidth=linewidth, linestyle=linestyle,
                              **kwargs)
        return self.ax.plot(x, y, color=color, alpha=alpha,
                            linewidth=linewidth, linestyle=linestyle,
                            markerfacecolor=markerfacecolor,
                            zorder=zorder, **kwargs)

    def curve_legend(self, label: str = None, color: str = 'black',
                     linewidth: int = 2, linestyle: str = '-',
                     markerfacecolor: str = 'white', **kwargs) -> Line2D:
        # linestyle marker markeredgecolor markeredgewidth
        # markerfacecolor markersize alpha
        line, = self.ax.plot([], [], label=label, color=color,
                             linewidth=linewidth, linestyle=linestyle,
                             markeredgewidth=linewidth, markeredgecolor=color,
                             markerfacecolor=markerfacecolor,
                             **kwargs)
        return line

    def scatter(self, x: np.ndarray, y: np.ndarray,
                color: str = 'black', linewidth: int = 2,
                label: str = None, curve_legend: bool = False,
                marker: str = 'D', facecolor: str = 'white',
                zorder: int = 3, **kwargs):
        # marker markeredgecolor markeredgewidth
        # markerfacecolor markersize alpha
        if curve_legend and label is not None:
            self.curve_legend(label=label, color=color,
                              linewidth=linewidth, marker=marker, **kwargs)
            label = None
        return self.ax.scatter(x=x, y=y, color=color, linewidth=linewidth,
                               label=label, marker=marker, facecolor=facecolor,
                               zorder=zorder, **kwargs)

    def bar(self, x: np.ndarray, y: np.ndarray,
            color: str = 'black', width: float = 0.2,
            align: str = 'edge', edgecolor: str = 'white',
            label: str = None, **kwargs) -> BarContainer:
        # facecolor edgewidth alpha
        return self.ax.bar(x, y, color=color, width=width,
                           align=align, edgecolor=edgecolor,
                           label=label, **kwargs)

    def bar3d(self, x: np.ndarray, y: np.ndarray, z: np.ndarray,
              color: str = 'black', size: tuple[float, float] = 0.5,
              label: str = None, **kwargs) -> BarContainer:
        # facecolor edgewidth alpha
        if isinstance(size, (float, int)):
            size = [size, size]
        return self.ax.bar3d(x=x, y=y, z=np.zeros_like(x),
                             dx=np.ones_like(x) * size[0],
                             dy=np.ones_like(y) * size[1],
                             dz=z, color=color, label=label,
                             **kwargs)

    def hist(self, x: np.ndarray, bins: int = None,
             density: bool = True, **kwargs):
        return self.ax.hist(x, bins=bins, density=density, **kwargs)

    def autolabel(self, rects: BarContainer, above: bool = True,
                  fontsize: int = 6,
                  fontproperties: str = 'Optima', fontweight: str = 'bold',
                  math_fontfamily: str = 'cm') -> None:
        r"""
        Attach a text label above each bar in *rects*, displaying its height.
        """
        for rect in rects:
            height = int(rect.get_height())
            offset = 3 if above else -13
            self.ax.annotate(f'{int(abs(height)):d}',
                             xy=(rect.get_x() + rect.get_width() / 2, height),
                             xytext=(0, offset),  # 3 points vertical offset
                             textcoords="offset points",
                             ha='center', va='bottom', fontsize=fontsize,
                             fontproperties=fontproperties,
                             fontweight=fontweight,
                             math_fontfamily=math_fontfamily)
