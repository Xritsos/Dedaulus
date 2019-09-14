# Daedalus_Interpolator_V2.0
# ********************************************************************************
# This program reads Daedalus' orbit (LLA) and TIEGCM's data and then interpolates
# TIGCM's variables (scalars) to Daedalus' orbit. In charge of the interpolation are
# a set of FORTRAN subroutines wrapped under f2py3. There are 2 different versions of
# those subroutines, Serial_Version and Parallel_Version. The Parallel_Version is
# using the OpenMP interface for multithreading.Interpolation Method: Trilinear 3D
# Instructions for FORTRAN subroutines compilation

# Serial_Version
# No Optimization: "f2py3 -c Interpolation_Serial_Version.f95 -m interpolation"

# Parallel_Version
# No Optimization: "f2py3 -c --f90flags="-fopenmp " -lgomp  Interpolation_Parallel_Version.f95 -m interpolation"
# -O1 Level Optimization: "f2py3 -c --f90flags="-fopenmp " -lgomp --opt='-O1' Interpolation_Parallel_Version.f95 -m interpolation"
# -O2 Level Optimization: "f2py3 -c --f90flags="-fopenmp " -lgomp --opt='-O2' Interpolation_Parallel_Version.f95 -m interpolation"
# -O3 Level Optimization: "f2py3 -c --f90flags="-fopenmp " -lgomp --opt='-O3' Interpolation_Parallel_Version.f95 -m interpolation"
# -ffast Level Optimization: "f2py3 -c --f90flags="-fopenmp " -lgomp --opt='-ffast' Interpolation_Parallel_Version.f95 -m interpolation"
# KEP 5/6/19


# Usage Instructions:
# 1) Compile either parallel or serial version selecting proper options from above
# 2) Run python code
# Compilation of fortran subroutines needs to take place once.
# ********************************************************************************



            #  ____                 _       _
            # |  _ \  __ _  ___  __| | __ _| |_   _ ___
            # | | | |/ _` |/ _ \/ _` |/ _` | | | | / __|
            # | |_| | (_| |  __/ (_| | (_| | | |_| \__ \
            # |____/ \__,_|\___|\__,_|\__,_|_|\__,_|___/



from netCDF4 import Dataset
import matplotlib.pyplot as plt
import pandas as pd
import interpolation
import numpy as np
from datetime import datetime
import os

def Interpolator( model_data_file, model_data_secondary_file, orbit_file, save, VAR, max_alt):
# directory-->string:: output directory
# model_data_file,model_data_secondary_file--> strings:: model data files in data folder netCDF file provided from modellers
# orbit_file-->string :: orbit filename in Time-Lat-Lon-Alt format as porvided in Jupyter
# max_alt-->float:: max altitude for the interpolation--depends on model and user preference
# save--> Logical:: if true saves interpolated values to directory
# VAR--> string:: variable to inteprolate, must be  one of the variables included in the model data
#Outputs:: Plots+ 1 csv file


    # ******************************************************************************
    # Interpolation Site Min and Max Altitude Along Track Depending on Model and User Preference
    min_alt=150
    # max_alt=450

    #============== Read File + Orbitt and Manipulate Data=======
    TIEGCM=Dataset(model_data_file)
    TIEGCM_secondary=Dataset(model_data_secondary_file)
    df = pd.read_csv( orbit_file )
    # =================================================

    # Pull data from orbit
    daed_lat_temp = df["Lat (deg)"]
    daed_lon_temp = df["Lon (deg)"]
    daed_alt_temp = df["Alt (km)"]


    # Sample Orbit and Find Positions Below 450km
    counter=0
    for i in range(0,len(daed_alt_temp)):
        if (daed_alt_temp[i] < max_alt and daed_alt_temp[i] > min_alt):
            counter=counter+1
    # ******************************************************************************


    # ******************************************************************************
    # Allocate Arrays
    daed_lat=np.zeros((counter))
    daed_lon=np.zeros((counter))
    daed_alt=np.zeros((counter))


    #Keep Data in MIN MAX Range
    counter=0
    for i in range(0,len(daed_alt_temp)):
        if (daed_alt_temp[i] < max_alt and daed_alt_temp[i] > min_alt):
            # daed_time[counter]=daed_time_temp[i]
            daed_lat[counter]=daed_lat_temp[i]
            daed_lon[counter]=daed_lon_temp[i]
            daed_alt[counter]=daed_alt_temp[i]
            counter=counter+1
    # ******************************************************************************


    # ******************************************************************************
    # Pull data from Model
    grid_lat=TIEGCM.variables['lat'][:]
    grid_lon=TIEGCM.variables['lon'][:]
    grid_lev=TIEGCM.variables['ilev'][:]
    grid_time=TIEGCM.variables['time'][:]
    zg=TIEGCM_secondary.variables['ZG'][:]

    # Select Variable to Interpolate
    ne=TIEGCM.variables[VAR][:]
    # ne=VAR


    # Read Variable Attribute and Parse for Surface Plotting
    # print (TIEGCM_secondary.variables['NE'])
    # surf_Z=ne[1,7,:,:]     # To Surf Plot At The End
    # ******************************************************************************


    # ******************************************************************************
    #Find model's temporal resolution in minutes
    model_dt=(grid_time[1]-grid_time[0])*60   #in seconds
    orbit_dt=1/16                             #in seconds
    print("Timestep of Model Data is ",model_dt, "seconds")
    print("Timestep of Orbit Data is ",orbit_dt, "seconds")
    # ******************************************************************************


    # ******************************************************************************
    #Allocate a matrix for the interpolated values
    int_data=np.zeros(((counter)))

    print("Interpolation Starting...",counter, "Positions to Interpolate")
    #*********************Call Interpolation Subroutines***************************
    interpolation.daed_interp(grid_lat,grid_lon,grid_lev,daed_lat,daed_lon,daed_alt,zg,model_dt,orbit_dt,ne,int_data)
    # *****************************************************************************
    print("Interpolation Done!")
    # ******************************************************************************


    # ******************************************************************************
    # Create 2d Array for Results alonside Daedalus' orbit
    int_data_out= np.zeros([len(daed_alt), 4])
    int_data_out[:,0]=daed_lat
    int_data_out[:,1]=daed_lon
    int_data_out[:,2]=daed_alt
    int_data_out[:,3]=int_data

    #Export Data
    if save==True:
        # if not os.path.exists(directory):
        #     os.makedirs(directory)
        np.savetxt(orbit_file[:-4]+"_" +VAR+".csv", int_data_out , delimiter=",")
    # ******************************************************************************


    # ******************************************************************************
    # Plotting
    plt.scatter(daed_lon,int_data,c=int_data,s=0.05)
    plt.title("TIEGCM:" +VAR+" Along Daedalus' Orbit")
    plt.xlabel("Lon")
    plt.ylabel("Electron Density $cm^-3$")
    plt.grid("True")


    # Surface Plot
    # plt.figure(2)
    # plt.imshow(surf_Z,cmap="rainbow")

    # if Save_Surf==True:
    #     np.savetxt("Outputs/"+"Surf_Data.csv", surf_Z , delimiter=",")

    plt.show()
    # ******************************************************************************
    return (orbit_file[:-4]+"_" +VAR+".csv")



# ******************************************************************************

# # Example Call
'''
directory="outputs"
model_data_file="tiegcm_restart_p.nc.0001"
model_data_secondary_file="tiegcm.s.nc.0001"
orbit_file="Daedalus_MDL_Sample_Orbit"
save=True
VAR="NE"
max_alt=450
Interpolator(directory,model_data_file,model_data_secondary_file,orbit_file,save,VAR,max_alt)
'''