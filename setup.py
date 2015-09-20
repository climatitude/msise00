#!/usr/bin/env python3
import setuptools #enables develop
from numpy.distutils.core import setup,Extension


with open('README.rst','r') as f:
	  long_description = f.read()

#%% install
setup(name='msise00',
      version='0.1',
	  description='Python wrapper for MSIS-E00 atmosphere model',
	  long_description=long_description,
	  author='Michael Hirsch',
	  url='https://github.com/scienceopen/msise00',
	  install_requires=['pymap3d','histutils',
                        'numpy','six','pytz','pandas','astropy'],
      packages=['msise00'],
      dependency_links = ['https://github.com/scienceopen/pymap3d/tarball/master#egg=pymap3d',
                          'https://github.com/scienceopen/histutils/tarball/master#egg=histutils'
                            ],
      ext_modules=[Extension(name='gtd7',
                    sources=['fortrancode/nrlmsise00_sub.for'],
                    f2py_options=['--quiet'])]
	  )