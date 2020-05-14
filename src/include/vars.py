'''
Imports
'''
from os.path import expanduser

'''
GLOBALS
'''

'''
ICONS
'''
NEW_WHITE = 'media/btn-icons/folder_add_2_w.png'
OPEN_WHITE = 'media/btn-icons/folder_edit_3_w.png'
NEW_BLACK = 'media/btn-icons/folder_add_2.png'
OPEN_BLACK = 'media/btn-icons/folder_edit_3.png'
ICON = 'media/app-icons/nlp.ico'

'''
HTML/CSS
'''
BETA = "<span style='color:#9370DB'><sub><small>BETA</small></sub></span>"

'''
REGEX
'''
DEFAULT_REGEX = "^(.*)$"

'''
CONSTANTS
'''
STR_EMPTY = "*"

'''
DELIMITERS
'''
SEMIC_SPLIT = ';'
MINUS_SPLIT = '-'
SPACE_SPLIT = ' '

'''
DIRECTORIES
'''
HOME_DIR = expanduser("~")
PRO_FOLDER = '/MRE-projects'
PRO_EXT = '.mrp'
PRO_FILE = 'project' + PRO_EXT

'''
CONFIG
'''
CFG_EXT = '.json'
CFG_FILE = 'config' + CFG_EXT

STATS_OPTIONS = [
    "#rows / distance",
    "#rows / tag",
    "med. distance / tag",
    "mean distance / tag"
]

'''
INDEXES
'''
IINDEX = 0
TINDEX = 1
PINDEX = 2
GINDEX = 3
DINDEX = 4
AINDEX = 5
FINDEX = 6
MINDEX = 7
NINDEX = 8

INDEXES = [
    IINDEX,
    TINDEX,
    PINDEX,
    GINDEX,
    DINDEX,
    AINDEX,
    FINDEX,
    MINDEX,
    NINDEX
]

'''
INDEX SIZE
'''
INDEX_SIZE = len(INDEXES)

'''
INDEX LABELS
'''
INDEX_LABELS = {
    IINDEX: "INPUT",
    TINDEX: "TAGS",
    PINDEX: "PREDICTION",
    GINDEX: "GROUNDTRUTH",
    DINDEX: "DISTANCE",
    AINDEX: "ALIGNMENT",
    FINDEX: "FEATURES",
    MINDEX: "MARKERS",
    NINDEX: "NOTES"
}

'''
LOG LEVEL
'''
# off
LOG_OFF = 0
# debug
LOG_DEBUG = 1
# info
LOG_INFO = 2
# warning
LOG_WARN = 3
# error
LOG_ERROR = 4
# critical
LOG_CRITICAL = 5
# all
LOG_ALL = 6

'''
LOG LEVEL DICT
'''
LOG_LEVELS = {
    "OFF": LOG_OFF,
    "DEBUG": LOG_DEBUG,
    "INFO": LOG_INFO,
    "WARNING": LOG_WARN,
    "ERROR": LOG_ERROR,
    "CRITICAL": LOG_CRITICAL,
    "ALL": LOG_ALL
}

'''
LOG LABELS DICT
'''
LOG_LABELS = {
    LOG_OFF: "OFF",
    LOG_DEBUG: "DEBUG",
    LOG_INFO: "INFO",
    LOG_WARN: "WARNING",
    LOG_ERROR: "ERROR",
    LOG_CRITICAL: "CRITICAL",
    LOG_ALL: "ALL"
}

'''
PLOT SCALES
'''
LINEAR = 'linear'
LOGARITHMIC = 'logarithmic'

PLOT_SCALES = [
    LINEAR,
    LOGARITHMIC
]
