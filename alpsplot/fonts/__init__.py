#!/usr/bin/env python3

import os
import matplotlib
import matplotlib.font_manager


def add_optima() -> None:
    dirname = os.path.dirname(__file__)
    fontManager: matplotlib.font_manager.FontManager = matplotlib.font_manager.fontManager
    ttflist: list[matplotlib.font_manager.FontEntry] = fontManager.ttflist
    for i, font in enumerate(ttflist):
        if 'optima.ttc' in font.fname.lower():
            del ttflist[i]

    for style in ['Regular', 'Italic', 'Bold', 'BoldItalic', 'ExtraBlack']:
        file_path = os.path.normpath(
            os.path.join(dirname, f'Optima-{style}.ttf'))
        fontManager.addfont(file_path)


def add_palatino() -> None:
    dirname = os.path.dirname(__file__)
    fontManager: matplotlib.font_manager.FontManager = matplotlib.font_manager.fontManager
    ttflist: list[matplotlib.font_manager.FontEntry] = fontManager.ttflist
    for i, font in enumerate(ttflist):
        if 'palatino.ttc' in font.fname.lower():
            del ttflist[i]

    for style in ['Roman', 'Italic', 'Bold', 'BoldItalic']:
        file_path = os.path.normpath(
            os.path.join(dirname, f'Palatino-{style}.ttf'))
        fontManager.addfont(file_path)
