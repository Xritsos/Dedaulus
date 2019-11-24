'''
This file contains some global variables which the modules can use.
You can acess it after you type at your code: import SourceCode.DaedalusGlobals as DaedalusGlobals
In case you need some variable to be added here, please contact the Daedalus team.
'''


# Absolute path where the CSV filenames with the orbit data reside.
CSV_Files_Path = "/home/NAS/Data_Files/OrbitData/" 

# Absolute path where the NetCDF filenames with the orbit data reside.
NetCDF_Files_Path = "/home/NAS/Data_Files/OrbitData/" 


# Absolute path where the filenames with calculated values reside.
Processed_Files_Path = "/home/NAS/Data_Files/ModelOutputs/" 

# Absolute path where temporary filenames 
Temporary_Files_Path = "/home/NAS/Data_Files/Temp/" 


# Absolute path where the filenames with the interpolated values reside.
Interpolated_Files_Path = "/home/NAS/Data_Files/ModelOutputs/A_Interpolated/" 

# Absolute path where the filenames with the Synthetic Truth values reside.
# That is after Sub-Grid Variability is applied on the data.
SyntheticTruth_Files_Path = "/home/NAS/Data_Files/ModelOutputs/B_SyntheticTruth/" 

# Absolute path where the filenames with the Stimuli values reside.
# That is after Wake-Effects and Charging-Effects are applied on the data.
Stimuli_Files_Path = "/home/NAS/Data_Files/ModelOutputs/C_Stimuli/" 

# Absolute path where the filenames with the Synthetic Science values reside.
# That is after the results of the satellite instruments are applied on the data.
SyntheticScience_Files_Path = "/home/NAS/Data_Files/ModelOutputs/D_SyntheticScience/" 
