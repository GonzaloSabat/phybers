"""! @brief Poggers"""
##
# @mainpage Fibers segmentation wrapper
#
# @section description_main Description
# An example of the segmentation code for fibers.
#
# @brief Example Python program with Doxygen style comments.
#
#Imports
from subprocess import run
import sys

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

run(["./main", npoints, fibrasdir, idsubj, atlasdir, atlasIformation, seg_resul, id_seg_result])

