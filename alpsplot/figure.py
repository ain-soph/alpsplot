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

import os
import numpy as np

import matplotlib.figure as figure
from matplotlib import ticker
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.lines import Line2D
from matplotlib.container import BarContainer
from matplotlib.collections import PathCollection
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    pass    # TODO: python 3.10

# TODO: We could use default values after matplotlib 3.5.0
# https://github.com/matplotlib/matplotlib/pull/20101


class Figure:
    r"""The Figure wrapper class.

    Args:
        name (str): Figure name used as default value of
            :meth:`save` and :meth:`set_title`.
        folder_path (str): Figure name used as default value of :meth:`save`.
            Defaults to ``'./output/'``.
        fig (~matplotlib.figure.Figure, optional): The pre-defined Figure.
            Otherwise, call :any:`pyplot.figure() <matplotlib.pyplot.figure>`
            to generate. Defaults to `None`.
        ax (~matplotlib.axes.Axes, optional): The pre-defined Axes.
            Otherwise, call :any:`pyplot.figure() <matplotlib.pyplot.figure>`
            to generate. Defaults to `None`.
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
        folder_path (str): Figure name used as default value of :meth:`save`.
            Defaults to ``'./output/'``.
        fig (~matplotlib.figure.Figure): Figure object.
        ax (~matplotlib.axes.Axes): Axes object.
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

    def save(self, path: str = None,
             folder_path: str = None,
             name: str = None, ext: str = '.pdf',
             dpi: int = 100, bbox_inches: str = 'tight',
             **kwargs):
        r"""Class methods are similar to regular functions.

        Args:
            path (str, optional): The filepath to save the figure.
                Defaults to ``f'{folder_path}/{name}{ext}'``.
            folder_path (str, optional): Called when :attr:`path` is `None`.
                Defaults to :attr:`~self.folder_path`.
            name (str, optional): Called when :attr:`path` is `None`.
                Defaults to :attr:`self.name`.
            ext (str): Called when :attr:`path` is `None`.
                Defaults to ``'.pdf'``.
            dpi (int): Passed to
                :any:`Figure.savefig() <matplotlib.figure.Figure.savefig>`.
                Defaults to `100`.
            bbox_inches (str): Passed to
                :any:`Figure.savefig() <matplotlib.figure.Figure.savefig>`.
                Defaults to `'tight'`.
            **kwargs: Keyword arguments passed to
                :any:`Figure.savefig() <matplotlib.figure.Figure.savefig>`.

        :Example:
            .. code-block:: python
                :emphasize-lines: 17

                import numpy as np
                from alpsplot.figure import Figure

                fig = Figure('test_save')
                fig.set_axis_lim('x', lim=(0.0, 10.0),
                                 margin=(0.5, 0.0),
                                 piece=5, _format='%d')
                fig.set_axis_lim('y', lim=(0.0, 10.0),
                                 margin=(0.5, 0.0),
                                 piece=5, _format='%d')

                x = np.arange(10, step=0.5)
                y = np.arange(10, step=0.5)
                fig.lineplot(x, y, color='red', label='test_save')

                fig.set_legend()
                fig.save(ext='.svg')  # './output/test_save.svg'

            .. image:: /images/figure/test_save.svg
                :width: 60%
        """
        if path is None:
            folder_path = folder_path or self.folder_path
            name = name or self.name
            ext = ext if ext.startswith('.') else '.'+ext
            path = os.path.join(folder_path, f'{name}{ext}')
        else:
            folder_path = os.path.dirname(path)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        self.fig.savefig(path, dpi=dpi, bbox_inches=bbox_inches, **kwargs)

    def set_title(self, text: str = None, fontsize: int = 16,
                  fontproperties: str = 'Optima', fontweight: str = 'bold',
                  math_fontfamily: str = 'cm', **kwargs):
        r"""Call :any:`Axes.set_title() <matplotlib.axes.Axes.set_title>`.

        Args:
            text (str, optional): The text of title.
                Defaults to :attr:`self.name`.

        ..

        Args:
            fontsize (int): The fontsize of text.
                Defaults to `16`.
            fontproperties (str): The font of text.
                Defaults to ``'Optima'``.
            fontweight (str): The fontweight of text.
                Defaults to ``'bold'``.
            math_fontfamily (str): The math_fontfamily of text.
                Defaults to ``'cm'``.
            **kwargs: Keyword arguments passed to
                :any:`Axes.set_title() <matplotlib.axes.Axes.set_title>`.

        :Example:
            .. code-block:: python
                :emphasize-lines: 5

                import numpy as np
                from alpsplot.figure import Figure

                fig = Figure('test_set_title')
                fig.set_title('A New Title')
                fig.save(ext='.svg')  # './output/test_set_title.svg'

            .. image:: /images/figure/test_set_title.svg
                :width: 60%
        """
        text = self.name if text is None else text
        self.ax.set_title(text, fontsize=fontsize,
                          fontproperties=fontproperties, fontweight=fontweight,
                          math_fontfamily=math_fontfamily, **kwargs)

    def set_axis_label(self, axis: str, text: str, fontsize: int = 12,
                       fontproperties: str = 'Optima', fontweight='bold',
                       math_fontfamily: str = 'cm', **kwargs):
        r"""Call :any:`Axes.set_xlabel() <matplotlib.axes.Axes.set_xlabel>`
        or :any:`Axes.set_ylabel() <matplotlib.axes.Axes.set_ylabel>`.

        Args:
            axis (str): The axis to set label.
                Possible values: ``['x', 'y', 'z']``.
            text (str): The text of axis label.

        ..

        Args:
            fontsize (int): The fontsize of text.
                Defaults to `12`.
            fontproperties (str): The font of text.
                Defaults to ``'Optima'``.
            fontweight (str): The fontweight of text.
                Defaults to ``'bold'``.
            math_fontfamily (str): The math_fontfamily of text.
                Defaults to ``'cm'``.
            **kwargs: Keyword arguments passed to
                :any:`Axes.set_xlabel() <matplotlib.axes.Axes.set_xlabel>`
                or :any:`Axes.set_ylabel() <matplotlib.axes.Axes.set_ylabel>`.

        :Example:
            .. code-block:: python
                :emphasize-lines: 5-6

                import numpy as np
                from alpsplot.figure import Figure

                fig = Figure('test_set_axis_label')
                fig.set_axis_label('x', 'x label')
                fig.set_axis_label('y', 'y label')
                fig.save(ext='.svg')  # './output/test_set_axis_label.svg'

            .. image:: /images/figure/test_set_axis_label.svg
                :width: 60%
        """
        func = getattr(self.ax, f'set_{axis}label')
        func(text, fontsize=fontsize, fontproperties=fontproperties,
             fontweight=fontweight, math_fontfamily=math_fontfamily,
             **kwargs)

    def set_axis_lim(self, axis: str, labels: list[str] = None,
                     lim: tuple[float, float] = (0.0, 1.0),
                     margin: tuple[float, tuple] = (0.0, 0.0),
                     piece: int = 10, _format: str = '%.1f',
                     fontsize: int = 11,
                     fontproperties: str = 'Optima',
                     fontweight: str = 'bold',
                     math_fontfamily: str = 'cm', **kwargs):
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
            set_ticklabels(labels, \*\*fontargs, \*\*kwargs)
            format_str = :any:`ticker.FormatStrFormatter <matplotlib.ticker.FormatStrFormatter>`\(_format)
            :any:`Axis.set_major_formatter <matplotlib.axis.Axis.set_major_formatter>`\(format_str)

        Args:
            axis (str): The axis to set label.
                Possible values: ``['x', 'y', 'z']``.
            labels (list[str]): The text of axis tick labels.
                Defaults to `None`.
            lim (tuple[str, str]): The limit of axis ticks.
                Defaults to `(0.0, 1.0)`.
            margin (tuple[str, str]): The margin at
                head and tail of axis ticks.
                Defaults to `(0.0, 0.0)`.
            piece (int): The number of axis ticks - 1.
                The interval among ticks are
                :math:`\frac{\text{lim}[1] - \text{lim}[0]}{\text{piece}}`.
                Defaults to `10`.
            _format (str): The format of tick labels.
                Defaults to ``'%.1f'``.

        ..

        Args:
            fontsize (int): The fontsize of text.
                Defaults to `11`.
            fontproperties (str): The font of text.
                Defaults to ``'Optima'``.
            fontweight (str): The fontweight of text.
                Defaults to ``'bold'``.
            math_fontfamily (str): The math_fontfamily of text.
                Defaults to ``'cm'``.
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

                fig = Figure('test_set_axis_lim')
                fig.set_axis_lim('x', lim=(2.0, 3.0),
                                 piece=2, _format='%.2f')
                fig.set_axis_lim('y', labels=['l1', 'l2', 'l3'],
                                 lim=(0.0, 4.0),
                                 margin=(2.0, 2.0),
                                 piece=2, _format='%d')
                fig.save(ext='.svg')  # './output/test_set_axis_lim.svg'

            .. image:: /images/figure/test_set_axis_lim.svg
                :width: 60%

        """  # noqa: E501
        final_lim = lim[0] - margin[0], lim[1] + margin[1]
        ticks = np.append(
            np.arange(lim[0], lim[1], (lim[1] - lim[0]) / piece), lim[1])
        getattr(self.ax, f'set_{axis}lim')(*final_lim)
        getattr(self.ax, f'set_{axis}ticks')(ticks)
        set_ticklabels_func = getattr(self.ax, f'set_{axis}ticklabels')
        font_args = dict(fontsize=fontsize,
                         fontproperties=fontproperties,
                         fontweight=fontweight,
                         math_fontfamily=math_fontfamily)
        if labels is None:
            labels = getattr(self.ax, f'get_{axis}ticks')()
            set_ticklabels_func(labels, **font_args, **kwargs)
            _format = '%d' if _format == 'interger' else _format
            getattr(self.ax, f'{axis}axis').set_major_formatter(
                ticker.FormatStrFormatter(_format))
        else:
            set_ticklabels_func(labels, **font_args, **kwargs)

    def set_legend(self, *args, frameon: bool = None,
                   framealpha: float = 1.0,
                   edgecolor: str = 'none',
                   fontsize: int = 11,
                   fontproperties: str = 'Optima',
                   fontstyle: str = None, fontweight='bold',
                   math_fontfamily: str = 'cm', **kwargs) -> None:
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
                Defaults to `0.0`.
            edgecolor (str): The legend's background patch edge color.
                Defaults to ``'none'``.

        ..

        Args:
            fontsize (int): The fontsize of text.
                Defaults to `11`.
            fontproperties (str): The font of text.
                Defaults to ``'Optima'``.
            fontstyle (str): The font style of text.
                Defaults to `None`.
            fontweight (str): The fontweight of text.
                Defaults to ``'bold'``.
            math_fontfamily (str): The math_fontfamily of text.
                Defaults to ``'cm'``.
            **kwargs: Keyword arguments passed to
                :any:`Axes.legend() <matplotlib.axes.Axes.legend>`.

        :Example:
            .. code-block:: python
                :emphasize-lines: 16

                import numpy as np
                from alpsplot.figure import Figure

                fig = Figure('test_set_legend')
                fig.set_axis_lim('x', lim=(0.0, 10.0),
                                 margin=(0.5, 0.0),
                                 piece=5, _format='%d')
                fig.set_axis_lim('y', lim=(0.0, 10.0),
                                 margin=(0.5, 0.0),
                                 piece=5, _format='%d')

                x = np.arange(10, step=0.5)
                y = np.arange(10, step=0.5)
                fig.lineplot(x, y, color='red', label='test_set_legend')

                fig.set_legend()
                fig.save(ext='.svg')  # './output/test_set_legend.svg'

            .. image:: /images/figure/test_set_legend.svg
                :width: 60%
        """
        self.ax.legend(*args, frameon=frameon, edgecolor=edgecolor,
                       framealpha=framealpha, **kwargs)
        plt.setp(self.ax.get_legend().get_texts(), fontsize=fontsize,
                 fontproperties=fontproperties,
                 fontstyle=fontstyle, fontweight=fontweight,
                 math_fontfamily=math_fontfamily)

    def lineplot(self, x: np.ndarray, y: np.ndarray,
                 err: np.array = None, err_style: str = 'band',
                 color: str = 'black', alpha: float = 1.0,
                 linewidth: int = 2, linestyle: str = '-',
                 label: str = None, markerfacecolor: str = 'white',
                 zorder: float = 1, **kwargs) -> Line2D:
        r"""A similar implementation to :any:`seaborn.lineplot() <seaborn.lineplot>`.

        Args:
            x (numpy.ndarray): The x array.
            y (numpy.ndarray): The y array.
            err (numpy.ndarray): The x array. Defaults to `None`.
            err_style (str): Whether to draw the confidence intervals
                with translucent error bands or discrete error bars.
                Possible values: ``['band', 'bars']``
                Defaults to `band`.

        ..

        Args:
            color (str): Set the color of the line.
                Defaults to ``'black'``.
            alpha (float): Set the alpha value used for blending
                - not supported on all backends.
                It must be within the 0-1 range.
                Defaults to `1.0`.
            linewidth (str): Set the line width in points.
                Defaults to `2`.
            linestyle (str): Set the linestyle of the line.
                Defaults to ``'-'``.
            label (str): Set a label that will be displayed in the legend.
                Defaults to `None`.
            markerfacecolor (str): Set the marker face color.
                Defaults to ``'white'``.
            zorder (float): Set the zorder for the artist.
                Artists with lower zorder values are drawn first.
                Defaults to `1`.
            **kwargs: Keyword arguments passed to
                :any:`Axes.plot() <matplotlib.axes.Axes.plot>`.

        :Example:
            .. code-block:: python
                :emphasize-lines: 14, 20, 26-27

                import numpy as np
                from alpsplot.figure import Figure

                fig = Figure('test_lineplot')
                fig.set_axis_lim('x', lim=(0.0, 10.0),
                                 margin=(0.5, 0.0),
                                 piece=5, _format='%d')
                fig.set_axis_lim('y', lim=(0.0, 10.0),
                                 margin=(0.5, 0.0),
                                 piece=5, _format='%d')

                x = np.arange(10, step=0.5)
                y = np.arange(10, step=0.5)
                fig.lineplot(x, y, color='red', label='plain')

                x = np.concatenate((x, x, x))
                noise = np.random.randn(20)
                y_mean = y / 2
                y_err = np.concatenate((y_mean-noise, y_mean, y_mean+noise))
                fig.lineplot(x, y_err, color='green', label='error band')

                x = np.concatenate((x, x, x))
                noise = np.random.randn(20)
                y_mean = y / 2 + 4
                y_err = np.concatenate((y_mean-noise, y_mean, y_mean+noise))
                fig.lineplot(x, y_err, color='blue', label='error bar',
                             err_style='bars')

                fig.set_legend()
                fig.save(ext='.svg')  # './output/test_lineplot.svg'

            .. image:: /images/figure/test_lineplot.svg
                :width: 60%
        """
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
                                     zorder=zorder)
            elif err_style == 'bars':
                self.ax.errorbar(x=x, y=y, yerr=err,
                                 color=color, alpha=alpha, linestyle="",
                                 zorder=zorder)
        return self.ax.plot(x, y, color=color, alpha=alpha,
                            linewidth=linewidth, linestyle=linestyle,
                            label=label, markerfacecolor=markerfacecolor,
                            zorder=zorder, **kwargs)

    def curve_legend(self, label: str = None, color: str = 'black',
                     linewidth: int = 2, linestyle: str = '-',
                     markerfacecolor: str = 'white', **kwargs) -> Line2D:
        r"""Call :any:`Axes.plot() <matplotlib.axes.Axes.plot>`
        to plot an empty line for legend,

        which is helpful for setting marker-with-line
        legend of :meth:`scatter`.

        Args:
            label (str): Set a label that will be displayed in the legend.
                Defaults to `None`.
            color (str): Set the color of the line.
                Defaults to ``'black'``.
            linewidth (str): Set the line width in points.
                Defaults to `2`.
            linestyle (str): Set the linestyle of the line.
                Defaults to ``'-'``.
            markerfacecolor (str): Set the marker face color.
                Defaults to ``'white'``.
            **kwargs: Keyword arguments passed to
                :any:`Axes.plot() <matplotlib.axes.Axes.plot>`.

        :Example:
            .. code-block:: python
                :emphasize-lines: 5-6

                import numpy as np
                from alpsplot.figure import Figure

                fig = Figure('test_curve_legend')
                fig.curve_legend(color='red', marker='D',
                                 label='test_curve_legend')
                fig.set_legend()
                fig.save(ext='.svg')  # './output/test_curve_legend.svg'

            .. image:: /images/figure/test_curve_legend.svg
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
                zorder: float = 3, **kwargs) -> PathCollection:
        r"""Call :any:`Axes.scatter() <matplotlib.axes.Axes.scatter>`
        to plot scatters.

        Args:
            x (numpy.ndarray): The x array.
            y (numpy.ndarray): The y array.
            color (str): Set the color of the line.
                Defaults to ``'black'``.
            linewidth (str): Set the line width in points.
                Defaults to `2`.
            marker (str): The marker style.
                Defaults to ``'D'``.
            facecolor (str): Set the marker face color.
                Defaults to ``'white'``.
            label (str): Set a label that will be displayed in the legend.
                Defaults to `None`.
            curve_legend (bool): Whether the legend contains
                a line around the marker.
                Defaults to `False`.
            zorder (float): Set the zorder for the artist.
                Artists with lower zorder values are drawn first.
                Defaults to `3`.
            **kwargs: Keyword arguments passed to
                :any:`Axes.scatter() <matplotlib.axes.Axes.scatter>`.

        :Example:
            .. code-block:: python
                :emphasize-lines: 14-16

                import numpy as np
                from alpsplot.figure import Figure

                fig = Figure('test_scatter')
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
                fig.save(ext='.svg')  # './output/test_scatter.svg'

            .. image:: /images/figure/test_scatter.svg
                :width: 60%
        """
        if curve_legend and label is not None:
            self.curve_legend(label=label, color=color,
                              linewidth=linewidth, marker=marker, **kwargs)
            label = None
        return self.ax.scatter(x=x, y=y, color=color, linewidth=linewidth,
                               marker=marker, facecolor=facecolor, label=label,
                               zorder=zorder, **kwargs)

    def bar(self, x: np.ndarray, y: np.ndarray,
            width: float = 0.2, align: str = 'edge',
            color: str = 'black', edgecolor: str = 'white',
            linewidth: int = 1, label: str = None,
            **kwargs) -> BarContainer:
        r"""Call :any:`Axes.bar() <matplotlib.axes.Axes.bar>`
        to plot bars.

        Args:
            x (numpy.ndarray): The x array.
            y (numpy.ndarray): The y array.
            width (float): The width of the bars.
                Defaults to `0.2`.
            align (str):
                Alignment of the bars to the ``x`` coordinates.

                Possible values: ``['center', 'edge']``.
                Defaults to ``'edge'``.

                * ``'center'``: Center the base on the x positions.
                * ``'edge'``: Align the left edges of the bars
                  with the ``x`` positions.

            color (str): The colors of the bar faces.
                Defaults to ``'black'``.
            edgecolor (str): Set the bar edge color.
                Defaults to ``'white'``.
            linewidth (float): Width of the bar edges.
                If `0`, don't draw edges.
                Defaults to `1`.
            label (str): Set a label that will be displayed in the legend.
                Defaults to `None`.
            **kwargs: Keyword arguments passed to
                :any:`Axes.bar() <matplotlib.axes.Axes.bar>`.
        """
        return self.ax.bar(x, y, width=width, align=align,
                           color=color, edgecolor=edgecolor,
                           linewidth=linewidth, label=label,
                           **kwargs)

    def hist(self, x: np.ndarray, bins: int = None,
             density: bool = True, **kwargs):
        r"""Call :any:`Axes.hist() <matplotlib.axes.Axes.hist>`
        to plot a histogram.

        Args:
            x (numpy.ndarray): The x array.
            bins (int | ~typing.Sequence[int] | str): Defaults to be `None`.

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
            density (bool): Defaults to be `False`.
                If `True`, draw and return a probability density.

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
        """
        return self.ax.hist(x, bins=bins, density=density, **kwargs)

    def autolabel(self, rects: BarContainer, above: bool = True,
                  fontsize: int = 6,
                  fontproperties: str = 'Optima', fontweight: str = 'bold',
                  math_fontfamily: str = 'cm',
                  **kwargs) -> None:
        r"""Call :any:`Axes.annotate() <matplotlib.axes.Axes.annotate>`
        to attach a text label above each bar in :attr:`rects`,
        displaying its height.

        Args:
            rects (~matplotlib.container.BarContainer): The bar rectangles
                to annotate.
            above (bool): Whether to put the text above the rects.

        Args:
            fontsize (int): The fontsize of text.
                Defaults to `6`.
            fontproperties (str): The font of text.
                Defaults to ``'Optima'``.
            fontweight (str): The fontweight of text.
                Defaults to ``'bold'``.
            math_fontfamily (str): The math_fontfamily of text.
                Defaults to ``'cm'``.
            **kwargs: Keyword arguments passed to
                :any:`Axes.annotate() <matplotlib.axes.Axes.annotate>`.
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
                             math_fontfamily=math_fontfamily,
                             **kwargs)

    # def bar3d(self, x: np.ndarray, y: np.ndarray, z: np.ndarray,
    #           color: str = 'black', size: tuple[float, float] = 0.5,
    #           label: str = None, **kwargs) -> BarContainer:
    #     # facecolor edgewidth alpha
    #     if isinstance(size, (float, int)):
    #         size = [size, size]
    #     return self.ax.bar3d(x=x, y=y, z=np.zeros_like(x),
    #                          dx=np.ones_like(x) * size[0],
    #                          dy=np.ones_like(y) * size[1],
    #                          dz=z, color=color, label=label,
    #                          **kwargs)
