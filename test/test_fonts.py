#!/usr/bin/env python3

from alpsplot.fonts import add_palatino
import matplotlib.font_manager
import os


def test_add_palatino():
    add_palatino()
    fontManager: matplotlib.font_manager.FontManager = matplotlib.font_manager.fontManager
    ttflist: list[matplotlib.font_manager.FontEntry] = fontManager.ttflist
    fname_list: list[str] = []
    for font in ttflist:
        if 'palatino' in font.fname.lower():
            assert 'ttc' not in font.fname.lower()
            assert font.name == 'Palatino'
            fname_list.append(os.path.basename(font.fname))
    style_list = ['normal', 'italic', 'bold', 'bold_italic']
    for style in style_list:
        assert f'palatino_{style}.ttf' in fname_list
