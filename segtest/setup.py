import setuptools
import os
from setuptools.command.develop import develop
from setuptools.command.install import install
import subprocess

pathname = os.path.dirname(__file__)
print("PATHNAME ES: " + pathname)

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        pathname = os.path.dirname(__file__)
        print("PATHNAME ES: " + pathname)
        
        #subprocess.run(["g++", "-std=c++14", "-O3", pathname + "/src/gsabat/Documents/segtest/Atlas_Fibras/main.cpp", "-o", "/home/gsabat/Documents/segtest/Atlas_Fibras/main", "-fopenmp", "-ffast-math"])
        
class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        develop.run(self)
        pathname = os.path.dirname(__file__)
        print("PATHNAME ES: " + pathname)
        
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION


setuptools.setup(name='segtest',
      version='0.0.32',
      description='Segmentation Test + example',
      url='https://github.com/GonzaloSabat/MT',
      author='Gonzalo Susbat',
      author_email='gsabat@udec.cl',
      license='UdeC',
      package_dir={"": "src"},
      packages=setuptools.find_packages(where="src"),
      #zip_safe=False,
      #packages=['segmentation'],
      #package_dir={'segmentation': 'src/segmentation'}
      include_package_data=True,
      cmdclass={'develop': PostDevelopCommand,'install': PostInstallCommand,},
      install_requires=[
          'numpy',
          'dipy',
          'joblib',
          'matplotlib',
          'sklearn',
          'networkx'
      ]
      )
      
