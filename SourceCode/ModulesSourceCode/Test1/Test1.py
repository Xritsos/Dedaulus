
import SourceCode.ModulesSourceCode.PlotGlobe.PlotGlobe as PlotGlobe
import numpy as np

def Test1():
    print( "Creating..." )

    # Plot Magnetic Field Unit Vectors 
    s = PlotGlobe.PlotGlobe( "", "O2", "nT", "Jet",    "", "ALFA", "cm^-3", "Jet",    "Magnetic Field (B unit)", "/home/NAS/TIEGCM_DATA/TIEGCM_EF/E_field_TIEGCMnew.nc", "B_Unit_x,B_Unit_y,B_Unit_z", "nT", None )
    
    # Plot Magnetic Field Vectors 
    s = PlotGlobe.PlotGlobe( "", "O2", "nT", "Jet",    "", "ALFA", "cm^-3", "Jet",    "Magnetic Field (B)", "/home/NAS/TIEGCM_DATA/TIEGCM_EF/E_field_TIEGCMnew.nc", "Bx,By,Bz", "nT", "Jet" )
    
    # Plot Electric Field Vectors
    #s = PlotGlobe.PlotGlobe( "", "Ephi", "V/m", "Jet",    "", "ALFA", "cm^-3", "Jet",    "Electic Field (data are Log10-scaled)", "/home/NAS/TIEGCM_DATA/TIEGCM_EF/E_field_TIEGCMnew.nc", "Ex,Ey,Ez", "V/m", "Jet",SurfaceOpacity=1  ) #s = PlotGlobe.PlotGlobe( "/home/NAS/TIEGCM_DATA/TIEGCM_EF/E_field_TIEGCMnew.nc", "Ephi", "V/m", "Jet",    "", "ALFA", "cm^-3", "Jet",    "Electic Field (data are Log10-scaled)", "/home/NAS/TIEGCM_DATA/TIEGCM_EF/E_field_TIEGCMnew.nc", "Ex,Ey,Ez", "V/m", "gray",SurfaceOpacity=1, LogScale=True  )
    
    # Plot Neutral Winds Vectors
    #s = PlotGlobe.PlotGlobe( "/home/NAS/TIEGCM_DATA/TIEGCM_EVT1_2015_StPatricksDay_HAO/tiegcm_dres.s_mar2015_amie_v1_01.nc", "UN", "cm/s", "Jet",    "", "ALFA", "cm^-3", "Jet",    "Neutral Winds", SurfaceOpacity=1 )
    
    # Plot Joule Heating
    s = PlotGlobe.PlotGlobe( "/home/NAS/TIEGCM_DATA/TIEGCM_EF/tiegcm_dres.s_mar2015_amie_v1_01_JH.nc", "Joule_Heating", "W/m^3", "Jet",    "/home/NAS/TIEGCM_DATA/TIEGCM_EF/Daedalus_Interpolator_JH.nc", "Joule_Heating", "W/m^3", "Jet",    "Joule Heating (data are Log10-scaled)", SurfaceOpacity=1, LogScale=True )

    
    print(s)
    return s
