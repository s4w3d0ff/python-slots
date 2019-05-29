from setuptools import setup
<<<<<<< HEAD
try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

setup(name='slotmachine',
    version='0.0.3.5',
    description='Simple, expandable, customizable slot machine',
    long_description=read_md('README.md'),
=======
with open('README.md') as file_object:
    description = file_object.read()
setup(name='slotmachine',
    version='0.0.3.4',
    description='Simple, expandable, customizable slot machine',
    long_description=description,
>>>>>>> e3477985cd3595ba9e080c37d2b83356809c7123
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
