'''
Application variables.
'''
APP = ['main.py']

APP_ID = 'moreviewer'

APP_SHORT_NAME = 'MoRe Viewer'

APP_LONG_NAME = 'Morphological Reinflection Viewer'

APP_DESCRIPTION = 'Graphical user interface for the evaluation of morphological reinflection tasks.'

APP_VERSION = '0.4.2'

APP_LICENSE = 'MIT'

AUTHOR_NAME = 'Ioannis Dikeoulias'

AUTHOR_EMAIL = 's9iodike@stud.uni-saarland.de'

YEAR = "2020"

DATA_FILES = []

ORG_NAME = 'AtomBytesCode'

ORG_ID = 'atbyco'

PROJECT_REPO = 'https://repos.lsv.uni-saarland.de/mlindemann/morpho'

OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'media/app-icons/nlp.icns',
    'plist': {
        'CFBundleName': APP_SHORT_NAME,
        'CFBundleDisplayName': APP_SHORT_NAME,
        'CFBundleGetInfoString': APP_LONG_NAME,
        'CFBundleIdentifier': "com."+ORG_ID+".osx."+APP_ID,
        'CFBundleVersion': APP_VERSION,
        'CFBundleShortVersionString': APP_VERSION,
        'NSHumanReadableCopyright': u"Copyright "+YEAR+", "+AUTHOR_NAME+", All Rights Reserved."
    }
}

REQUIRED = {
    'pyqt5',
    'numpy',
    'jellyfish',
    'matplotlib',
    'langdetect',
    'darkdetect'
}
