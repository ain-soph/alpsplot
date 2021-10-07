#!/usr/bin/env python3

from .version import __version__

from .figure import Figure
from .colormap import *
from .utils import *

import matplotlib
from .fonts import add_optima, add_palatino

add_optima()
add_palatino()
matplotlib.rc('mathtext', fontset='cm')
matplotlib.rc('pdf', fonttype=42)
matplotlib.rc('ps', fonttype=42)
matplotlib.rc('svg', image_inline=True, fonttype='none')
