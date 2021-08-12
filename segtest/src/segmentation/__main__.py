"""! @brief Testing"""
##
# @mainpage Fibers segmentation wrapper
#
# @section description_main Description
# An example of the segmentation code for fibers.
#
# @brief Example Python program with Doxygen style comments.
#
#Imports
import sys
import os
from subprocess import run

print(len(locals()))
pathname = os.path.dirname(__file__)
print("PATHNAME ES: " + pathname)
print("ARG0: " + sys.argv[0])
print("ARG1: " + sys.argv[1])
print("ARG2: " + sys.argv[2])
print("ARG3: " + sys.argv[3])
print("ARG4: " + sys.argv[4])
print("ARG5: " + sys.argv[5])
print("ARG6: " + sys.argv[6])
print("ARG7: " + sys.argv[7])
#Global Constants
## Number of points.
npoints = sys.argv[1]
## Fibers .bundles path.
fibrasdir = sys.argv[2]
## Subject ID.
idsubj = sys.argv[3]
## Atlas directory path.
atlasdir = sys.argv[4]
## Atlas info file.
atlasIformation = sys.argv[5]
## Output directory path for the segmentated fascicles for the subject.
seg_resul = sys.argv[6]
## Output directory path for the index of the original fibers for each detected fascicle.
id_seg_result = sys.argv[7]
#Functions



result_path = input ("Enter the path for the result folder to be created: ")
if os.path.exists(result_path + "/result"):
    print("Target directory exists. Checking if executable file exists: ")
else:
    print("Target directory does not exist in path. Creating it: ")
    run(['mkdir', result_path + '/result'])
    
    if os.path.exists(result_path + "/result"):
        print("Target directory exists noqw. Checking if executable file exists: ")
    else: 
        print("Target directory still doesn't exist. Exiting...")
        exit()
        
if os.path.exists(pathname + "/main"):
    print("Found executable file. Running segmentation executable file: ")
else:
    print("Executable file not found. Compiling main.cpp")
    run(['g++','-std=c++14','-O3', pathname + '/main.cpp', '-o', pathname + '/main', '-fopenmp', '-ffast-math'])
    if os.path.exists(pathname + "/main"):
        print("main.cpp compiled. Running executable file: ")
    else: 
        print("Executable file still not found. Exiting")
        exit()



run([pathname + "/./main", npoints, fibrasdir, idsubj, atlasdir, atlasIformation, seg_resul, id_seg_result])

