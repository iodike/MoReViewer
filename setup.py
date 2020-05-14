'''
Imports
'''
from setuptools import setup, find_packages
from src.include.appinfo import *

'''
Setup information
'''
setup(
    app=APP,
    name=APP_SHORT_NAME,
    version=APP_VERSION,
    data_files=DATA_FILES,
    description=APP_DESCRIPTION,
    url=PROJECT_REPO,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    license=APP_LICENSE,
    packages=find_packages(),
    options={'py2app': OPTIONS},
    install_requires=list(REQUIRED),
    setup_requires=['py2app'],
    zip_safe=False
)
