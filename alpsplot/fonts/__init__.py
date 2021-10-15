#!/usr/bin/env python3

import os
import matplotlib
from matplotlib.font_manager import fontManager

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from matplotlib.font_manager import FontManager, FontEntry
    fontManager: FontManager


def add_optima() -> None:
    r"""
    Add ``optima`` font into :any:`matplotlib.font_manager`.

    You could use it by setting ``fontproperties='Optima'``
    """
    dirname = os.path.dirname(__file__)
    ttflist: list['FontEntry'] = fontManager.ttflist
    for i, font in enumerate(ttflist):
        if 'optima.ttc' in font.fname.lower():
            del ttflist[i]

    for style in ['Regular', 'Italic', 'Bold', 'BoldItalic', 'ExtraBlack']:
        file_path = os.path.normpath(
            os.path.join(dirname, f'Optima-{style}.ttf'))
        fontManager.addfont(file_path)


def add_palatino() -> None:
    r"""
    Add ``optima`` font into :any:`matplotlib.font_manager`.

    You could use it by setting ``fontproperties='Palatino'``
    """
    dirname = os.path.dirname(__file__)
    ttflist: list['FontEntry'] = fontManager.ttflist
    for i, font in enumerate(ttflist):
        if 'palatino.ttc' in font.fname.lower():
            del ttflist[i]

    for style in ['Roman', 'Italic', 'Bold', 'BoldItalic']:
        file_path = os.path.normpath(
            os.path.join(dirname, f'Palatino-{style}.ttf'))
        fontManager.addfont(file_path)


def main():
    add_optima()
    add_palatino()
    matplotlib.rc('mathtext', fontset='cm')
    matplotlib.rc('pdf', fonttype=42)
    matplotlib.rc('ps', fonttype=42)
    matplotlib.rc('svg', image_inline=True, fonttype='none')
