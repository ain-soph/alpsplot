#!/usr/bin/env python3

from .version import __version__

from alpsplot import colormap, utils
from alpsplot.figure import Figure

import os
import matplotlib.pyplot as plt
from .utils import fonts

__all__ = ['colormap', 'Figure', 'utils']

fonts.main()
plt.style.use(os.path.join(os.path.dirname(__file__), 'alpsplot.mplstyle'))
