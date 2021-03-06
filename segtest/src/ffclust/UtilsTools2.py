#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 15:54:16 2021

@author: liset
"""
import subprocess as sp
import os
import ffclust.FibersTools.FibersTools as fb
import pandas as pd
import sys

#%% Primero se crea un directorio para guardar todos los parámetros estadísticos

#in_stadisticsPath="data/ffclust/stadistics/" # Esto sería un directorio dentro de los resultados de cada algoritmo aplicado, ya sea, segmentación, clustering (jerárquico o ffclust)
pathname = os.path.dirname(__file__)
#in_stadisticsPath=sys.argv[1] + "/statistics"
in_stadisticsPath=sys.argv[1]

stadisticsFolder =  in_stadisticsPath + "/stadistics"

print("in_stadisticsPath is: " + in_stadisticsPath)
if not os.path.exists(in_stadisticsPath):
    os.mkdir(in_stadisticsPath)

if not os.path.exists(stadisticsFolder):
    os.mkdir(stadisticsFolder)
#%% 1. Fibers Lens (se calcula para el centroide del clúster) and Fibers Size ( cantidad de fibras por clúster)

def write_lensAndsizes(in_cent, in_dirsetfibers):    
    """ 
    Fibers Lens (se calcula para el centroide del clúster) and 
    Fibers Size ( cantidad de fibras por clúster)
    """
    
    txt_lens = ""
    txt_sizes = ""
    
    for i in range(len(in_cent)):
        
        # Para calcular el largo se utiliza la función fiber_lens de FibersTools.
        txt_lens += str(fb.fiber_lens(in_cent[i]))+"\n" 
    
        # 2. Para calcular el tamño se utiliza getBundleSize() de FibersTools.

        txt_sizes += str(fb.getBundleSize(in_dirsetfibers+str(i)+".bundles"))+"\n"
    
    #with open(in_stadisticsPath + "/lens.txt", "w") as file:
    #    if os.path.exists(in_stadisticsPath + "/lens.txt"):
    #        print("LENS EXISTS")
    #    else:
    #        print("LENS DOESNT EXIST") 
    #    file.write(txt_lens)

    #with open(in_stadisticsPath + "/sizes.txt", "w") as file:
    #    if os.path.exists(in_stadisticsPath + "/sizes.txt"):
    #        print("sizes EXISTS")
    #    else:
    #        print("sizes DOESNT EXIST") 
    #    file.write(txt_sizes)
   
    with open(stadisticsFolder+ "/lens.txt", "w") as file:
        if os.path.exists(stadisticsFolder + "/lens.txt"):
            print("LENS EXISTS")
        else:
            print("LENS DOESNT EXIST") 
        file.write(txt_lens)

    with open(stadisticsFolder + "/sizes.txt", "w") as file:
        if os.path.exists(stadisticsFolder + "/sizes.txt"):
            print("sizes EXISTS")
        else:
            print("sizes DOESNT EXIST") 
        file.write(txt_sizes)

in_cent = fb.read_bundle(in_stadisticsPath + "/FinalCentroids/centroids.bundles")
in_dirsetfibers= in_stadisticsPath + "/FinalBundles/"
print("writing lens and sizes with arguments: ")
print(in_dirsetfibers)

write_lensAndsizes(in_cent, in_dirsetfibers)
#%% 3. Stadistics Measures (Hay que revisar porque parece tener alguna ruta relativa por default). Esta función se encuentra implementada en C++ y tiene disponible los siguientes cálculos: 
# - Distancia intra-clúster mínima,  Distancia intra promedio y  Distancia intra máxima.
# - Rij.
# - Distancia Inter-clústeres.
# - DBindex
print("\n---Stadistics Measures ---")
in_centroides= in_stadisticsPath + "/FinalCentroids/centroids.bundles"
in_clusters_directory= in_stadisticsPath + "/FinalBundles"
out_Result_directory= in_stadisticsPath + "/stadistics/mensure"


in_npoints="21"
dbindex_path = pathname + '/data/ffclust/'

if os.path.exists(dbindex_path + '/dbindex'):
    print("dbindex exists.")
else:
    print("dbindex does not exist in path. Compiling it: ")
    sp.run(['g++','-std=c++14','-O3', dbindex_path + '/dbindex.cpp', '-o', dbindex_path + '/dbindex', '-fopenmp', '-ffast-math'])
    
    if os.path.exists(dbindex_path + '/dbindex'):
        print("Target directory has been created successfully.")

    else: 
        print("Target directory still doesn't exist. Exiting...")
        exit()
        
sp.run([ dbindex_path + '/dbindex',in_centroides, in_clusters_directory, out_Result_directory,in_npoints])


#%% 4. Filtrado de los parámetros estadísticos sets de fibras. 
# Detallar que para el filtrado es necesario aplicar el paso 1, 2 y 3. Estos generan archivos ".txt" con la información estadísticas.     
print("\n---Filtrado de los parámetros estadísticos sets de fibras---")
#fb.Stadistics_txt_toxlsx(in_stadisticsPath) # Función que introduce las variables estadísticas en un Dataframe. 
fb.Stadistics_txt_toxlsx(stadisticsFolder) # Función que introduce las variables estadísticas en un Dataframe. 
# Esta función guarda el dataframe en un excel dentro del directorio de las variables estadísticas. 

df_data = pd.read_excel(stadisticsFolder+'stadistics.xlsx') ## Lectura del obj pandas

# Luego, aplicar múltiples filtrados se reduce a la utilización de las herramientas para filtrar objetos pandas
# Ejemplo de filtrado por el tamaño
filt_size = df_data[(df_data.sizes>=100) & (df_data.sizes<=150)] 
filt_size
# Ejemplo de filtrado por el tamaño y el largo
filt_sizelens = df_data[(df_data.sizes>=100) & (df_data.lens >5)] 
    
#%% 5. Sampling from points to "n" equidistant points (se calcula para un conjunto de fibras)       

#indir="data/100206/100206_MNI.bundles"
#in_npoints="21" #puede variar, elección del usuario, se recomienda usar a 21 puntos.
#outdir="data/100206/100206_MNI_21p.bundles"
#sp.run(['./sampled_npoints/sliceFibers', indir, outdir, in_npoints])

#%% 6. Deformation to MNI space for HCP database

#in_imgdef="data/100206/acpc_dc2standard.nii" #importante, dar error si no se entrega
#indir="data/100206/100206.bundles" #importante
#outdir="data/100206/100206_MNI.bundles"
#sp.run(['./deformHCPtoMNI/deform',in_imgdef, indir, outdir])
    
#%% 7. Intersección


