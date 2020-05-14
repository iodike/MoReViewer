'''
PyQt5 imports.
'''
from PyQt5.QtCore import Qt, QSettings, QSize, QFile, QRegExp, QThread, QTimer
from PyQt5.QtGui import QFont, QIcon, QPixmap, QTextCharFormat, QSyntaxHighlighter, QPainter, QPalette, QBrush
from PyQt5.QtWidgets import *

'''
Source imports.
'''
from src.utils.QHLine import *
from src.include.languages import *
from src.include.grammar import *
from src.include.vars import *
from src.include.appinfo import *

'''
Python native imports.
'''
import random
import string
import os
import re
import statistics
import difflib
import hashlib
from datetime import datetime
import json
import time
import logging

'''
Python third-party imports.
'''
import numpy
import jellyfish
from langdetect import detect
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import darkdetect
from shutil import copy
