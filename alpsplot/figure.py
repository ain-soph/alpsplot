#!/usr/bin/env python3

from .fonts import add_palatino

import os
import numpy as np

import matplotlib.ticker as ticker
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.lines import Line2D
from matplotlib.container import BarContainer
import seaborn

add_palatino()
matplotlib.rc('mathtext', fontset='cm')
matplotlib.rc('pdf', fonttype=42)
matplotlib.rc('ps', fonttype=42)
matplotlib.rc('svg', image_inline=True, fonttype='none')


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
    def __init__(self, name: str, folder_path: str = None, fig: Figure = None, ax: Axes = None, figsize: tuple[float, float] = (5, 2.5), **kwargs):
        super(Figure, self).__init__()
        self.name: str = name
        self.folder_path: str = folder_path
        if folder_path is None:
            self.folder_path = './output/'
        self.fig: Figure = fig
        self.ax: Axes = ax
        if fig is None and ax is None:
            self.fig: Figure = plt.figure(figsize=figsize, **kwargs)
            self.ax = self.fig.add_subplot(1, 1, 1)
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['bottom'].set_visible(True)
        self.ax.spines['left'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.ax.grid(axis='y', linewidth=1)
        self.ax.set_axisbelow(True)

        self.ax.set_xlim([0.0, 1.0])
        self.ax.set_ylim([0.0, 1.0])

    def save(self, path: str = None, folder_path: str = None, ext: str = '.pdf') -> None:
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
                  fontproperties: str = 'Palatino', fontweight: str = 'bold', math_fontfamily: str = 'cm') -> None:
        if text is None:
            text = self.name
        self.ax.set_title(text, fontsize=fontsize,
                          fontproperties=fontproperties, fontweight=fontweight, math_fontfamily=math_fontfamily)

    def set_axis_label(self, axis: str, text: str, fontsize: int = 12,
                       fontproperties: str = 'Palatino', fontweight='bold', math_fontfamily: str = 'cm', **kwargs):
        func = getattr(self.ax, f'set_{axis}label')
        func(text, fontsize=fontsize, fontproperties=fontproperties,
             fontweight=fontweight, math_fontfamily=math_fontfamily, **kwargs)

    def set_axis_lim(self, axis: str, lim: list[float] = [0.0, 1.0], margin: list[float] = [0.0, 0.0],
                     piece: int = 10, _format: str = '%.1f', fontsize: int = 11,
                     fontproperties: str = 'Palatino', fontweight: str = 'bold', math_fontfamily: str = 'cm') -> None:
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
        ticks = getattr(self.ax, f'get_{axis}ticks')()
        set_ticklabels_func = getattr(self.ax, f'set_{axis}ticklabels')
        set_ticklabels_func(ticks, fontsize=fontsize,
                            fontproperties=fontproperties, fontweight=fontweight, math_fontfamily=math_fontfamily)
        format_func(_format)

    def set_legend(self, *args, fontsize=11, frameon: bool = True, edgecolor='white', framealpha=1.0,
                   fontproperties: str = 'Palatino', fontstyle='italic', fontweight='bold', math_fontfamily: str = 'cm', **kwargs) -> None:
        self.ax.legend(*args, frameon=frameon, edgecolor=edgecolor,
                       framealpha=framealpha, **kwargs)
        plt.setp(self.ax.get_legend().get_texts(), fontsize=fontsize,
                 fontproperties=fontproperties, fontstyle=fontstyle, fontweight=fontweight, math_fontfamily=math_fontfamily)

    def plot(self, x: np.ndarray, y: np.ndarray, color: str = 'black', linewidth: int = 2,
             label: str = None, markerfacecolor: str = 'white', linestyle: str = '-', zorder: int = 1, **kwargs) -> Line2D:
        # linestyle marker markeredgecolor markeredgewidth markerfacecolor markersize alpha
        ax = seaborn.lineplot(x=x, y=y, ax=self.ax, color=color, linewidth=linewidth,
                              markerfacecolor=markerfacecolor, zorder=zorder, **kwargs)
        line: Line2D = ax.get_lines()[-1]
        line.set_linestyle(linestyle)
        if label is not None:
            self.curve_legend(label=label, color=color,
                              linewidth=linewidth, linestyle=linestyle, **kwargs)
        return line

    def curve_legend(self, label: str = None, color: str = 'black', linewidth: int = 2, linestyle: str = '-',
                     markerfacecolor: str = 'white', **kwargs) -> Line2D:
        # linestyle marker markeredgecolor markeredgewidth markerfacecolor markersize alpha
        line, = self.ax.plot([], [], color=color, linewidth=linewidth, markeredgewidth=linewidth, markeredgecolor=color,
                             label=label, markerfacecolor=markerfacecolor, linestyle=linestyle, **kwargs)
        return line

    def scatter(self, x: np.ndarray, y: np.ndarray, color: str = 'black', linewidth: int = 2,
                label: str = None, marker: str = 'D', facecolor: str = 'white', zorder: int = 3, **kwargs):
        # marker markeredgecolor markeredgewidth markerfacecolor markersize alpha
        if label is not None:
            self.curve_legend(label=label, color=color,
                              linewidth=linewidth, marker=marker, **kwargs)
        return self.ax.scatter(x=x, y=y, color=color, linewidth=linewidth, marker=marker, facecolor=facecolor, zorder=zorder, **kwargs)

    def bar(self, x: np.ndarray, y: np.ndarray, color: str = 'black', width: float = 0.2,
            align: str = 'edge', edgecolor: str = 'white', label: str = None, **kwargs) -> BarContainer:
        # facecolor edgewidth alpha
        return self.ax.bar(x, y, color=color, width=width, align=align, edgecolor=edgecolor, label=label, **kwargs)

    def bar3d(self, x: np.ndarray, y: np.ndarray, z: np.ndarray, color: str = 'black', size: tuple[float, float] = 0.5,
              label: str = None, **kwargs) -> BarContainer:
        # facecolor edgewidth alpha
        if isinstance(size, (float, int)):
            size = [size, size]
        return self.ax.bar3d(x=x, y=y, z=np.zeros_like(x),
                             dx=np.ones_like(x) * size[0], dy=np.ones_like(y) * size[1], dz=z,
                             color=color, label=label, **kwargs)

    def hist(self, x: np.ndarray, bins: int = None, density: bool = True, **kwargs):
        return self.ax.hist(x, bins=bins, density=density, **kwargs)

    def autolabel(self, rects: BarContainer, above: bool = True, fontsize: int = 6,
                  fontproperties: str = 'Palatino', fontweight: str = 'bold', math_fontfamily: str = 'cm') -> None:
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = int(rect.get_height())
            offset = 3 if above else -13
            self.ax.annotate(f'{int(abs(height)):d}',
                             xy=(rect.get_x() + rect.get_width() / 2, height),
                             xytext=(0, offset),  # 3 points vertical offset
                             textcoords="offset points",
                             ha='center', va='bottom', fontsize=fontsize,
                             fontproperties=fontproperties, fontweight=fontweight, math_fontfamily=math_fontfamily)
