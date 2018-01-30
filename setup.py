from setuptools import setup, find_packages

import animpy

VERSION = animpy.__version__
AUTHOR = animpy.__author__
EMAIL = animpy.__email__

setup(
    name='animpy',
    version=VERSION,
    packages=find_packages(),
    url='https://github.com/clamytoe/animpy',
    license='MIT',
    author=AUTHOR,
    author_email=EMAIL,
    description='Anime Python Research Tool (animpy)',
    install_requirements=[
        'beautifulsoup4',
        'click',
        'lxml',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        animpy=animpy.main:cli
    ''',
)

print(f'\n\n\t\t    '
      'AnimPy version {VERSION} installation succeeded.\n')
