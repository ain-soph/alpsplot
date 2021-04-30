#!/usr/bin/env python3

from alpsplot.fonts import add_optima, add_palatino
import matplotlib.font_manager
import os

from os.path import dirname as d
from os.path import abspath, normpath


def test_add_palatino():
    fontManager: matplotlib.font_manager.FontManager = matplotlib.font_manager.fontManager
    ttflist: list[matplotlib.font_manager.FontEntry] = fontManager.ttflist
    fname_list: list[str] = []
    ttc_path = os.path.join(normpath(d(d(abspath(__file__)))),
                            'fonts', 'Palatino.ttc')
    fontManager.addfont(ttc_path)
    add_palatino()
    for font in ttflist:
        if 'palatino' in font.fname.lower():
            assert 'ttc' not in font.fname.lower()
            assert font.name == 'Palatino'
            fname_list.append(os.path.basename(font.fname))
    style_list = ['Roman', 'Italic', 'Bold', 'BoldItalic']
    for style in style_list:
        assert f'Palatino-{style}.ttf' in fname_list


def test_add_optima():
    fontManager: matplotlib.font_manager.FontManager = matplotlib.font_manager.fontManager
    ttflist: list[matplotlib.font_manager.FontEntry] = fontManager.ttflist
    fname_list: list[str] = []
    ttc_path = os.path.join(normpath(d(d(abspath(__file__)))),
                            'fonts', 'Optima.ttc')
    fontManager.addfont(ttc_path)
    add_optima()
    for font in ttflist:
        if 'optima' in font.fname.lower():
            print(font.fname)
            assert 'ttc' not in font.fname.lower()
            assert font.name == 'Optima'
            fname_list.append(os.path.basename(font.fname))
    style_list = ['Regular', 'Italic', 'Bold', 'BoldItalic', 'ExtraBlack']
    for style in style_list:
        assert f'Optima-{style}.ttf' in fname_list
