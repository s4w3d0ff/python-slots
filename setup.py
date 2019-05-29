from setuptools import setup

read_md = lambda f: open(f, 'r').read()

setup(name='slotmachine',
    version='0.0.3.8',
    description='Simple, expandable, customizable slot machine',
    long_description=read_md('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/s4w3d0ff/python-slots',
    author='s4w3d0ff',
    author_email="info@s4w3d0ff.host",
    license='GPL v3',
    packages=['slotmachine'],
    install_requires=['tqdm'],
    extras_require={'numpy': ['numpy']},
    zip_safe=False,
    keywords=['slots', 'slotmachine', 'slot-machine'],
    classifiers = [
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3'
          ]
    )
