
# This script calculates the motional Electric field VxB due to spacecraft motion in orbit.
# Inputs are velocity of spacecraft in the orbit and magnetic field using IGRF model

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame


# Plotting Function
# x--> variable to be plotted 1D array
# plt_serial--> integer :: plot number
# label_y--> string:: y label
# title--> string :: title of plot
def plot_along_orbit(x,plt_serial,label_y,title):
    plt.figure(plt_serial)
    plt.plot(x)
    plt.title(title)
    plt.xlabel("Measurements")
    plt.ylabel(label_y)
    plt.grid(True)
    plt.show()

# ******************************************************************************************
# Main
# file_IGRF -->String:: file to read Magnetic Field and Daedalus Velocities(INPUT)
# outfile--> string::filename to save plasma products(OUTPUT)

def main(file_IGRF,outfile,Save_Products,var_to_plot,Plot_Products,label_y,title):

    Orbit_Data=pd.read_csv("data/"+file_IGRF)
    daed_time=Orbit_Data["Time (UTCG)"]
    daed_Bx=Orbit_Data["Bx_Tesla"]
    daed_By=Orbit_Data["By_Tesla"]
    daed_Bz=Orbit_Data["Bz_Tesla"]
    
    # Read Velocity Along Orbit
    daed_vx=Orbit_Data["vx (km/sec)"]
    daed_vy=Orbit_Data["vy (km/sec)"]
    daed_vz=Orbit_Data["vz (km/sec)"]
  
    # ******************************************************************************************
    # Calculating Motional Electric Field Using VxB --> *1e3 to convert km/s to m/s
    # ******************************************************************************************
    Ex = 1e3*(daed_vy*daed_Bz - daed_vz*daed_By)  # in V/m  
    Ey = 1e3*(daed_vz*daed_Bx - daed_vx*daed_Bz)  # in V/m
    Ez = 1e3*(daed_vx*daed_By - daed_vy*daed_Bx)  # in V/m

    Etot = np.sqrt(Ex*Ex + Ey*Ey + Ez*Ez)         # in V/m
    
    # Plotting Data
    if var_to_plot== "":
        plot_along_orbit(Ex  ,1  ,"Ex $(V/m)$","Motional Ex")
        plot_along_orbit(Ey  ,2  ,"Ey $(V/m)$","Motional Ey")
        plot_along_orbit(Ez  ,3  ,"Ez $(V/m)$","Motional Ez")
        plot_along_orbit(Etot  ,4  ,"Et $(V/m)$","Motional E total")
    else:

        plot_along_orbit(Orbit_Data[var_to_plot],1 ,label_y,title)
    # ******************************************************************************************

    if Save_Products==True:
        # Export Products for PIC initialization to CSV
        Exports={'Time (UTCG)':daed_time,'Ex (V/m)':Ex,'Ey (V/m)':Ey,
                    'Ez (V/m)':Ez,'Etot (V/m)':Etot}



        df = DataFrame(Exports, columns= ['Time (UTCG)', 'Ex (V/m)','Ey (V/m)','Ez (V/m)','Etot (V/m)'])
        export_csv = df.to_csv ("data/"+ outfile + '.csv', index = None, header=True)
    # ******************************************************************************************

    return

## Example Call
from motionalE import *
file_IGRF="Orbit_IGRF_all.csv"
outfile="MotionalE"
Save_Products=False
Plot_Products=True
# Plot_All=False
var_to_plot=""
label_y="mV/m"
title="Motional E Along Orbit"
main(file_IGRF,outfile,Save_Products,var_to_plot,Plot_Products,label_y,title)