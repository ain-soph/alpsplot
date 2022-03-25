#!/usr/bin/env python3

r"""
`Linestyles`_
==============

..  _Linestyles: https://matplotlib.org/stable/api/_as_gen/
    matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle

===============================   =================
Linestyle                         Description
===============================   =================
``'-'`` or ``'solid'``            solid line
``'--'`` or  ``'dashed'``         dashed line
``'-.'`` or  ``'dashdot'``        dash-dotted line
``':'`` or ``'dotted'``           dotted line
``'None'`` or ``' '`` or ``''``   draw nothing
===============================   =================


`Markers`_
=============

..  _Markers: https://matplotlib.org/stable/api/markers_api.html

============================== ====== =========================================
marker                         symbol description
============================== ====== =========================================
``"."``                        |m00|  point
``","``                        |m01|  pixel
``"o"``                        |m02|  circle
``"v"``                        |m03|  triangle_down
``"^"``                        |m04|  triangle_up
``"<"``                        |m05|  triangle_left
``">"``                        |m06|  triangle_right
``"1"``                        |m07|  tri_down
``"2"``                        |m08|  tri_up
``"3"``                        |m09|  tri_left
``"4"``                        |m10|  tri_right
``"8"``                        |m11|  octagon
``"s"``                        |m12|  square
``"p"``                        |m13|  pentagon
``"P"``                        |m23|  plus (filled)
``"*"``                        |m14|  star
``"h"``                        |m15|  hexagon1
``"H"``                        |m16|  hexagon2
``"+"``                        |m17|  plus
``"x"``                        |m18|  x
``"X"``                        |m24|  x (filled)
``"D"``                        |m19|  diamond
``"d"``                        |m20|  thin_diamond
``"|"``                        |m21|  vline
``"_"``                        |m22|  hline
``0`` (``TICKLEFT``)           |m25|  tickleft
``1`` (``TICKRIGHT``)          |m26|  tickright
``2`` (``TICKUP``)             |m27|  tickup
``3`` (``TICKDOWN``)           |m28|  tickdown
``4`` (``CARETLEFT``)          |m29|  caretleft
``5`` (``CARETRIGHT``)         |m30|  caretright
``6`` (``CARETUP``)            |m31|  caretup
``7`` (``CARETDOWN``)          |m32|  caretdown
``8`` (``CARETLEFTBASE``)      |m33|  caretleft (centered at base)
``9`` (``CARETRIGHTBASE``)     |m34|  caretright (centered at base)
``10`` (``CARETUPBASE``)       |m35|  caretup (centered at base)
``11`` (``CARETDOWNBASE``)     |m36|  caretdown (centered at base)
``"none"`` or ``"None"``              nothing
``" "`` or  ``""``                    nothing
``'$...$'``                    |m37|  Render the string using mathtext.
                                      E.g ``"$f$"`` for marker showing the
                                      letter ``f``.
``verts``                             A list of (x, y) pairs used for Path
                                      vertices. The center of the marker is
                                      located at (0, 0) and the size is
                                      normalized, such that the created path
                                      is encapsulated inside the unit cell.
path                                  A :any:`Path <matplotlib.path.Path>`
                                      instance.
``(numsides, 0, angle)``              A regular polygon with ``numsides``
                                      sides, rotated by ``angle``.
``(numsides, 1, angle)``              A star-like symbol with ``numsides``
                                      sides, rotated by ``angle``.
``(numsides, 2, angle)``              An asterisk with ``numsides`` sides,
                                      rotated by ``angle``.
============================== ====== =========================================

.. |m00| image:: https://matplotlib.org/stable/_images/m00.png
.. |m01| image:: https://matplotlib.org/stable/_images/m01.png
.. |m02| image:: https://matplotlib.org/stable/_images/m02.png
.. |m03| image:: https://matplotlib.org/stable/_images/m03.png
.. |m04| image:: https://matplotlib.org/stable/_images/m04.png
.. |m05| image:: https://matplotlib.org/stable/_images/m05.png
.. |m06| image:: https://matplotlib.org/stable/_images/m06.png
.. |m07| image:: https://matplotlib.org/stable/_images/m07.png
.. |m08| image:: https://matplotlib.org/stable/_images/m08.png
.. |m09| image:: https://matplotlib.org/stable/_images/m09.png
.. |m10| image:: https://matplotlib.org/stable/_images/m10.png
.. |m11| image:: https://matplotlib.org/stable/_images/m11.png
.. |m12| image:: https://matplotlib.org/stable/_images/m12.png
.. |m13| image:: https://matplotlib.org/stable/_images/m13.png
.. |m14| image:: https://matplotlib.org/stable/_images/m14.png
.. |m15| image:: https://matplotlib.org/stable/_images/m15.png
.. |m16| image:: https://matplotlib.org/stable/_images/m16.png
.. |m17| image:: https://matplotlib.org/stable/_images/m17.png
.. |m18| image:: https://matplotlib.org/stable/_images/m18.png
.. |m19| image:: https://matplotlib.org/stable/_images/m19.png
.. |m20| image:: https://matplotlib.org/stable/_images/m20.png
.. |m21| image:: https://matplotlib.org/stable/_images/m21.png
.. |m22| image:: https://matplotlib.org/stable/_images/m22.png
.. |m23| image:: https://matplotlib.org/stable/_images/m23.png
.. |m24| image:: https://matplotlib.org/stable/_images/m24.png
.. |m25| image:: https://matplotlib.org/stable/_images/m25.png
.. |m26| image:: https://matplotlib.org/stable/_images/m26.png
.. |m27| image:: https://matplotlib.org/stable/_images/m27.png
.. |m28| image:: https://matplotlib.org/stable/_images/m28.png
.. |m29| image:: https://matplotlib.org/stable/_images/m29.png
.. |m30| image:: https://matplotlib.org/stable/_images/m30.png
.. |m31| image:: https://matplotlib.org/stable/_images/m31.png
.. |m32| image:: https://matplotlib.org/stable/_images/m32.png
.. |m33| image:: https://matplotlib.org/stable/_images/m33.png
.. |m34| image:: https://matplotlib.org/stable/_images/m34.png
.. |m35| image:: https://matplotlib.org/stable/_images/m35.png
.. |m36| image:: https://matplotlib.org/stable/_images/m36.png
.. |m37| image:: https://matplotlib.org/stable/_images/m37.png
"""

from alpsplot.utils import group_err_bar

from matplotlib import ticker
from matplotlib import pyplot as plt

import os
import numpy as np

from typing import Sequence, Union
from typing import TYPE_CHECKING
if TYPE_CHECKING:    # TODO: python 3.11
    import matplotlib.figure as figure
    from matplotlib.axes import Axes
    from matplotlib.axis import Axis
    from matplotlib.lines import Line2D
    from matplotlib.container import BarContainer
    from matplotlib.collections import PathCollection

# TODO: We could use default values after matplotlib 3.5.0
# https://github.com/matplotlib/matplotlib/pull/20101

__all__ = ['Figure']


class Figure:
    r"""The Figure wrapper class.

    Args:
        name (str): Figure name used as default value of
            :meth:`save` and :meth:`set_title`.
        folder_path (str): Folder path used as default value of :meth:`save`.
            Defaults to ``'./output/'``.
        fig (~matplotlib.figure.Figure, optional): The pre-defined Figure.
            Otherwise, call :any:`pyplot.figure() <matplotlib.pyplot.figure>`
            to generate. Defaults to ``None``.
        ax (~matplotlib.axes.Axes, optional): The pre-defined Axes.
            Otherwise, call :any:`pyplot.figure() <matplotlib.pyplot.figure>`
            to generate. Defaults to ``None``.
        figsize (tuple[float, float]):
            Passed to :any:`pyplot.figure() <matplotlib.pyplot.figure>`
            when :attr:`fig` and :attr:`ax` are not set.
            Recommend to use ``(5, 2.5)`` for singular plot
            and ``(5, 3.75)`` for subplots.
            Defaults to ``(5, 2.5)``
        **kwargs: Keyword arguments passed to
            :any:`pyplot.figure() <matplotlib.pyplot.figure>`
            when :attr:`fig` and :attr:`ax` are not set.

    Attributes:
        name (str): Figure name used as default value of
            :meth:`save` and :meth:`set_title`.
        folder_path (str): Folder path used as default value of :meth:`save`.
            Defaults to ``'./output/'``.
        fig (~matplotlib.figure.Figure): Figure object.
        ax (~matplotlib.axes.Axes): Axes object.
    """

    def __init__(self, name: str = 'figure', folder_path: str = './output/',
                 fig: 'figure.Figure' = None, ax: 'Axes' = None,
                 figsize: tuple[float, float] = (5, 2.5), **kwargs):
        self.name: str = name
        self.folder_path: str = folder_path
        if fig is None and ax is None:
            fig: 'figure.Figure' = plt.figure(figsize=figsize, **kwargs)
            ax = fig.add_subplot(1, 1, 1)
        self.fig: 'figure.Figure' = fig
        self.ax: 'Axes' = ax
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['bottom'].set_visible(True)
        self.ax.spines['left'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.ax.grid(axis='y', linewidth=1, alpha=0.5)
        self.ax.set_axisbelow(True)

    def save(self, path: str = None,
             folder_path: str = None, filename: str = None,
             name: str = None, ext: str = '.pdf',
             dpi: int = 100, bbox_inches: str = 'tight',
             **kwargs):
        r"""Class methods are similar to regular functions.

        Args:
            path (str, optional): The file path to save the figure.
                Defaults to ``f'{folder_path}/{filename}'``.
            folder_path (str, optional): Called when :attr:`path` is ``None``.
                Defaults to :attr:`~self.folder_path`.
            folder_path (str, optional): Called when :attr:`path` is ``None``.
                Defaults to ``f'{name}{ext}'``.
            name (str, optional): Called when :attr:`path` is ``None``.
                Defaults to :attr:`self.name`.
            ext (str): Called when :attr:`path` is ``None``.
                Defaults to ``'.pdf'``.
            dpi (int): Passed to
                :any:`Figure.savefig() <matplotlib.figure.Figure.savefig>`.
                Defaults to ``100``.
            bbox_inches (str): Passed to
                :any:`Figure.savefig() <matplotlib.figure.Figure.savefig>`.
                Defaults to ``'tight'``.
            **kwargs: Keyword arguments passed to
                :any:`Figure.savefig() <matplotlib.figure.Figure.savefig>`.

        :Example:
            .. code-block:: python
                :emphasize-lines: 17

                import numpy as np
                from alpsplot.figure import Figure

                fig = Figure('save')
                fig.set_axis_lim('x', lim=(0.0, 10.0),
                                 margin=(0.5, 0.0),
                                 piece=5, _format='%d')
                fig.set_axis_lim('y', lim=(0.0, 10.0),
                                 margin=(0.5, 0.0),
                                 piece=5, _format='%d')

                x = np.arange(10, step=0.5)
                y = np.arange(10, step=0.5)
                fig.lineplot(x, y, color='red', label='save')

                fig.set_legend()
                fig.save(ext='.svg')  # './output/save.svg'

            .. image:: /images/figure/save.svg
                :width: 60%
        """
        if path is None:
            folder_path = folder_path or self.folder_path
            if filename is None:
                name = name or self.name
                ext = ext if ext.startswith('.') else '.' + ext
                filename = f'{name}{ext}'
            path = os.path.join(folder_path, filename)
        else:
            folder_path = os.path.dirname(path)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        self.fig.savefig(path, dpi=dpi, bbox_inches=bbox_inches, **kwargs)

    def set_title(self, text: str = None, **kwargs):
        r"""Call :any:`Axes.set_title() <matplotlib.axes.Axes.set_title>`.

        Args:
            text (str, optional): The text of title.
                Defaults to :attr:`self.name`.
            **kwargs: Keyword arguments passed to
                :any:`Axes.set_title() <matplotlib.axes.Axes.set_title>`.

        Returns:
            ~matplotlib.text.Text:
                The matplotlib text instance representing the title.

        :Example:
            .. code-block:: python
                :emphasize-lines: 5

                import numpy as np
                from alpsplot.figure import Figure

                fig = Figure('set_title')
                fig.set_title('A New Title')
                fig.save(ext='.svg')  # './output/set_title.svg'

            .. image:: /images/figure/set_title.svg
                :width: 60%
        """
        text = self.name if text is None else text
        return self.ax.set_title(text, **kwargs)

    def set_axis_label(self, axis: str, text: str, **kwargs):
        r"""Call :any:`Axes.set_xlabel() <matplotlib.axes.Axes.set_xlabel>`
        or :any:`Axes.set_ylabel() <matplotlib.axes.Axes.set_ylabel>`.

        Args:
            axis (str): The axis to set label.
                Possible values: ``['x', 'y', 'z']``.
            text (str): The text of axis label.
            **kwargs: Keyword arguments passed to
                :any:`Axes.set_xlabel() <matplotlib.axes.Axes.set_xlabel>`
                or :any:`Axes.set_ylabel() <matplotlib.axes.Axes.set_ylabel>`.

        Returns:
            ~matplotlib.text.Text:
                The matplotlib text instance representing the axis label.

        :Example:
            .. code-block:: python
                :emphasize-lines: 5-6

                import numpy as np
                from alpsplot.figure import Figure

                fig = Figure('set_axis_label')
                fig.set_axis_label('x', 'x label')
                fig.set_axis_label('y', 'y label')
                fig.save(ext='.svg')  # './output/set_axis_label.svg'

            .. image:: /images/figure/set_axis_label.svg
                :width: 60%
        """
        func = getattr(self.ax, f'set_{axis}label')
        return func(text, **kwargs)

    def set_axis_lim(self, axis: str, labels: list[str] = None,
                     lim: tuple[float, float] = (0.0, 1.0),
                     margin: tuple[float, tuple] = (0.0, 0.0),
                     piece: int = 10, _format: str = None,
                     **kwargs):
        r"""Set ticks and their labels for axis.

        .. table::
            :widths: auto

            +--------------------+-------------------------------------------------------------------------+
            | ``set_lim``        | :any:`Axes.set_xlim() <matplotlib.axes.Axes.set_xlim>`                  |
            |                    | or :any:`Axes.set_ylim() <matplotlib.axes.Axes.set_ylim>`               |
            +--------------------+-------------------------------------------------------------------------+
            | ``set_ticks``      | :any:`Axes.set_xticks() <matplotlib.axes.Axes.set_xticks>`              |
            |                    | or :any:`Axes.set_yticks() <matplotlib.axes.Axes.set_yticks>`           |
            +--------------------+-------------------------------------------------------------------------+
            | ``set_ticklabels`` | :any:`Axes.set_xticklabels() <matplotlib.axes.Axes.set_xticklabels>`    |
            |                    | or :any:`Axes.set_yticklabels() <matplotlib.axes.Axes.set_yticklabels>` |
            +--------------------+-------------------------------------------------------------------------+

        .. parsed-literal::
            set_lim(lim[0] - margin[0], lim[1] + margin[1])
            set_ticks(lim[0], lim[0] + :math:`\frac{1}{\text{lim}[1] - \text{lim}[0]}`, :math:`\dots`, lim[1])
            if labels is not None:
                set_ticklabels(labels, \*\*kwargs)
            elif _format is not None:
                format_str = :any:`ticker.FormatStrFormatter <matplotlib.ticker.FormatStrFormatter>`\(_format)
                :any:`Axis.set_major_formatter <matplotlib.axis.Axis.set_major_formatter>`\(format_str)

        Args:
            axis (str): The axis to set label.
                Possible values: ``['x', 'y', 'z']``.
            labels (list[str]): The text of axis tick labels.
                Defaults to ``None``.
            lim (tuple[str, str]): The limit of axis ticks.
                Defaults to ``(0.0, 1.0)``.
            margin (tuple[str, str]): The margin at
                head and tail of axis ticks.
                Defaults to ``(0.0, 0.0)``.
            piece (int): The number of axis ticks - 1.
                The interval among ticks are
                :math:`\frac{\text{lim}[1] - \text{lim}[0]}{\text{piece}}`.
                Defaults to ``10``.
            _format (str): The format of tick labels used in
                :any:`ticker.FormatStrFormatter <matplotlib.ticker.FormatStrFormatter>`
                (e.g., '%.1f' or '%d').
                Defaults to ``None``.
            **kwargs: Keyword arguments passed to
                :any:`Axes.set_xticklabels()
                <matplotlib.axes.Axes.set_xticklabels>`
                or :any:`Axes.set_yticklabels()
                <matplotlib.axes.Axes.set_yticklabels>`.

        :Example:
            .. code-block:: python
                :emphasize-lines: 5-10

                import numpy as np
                from alpsplot.figure import Figure

                fig = Figure('set_axis_lim')
                fig.set_axis_lim('x', lim=(2.0, 3.0),
                                 piece=2, _format='%.2f')
                fig.set_axis_lim('y', labels=['l1', 'l2', 'l3'],
                                 lim=(0.0, 4.0),
                                 margin=(2.0, 2.0),
                                 piece=2, _format='%d')
                fig.save(ext='.svg')  # './output/set_axis_lim.svg'

            .. image:: /images/figure/set_axis_lim.svg
                :width: 60%

        """  # noqa: E501
        final_lim = lim[0] - margin[0], lim[1] + margin[1]
        ticks = np.append(
            np.arange(lim[0], lim[1], (lim[1] - lim[0]) / piece), lim[1])
        getattr(self.ax, f'set_{axis}lim')(*final_lim)
        getattr(self.ax, f'set_{axis}ticks')(ticks)
        if labels is not None:
            set_ticklabels_func = getattr(self.ax, f'set_{axis}ticklabels')
            set_ticklabels_func(labels, **kwargs)
        elif _format is not None:
            target_axis: Axis = getattr(self.ax, f'{axis}axis')
            target_axis.set_major_formatter(
                ticker.FormatStrFormatter(_format))

    def set_legend(self, *args, frameon: bool = None,
                   framealpha: float = 1.0,
                   edgecolor: str = 'none',
                   **kwargs) -> None:
        r"""Call :any:`Axes.legend() <matplotlib.axes.Axes.legend>`
        to set legend of :attr:`self.ax`.

        Args:
            *args: Passed to :any:`Axes.legend()
                <matplotlib.axes.Axes.legend>`.
            frameon (bool): Whether the legend
                should be drawn on a patch (frame).
                Defaults to ``rcParams["legend.frameon"]=True``.
            framealpha (float): The alpha transparency
                of the legend's background.
                If shadow is activated and framealpha is None,
                the default value is ignored.
                Defaults to ``0.0``.
            edgecolor (str): The legend's background patch edge color.
                Defaults to ``'none'``.
            **kwargs: Keyword arguments passed to
                :any:`Axes.legend() <matplotlib.axes.Axes.legend>`.

        Returns:
            ~matplotlib.legend.Legend: The matplotlib legend instance.

        :Example:
            .. code-block:: python
                :emphasize-lines: 16

                import numpy as np
                from alpsplot.figure import Figure

                fig = Figure('set_legend')
                fig.set_axis_lim('x', lim=(0.0, 10.0),
                                 margin=(0.5, 0.0),
                                 piece=5, _format='%d')
                fig.set_axis_lim('y', lim=(0.0, 10.0),
                                 margin=(0.5, 0.0),
                                 piece=5, _format='%d')

                x = np.arange(10, step=0.5)
                y = np.arange(10, step=0.5)
                fig.lineplot(x, y, color='red', label='set_legend')

                fig.set_legend()
                fig.save(ext='.svg')  # './output/set_legend.svg'

            .. image:: /images/figure/set_legend.svg
                :width: 60%
        """
        legend = self.ax.legend(*args, frameon=frameon, edgecolor=edgecolor,
                                framealpha=framealpha, **kwargs)
        return legend

    def lineplot(self, x: np.ndarray, y: np.ndarray,
                 err: np.array = None, err_style: str = 'band',
                 color: str = 'black', alpha: float = 1.0,
                 linewidth: int = 2, linestyle: str = '-',
                 label: str = None, markerfacecolor: str = 'white',
                 zorder: float = 1, **kwargs) -> 'Line2D':
        r"""A similar implementation to :any:`seaborn.lineplot() <seaborn.lineplot>`.
        same x value with different y values will result in
        the error band/bar at that x.

        Args:
            x (numpy.ndarray): The x array.
            y (numpy.ndarray): The y array.
            err (numpy.ndarray): The x array. Defaults to ``None``.
            err_style (str): Whether to draw the confidence intervals
                with translucent error bands or discrete error bars.
                Possible values: ``['band', 'bars']``
                Defaults to ``'band'``.

        ..

        Args:
            color (str): Set the color of the line.
                Defaults to ``'black'``.
            alpha (float): Set the alpha value used for blending
                - not supported on all backends.
                It must be within the 0-1 range.
                Defaults to ``1.0``.
            linewidth (str): Set the line width in points.
                Defaults to ``2``.
            linestyle (str): Set the linestyle of the line.
                Defaults to ``'-'``.
            label (str): Set a label that will be displayed in the legend.
                Defaults to ``None``.
            markerfacecolor (str): Set the marker face color.
                Defaults to ``'white'``.
            zorder (float): Set the zorder for the artist.
                Artists with lower zorder values are drawn first.
                Defaults to ``1``.
            **kwargs: Keyword arguments passed to
                :any:`Axes.plot() <matplotlib.axes.Axes.plot>`.

        Returns:
            list[matplotlib.lines.Line2D]:
                A list of lines representing the plotted data.

        :Example:
            .. code-block:: python
                :emphasize-lines: 14, 20, 25-26

                import numpy as np
                from alpsplot.figure import Figure

                fig = Figure('lineplot')
                fig.set_axis_lim('x', lim=(0.0, 10.0),
                                 margin=(0.5, 0.0),
                                 piece=5, _format='%d')
                fig.set_axis_lim('y', lim=(0.0, 10.0),
                                 margin=(0.5, 0.0),
                                 piece=5, _format='%d')

                x = np.arange(10, step=0.5)
                y = np.arange(10, step=0.5)
                fig.lineplot(x, y, color='red', label='plain')

                x_err = np.concatenate((x, x, x))
                noise = np.random.randn(20)
                y_mean = y / 2
                y_err = np.concatenate((y_mean-noise, y_mean, y_mean+noise))
                fig.lineplot(x_err, y_err, color='green', label='error band')

                noise = np.random.randn(20)
                y_mean = y / 2 + 4
                y_err = np.concatenate((y_mean-noise, y_mean, y_mean+noise))
                fig.lineplot(x_err, y_err, color='blue', label='error bar',
                             err_style='bars')

                fig.set_legend()
                fig.save(ext='.svg')  # './output/lineplot.svg'

            .. image:: /images/figure/lineplot.svg
                :width: 60%
        """
        if len(set(x)) != len(x):
            assert err is None
            y_dict = group_err_bar(x, y)
            x = np.array(list(y_dict.keys()))
            y = np.array([y_list.mean() for y_list in y_dict.values()])
            err = np.array([y_list.std() for y_list in y_dict.values()])
        if err is not None:
            match err_style:
                case 'band':
                    self.ax.fill_between(x=x, y1=y - err, y2=y + err,
                                         color=color, alpha=alpha * 0.2,
                                         zorder=zorder)
                case 'bars':
                    self.ax.errorbar(x=x, y=y, yerr=err,
                                     color=color, alpha=alpha, linestyle="",
                                     zorder=zorder)
                case _:
                    raise ValueError(f'{err_style=}')
        return self.ax.plot(x, y, color=color, alpha=alpha,
                            linewidth=linewidth, linestyle=linestyle,
                            label=label, markerfacecolor=markerfacecolor,
                            zorder=zorder, **kwargs)

    def curve_legend(self, label: str = None, color: str = 'black',
                     linewidth: int = 2, linestyle: str = '-',
                     markerfacecolor: str = 'white', **kwargs) -> 'Line2D':
        r"""Call :any:`Axes.plot() <matplotlib.axes.Axes.plot>`
        to plot an empty line for legend,

        which is helpful for setting marker-with-line
        legend of :meth:`scatter`.

        Args:
            label (str): Set a label that will be displayed in the legend.
                Defaults to ``None``.
            color (str): Set the color of the line.
                Defaults to ``'black'``.
            linewidth (str): Set the line width in points.
                Defaults to ``2``.
            linestyle (str): Set the linestyle of the line.
                Defaults to ``'-'``.
            markerfacecolor (str): Set the marker face color.
                Defaults to ``'white'``.
            **kwargs: Keyword arguments passed to
                :any:`Axes.plot() <matplotlib.axes.Axes.plot>`.

        Returns:
            ~matplotlib.lines.Line2D: An invisible line object.

        :Example:
            .. code-block:: python
                :emphasize-lines: 5-6

                import numpy as np
                from alpsplot.figure import Figure

                fig = Figure('curve_legend')
                fig.curve_legend(color='red', marker='D',
                                 label='curve_legend')
                fig.set_legend()
                fig.save(ext='.svg')  # './output/curve_legend.svg'

            .. image:: /images/figure/curve_legend.svg
                :width: 60%
        """
        line, = self.ax.plot([], [], label=label, color=color,
                             linewidth=linewidth, linestyle=linestyle,
                             markeredgewidth=linewidth, markeredgecolor=color,
                             markerfacecolor=markerfacecolor,
                             **kwargs)
        return line

    def scatter(self, x: np.ndarray, y: np.ndarray,
                color: str = 'black', linewidth: int = 2,
                marker: str = 'D', facecolor: str = 'white',
                label: str = None, curve_legend: bool = False,
                zorder: float = 3, **kwargs) -> 'PathCollection':
        r"""Call :any:`Axes.scatter() <matplotlib.axes.Axes.scatter>`
        to plot scatters.

        Args:
            x (numpy.ndarray): The x array.
            y (numpy.ndarray): The y array.
            color (str): Set the color of the line.
                Defaults to ``'black'``.
            linewidth (str): Set the line width in points.
                Defaults to ``2``.
            marker (str): The marker style.
                Defaults to ``'D'``.
            facecolor (str): Set the marker face color.
                Defaults to ``'white'``.
            label (str): Set a label that will be displayed in the legend.
                Defaults to ``None``.
            curve_legend (bool): Whether the legend contains
                a line around the marker.
                Defaults to ``False``.
            zorder (float): Set the zorder for the artist.
                Artists with lower zorder values are drawn first.
                Defaults to ``3``.
            **kwargs: Keyword arguments passed to
                :any:`Axes.scatter() <matplotlib.axes.Axes.scatter>`.

        Returns:
            ~matplotlib.collections.PathCollection: A collection of Paths.

        :Example:
            .. code-block:: python
                :emphasize-lines: 14-16

                import numpy as np
                from alpsplot.figure import Figure

                fig = Figure('scatter')
                fig.set_axis_lim('x', lim=(0.0, 10.0),
                                 margin=(0.5, 0.0),
                                 piece=5, _format='%d')
                fig.set_axis_lim('y', lim=(0.0, 10.0),
                                 margin=(0.5, 0.0),
                                 piece=5, _format='%d')

                x = np.arange(10, step=0.5)
                y = np.arange(10, step=0.5)
                fig.scatter(x, y, color='red', label='plain')
                fig.scatter(x, y/2, color='green', label='curve_legend',
                            marker='s', curve_legend=True)

                fig.set_legend()
                fig.save(ext='.svg')  # './output/scatter.svg'

            .. image:: /images/figure/scatter.svg
                :width: 60%
        """
        if curve_legend and label is not None:
            self.curve_legend(label=label, color=color,
                              linewidth=linewidth, marker=marker, **kwargs)
            label = None
        return self.ax.scatter(x=x, y=y, color=color, linewidth=linewidth,
                               marker=marker, facecolor=facecolor, label=label,
                               zorder=zorder, **kwargs)

    def bar(self, x: np.ndarray, y: np.ndarray, width: float = 0.8,
            color: str = 'black', edgecolor: str = 'white',
            align: str = 'edge', linewidth: int = 1,
            label: str = None, **kwargs) -> 'BarContainer':
        r"""Call :any:`Axes.bar() <matplotlib.axes.Axes.bar>`
        to plot bars.

        Args:
            x (numpy.ndarray): The x array.
            y (numpy.ndarray): The y array.
            width (float): The width of the bars.
                Defaults to ``0.8``.
            color (str): The colors of the bar faces.
                Defaults to ``'black'``.
            edgecolor (str): Set the bar edge color.
                Defaults to ``'white'``.
            align (str):
                Alignment of the bars to the ``x`` coordinates.

                Possible values: ``['center', 'edge']``.
                Defaults to ``'edge'``.

                * ``'center'``: Center the base on the x positions.
                * ``'edge'``: Align the left edges of the bars
                  with the ``x`` positions.
            linewidth (float): Width of the bar edges.
                If ``0``, don't draw edges.
                Defaults to ``1``.
            label (str): Set a label that will be displayed in the legend.
                Defaults to ``None``.
            **kwargs: Keyword arguments passed to
                :any:`Axes.bar() <matplotlib.axes.Axes.bar>`.

        Returns:
            ~matplotlib.container.BarContainer:
                Container with all the bars and optionally errorbars.

        :Example:
            .. code-block:: python
                :emphasize-lines: 14-15

                import numpy as np
                from alpsplot.figure import Figure

                fig = Figure('bar')
                fig.set_axis_lim('x', lim=(0.0, 10.0),
                                    margin=(0.5, 0.0),
                                    piece=5, _format='%d')
                fig.set_axis_lim('y', lim=(0.0, 10.0),
                                    margin=(0.5, 0.0),
                                    piece=5, _format='%d')

                x = np.arange(10, step=2)
                y = np.arange(10, step=2)
                fig.bar(x, y, width=1, color='red', label='bar1')
                fig.bar(x+1, y+1, width=1, color='green', label='bar2')
                fig.set_legend()
                fig.save(ext='.svg')  # './output/bar.svg'

            .. image:: /images/figure/bar.svg
                :width: 60%
        """
        return self.ax.bar(x, y, width=width,
                           color=color, edgecolor=edgecolor,
                           linewidth=linewidth, label=label,
                           align=align, **kwargs)

    def hist(self, x: np.ndarray,
             bins: Union[int, Sequence[float], str] = None,
             density: bool = True,
             facecolor: str = 'black', edgecolor: str = 'white',
             linewidth: int = 1, **kwargs):
        r"""Call :any:`Axes.hist() <matplotlib.axes.Axes.hist>`
        to plot a histogram.

        Args:
            x (numpy.ndarray): The x array.
            bins (int | ~typing.Sequence[int] | str): Defaults to be ``None``.

                * :class:`int`: it defines the number of
                  equal-width bins in the range.
                * :class:`~typing.Sequence`: it defines the bin edges,
                  including the left edge of the first bin
                  and the right edge of the last bin.

                  In this case, bins may be unequally spaced.
                  All but the last (righthand-most) bin is half-open.

                  .. note::

                    If bins is: ``[1, 2, 3, 4]``,
                    then the first bin is ``[1, 2)``
                    (including 1, but excluding 2)
                    and the second ``[2, 3)``.
                    The last bin, however,
                    is ``[3, 4]``, which includes 4.

                * :class:`str`: it is one of the binning strategies
                  supported by :any:`numpy.histogram_bin_edges`:

                  ``['auto', 'fd', 'doane', 'scott',
                  'stone', 'rice', 'sturges', 'sqrt']``.
            density (bool): Defaults to be ``False``.
                If ``True``, draw and return a probability density.

                Each bin will display the bin's raw count
                divided by the total number of counts
                and the bin width:

                ``density = counts / (sum(counts) * np.diff(bins))``,

                so that the area under the histogram integrates to 1:

                ``np.sum(density * np.diff(bins)) == 1``.

                .. note::

                    If stacked is also True,
                    the sum of the histograms is normalized to 1.

            **kwargs: Keyword arguments passed to
                :any:`Axes.hist() <matplotlib.axes.Axes.hist>`.

        Returns:
            ~matplotlib.container.BarContainer:
                Container with all the bars and optionally errorbars.

        :Example:
            .. code-block:: python
                :emphasize-lines: 13-14

                import numpy as np
                from alpsplot.figure import Figure

                fig = Figure('hist')
                fig.set_axis_lim('x', lim=(-2.0, 2.0),
                                    margin=(0.1, 0.1),
                                    piece=4, _format='%d')
                fig.set_axis_lim('y', lim=(0.0, 1.0),
                                    margin=(0.0, 0.1),
                                    piece=4, _format='%.2f')

                x = np.random.randn(1000)
                fig.hist(x, range=(-2,2), bins=8,
                         facecolor='red', label='hist')
                fig.set_legend()
                fig.save(ext='.svg')  # './output/hist.svg'

            .. image:: /images/figure/hist.svg
                :width: 60%
        """
        return self.ax.hist(x, bins=bins, density=density,
                            facecolor=facecolor, edgecolor=edgecolor,
                            linewidth=linewidth, **kwargs)

    def autolabel(self, rects: 'BarContainer',
                  offset: float = None, above: bool = True,
                  fontsize: int = 7, **kwargs) -> None:
        r"""Call :any:`Axes.annotate() <matplotlib.axes.Axes.annotate>`
        to attach a text label above each bar in :attr:`rects`,
        displaying its height.

        Args:
            rects (~matplotlib.container.BarContainer): The bar rectangles
                to annotate.
            offset (float) = The offset of texts from rects.
                If ``None``, it would be ``3 if above else -13``.
                Defaults to ``None``.
            above (bool): Whether to put the text above the rects.
                Defaults to ``True``.
            fontsize (int): The fontsize of text.
                Defaults to ``7``.
            **kwargs: Keyword arguments passed to
                :any:`Axes.annotate() <matplotlib.axes.Axes.annotate>`.

        :Example:
            .. code-block:: python
                :emphasize-lines: 17-18

                import numpy as np
                from alpsplot.figure import Figure

                fig = Figure('autolabel')
                fig.set_axis_lim('x', lim=(0.0, 10.0),
                                    margin=(0.5, 0.0),
                                    piece=5, _format='%d')
                fig.set_axis_lim('y', lim=(0.0, 10.0),
                                    margin=(0.5, 0.0),
                                    piece=5, _format='%d')

                x = np.arange(10, step=2)
                y = np.arange(10, step=2)
                rects1 = fig.bar(x, y, width=1, color='red', label='bar1')
                rects2 = fig.bar(x+1, y+1, width=1,
                                    color='green', label='bar2')
                fig.autolabel(rects1)
                fig.autolabel(rects2, above=False)
                fig.set_legend()
                fig.save(ext='.svg')  # './output/autolabel.svg'

            .. image:: /images/figure/autolabel.svg
                :width: 60%
        """
        if offset is None:
            offset = 3 if above else -13
        for rect in rects:
            height = int(rect.get_height())
            self.ax.annotate(f'{int(abs(height)):d}',
                             xy=(rect.get_x() + rect.get_width() / 2, height),
                             xytext=(0, offset),  # 3 points vertical offset
                             textcoords="offset points",
                             ha='center', va='bottom',
                             fontsize=fontsize, **kwargs)

    # def bar3d(self, x: np.ndarray, y: np.ndarray, z: np.ndarray,
    #           color: str = 'black', size: tuple[float, float] = 0.5,
    #           label: str = None, **kwargs) -> 'BarContainer':
    #     # facecolor edgewidth alpha
    #     if isinstance(size, (float, int)):
    #         size = [size, size]
    #     return self.ax.bar3d(x=x, y=y, z=np.zeros_like(x),
    #                          dx=np.ones_like(x) * size[0],
    #                          dy=np.ones_like(y) * size[1],
    #                          dz=z, color=color, label=label,
    #                          **kwargs)
