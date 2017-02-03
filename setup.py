#!/usr/bin/env python
from setuptools import setup, find_packages
from codecs import open
from os import path
import gatheros

__version__ = gatheros.__version__

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

setup(
    name=gatheros.__name__,
    version=__version__,
    description='A suite for gathering and presenting OS related information',
    long_description=long_description,
    url='https://github.com/operatorequals/gatheros',
    download_url='https://github.com/operatorequals/gatheros/tarball/' + __version__,
    license='BSD',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 2',
      'Operating System :: POSIX :: Linux'
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author=gatheros.__author__,
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='john.torakis@gmail.com',
    # scripts = ["gatheros/gatheros", "gatheros/gatheros_show", "gatheros/gatheros_exec" ],
    entry_points = {
        'console_scripts' : [ "gatheros=gatheros.gatheros:main",
                        "gatheros-exec=gatheros.gatheros_exec:main",
                        "gatheros-show=gatheros.gatheros_show:main",
                        # "gatheros-edit=gatheros.gatheros_edit:main",
                        ]
                    }
)
