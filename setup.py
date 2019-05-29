from setuptools import setup
setup(name='slots',
    version='0.0.3',
    description='Simple, expandable, customizable slot machine',
    url='https://github.com/s4w3d0ff/python-slots',
    author='s4w3d0ff',
    license='GPL v2',
    packages=['slots'],
    install_requires=['tqdm'],
    extras_require={'numpy': ['numpy']},
    zip_safe=False,
    keywords=['slots', 'slotmachine', 'slot-machine'],
    classifiers = [
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python :: 2.7+',
          'Programming Language :: Python :: 3.4+'
          ]
    )
