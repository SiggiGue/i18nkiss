# -- encoding: utf-8 --

from setuptools import setup, find_packages

setup(name='i18n',
      version='0.1alpha',
      description="i18n tool in kiss mode.",
      author='Siegfried Guendert',
      author_email='siegfried.guendert@googlemail.com',
      license='ITAP GmbH',
      keywords='i18n',
      packages=find_packages(exclude=('docs', '.git')))
