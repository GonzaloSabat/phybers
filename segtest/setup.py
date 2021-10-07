import setuptools
import os
from setuptools.command.develop import develop
from setuptools.command.install import install
import subprocess

pathname = os.path.dirname(__file__)


setuptools.setup(name='segtest',
      version='0.0.39',
      description='Segmentation + FFClust + HClust',
      url='https://github.com/GonzaloSabat/MT',
      author='Gonzalo Sabat',
      author_email='gsabat@udec.cl',
      license='UdeC',
      package_dir={"": "src"},
      packages=setuptools.find_packages(where="src"),
      #zip_safe=False,
      #packages=['segmentation'],
      #package_dir={'segmentation': 'src/segmentation'}
      include_package_data=True,
      install_requires=[
          'numpy',
          'dipy',
          'joblib',
          'matplotlib',
          'sklearn',
          'networkx'
      ]
      )
      
