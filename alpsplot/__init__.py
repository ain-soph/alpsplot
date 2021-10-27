#!/usr/bin/env python3

from .version import __version__

from alpsplot import colormap as colormap
from alpsplot import utils as utils
from alpsplot.figure import Figure

from .utils import fonts
fonts.main()

__all__ = ['Figure']
