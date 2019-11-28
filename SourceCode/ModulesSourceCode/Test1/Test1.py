
import SourceCode.ModulesSourceCode.PlotGlobe.PlotGlobe as PlotGlobe
import numpy as np

def Test1():
    print( "Creating..." )
    #s = PlotGlobe.PlotGlobe( "DAED_ORB_Evt0_LLA_Per120_Lat00_Srt01Hz_Msc.csv", "../../DataFiles/orbit_IRIresult.csv", "ne iri16", "cm^-3", "Jet" )
    #s = PlotGlobe.PlotGlobe( "", "../../DataFiles/orbit_IRIresult.csv", "Electron Density currents", "cm^-3", "Jet" )
    #s = PlotGlobe.PlotGlobe( "../../DataFiles/sphere_IRIresult.csv", "", "Electron Density currents", "cm^-3", "Jet" )
    #s = PlotGlobe.PlotGlobe( "sphere_IRI16_cities.csv", "", "Electron Density currents", "cm^-3", "Jet" )

    #s = PlotGlobe.PlotGlobe( "Surface.nc", "ALFA", "cm^-3", "Jet",    "Orbit.nc", "ALFA", "cm^-3", "Jet",    "Electron Density currents" )
    #s = PlotGlobe.PlotGlobe( "sphere_IRI16_cities.csv", "Te_iri16_K", "cm^-3", "Jet",   "Orbit.nc", "Oxygen", "cm^-3", "Jet",   "Electron Density currents" )

    #s = PlotGlobe.PlotGlobe( "/home/NAS/Data_Files/Temp/Surface.nc", "ALFA", "NO", "Jet",    "", "ALFA", "cm^-3", "Jet",    "O2" )

    s = PlotGlobe.PlotGlobe( "", "O2", "nT", "Jet",    "", "ALFA", "cm^-3", "Jet",    "Magnetic Field (nT)", "/home/NAS/TIEGCM_DATA/TIEGCM_EF/E_field_TIEGCMnew.nc", "B", "nT", "Jet" )

    s = PlotGlobe.PlotGlobe( "/home/NAS/TIEGCM_DATA/TIEGCM_EF/E_field_TIEGCMnew.nc", "Ephi", "V/m", "Jet",    "", "ALFA", "cm^-3", "Jet",    "Electic Field", "/home/NAS/TIEGCM_DATA/TIEGCM_EF/E_field_TIEGCMnew.nc", "E", "E", "gray",SurfaceOpacity=1  )

    s = PlotGlobe.PlotGlobe( "/home/NAS/TIEGCM_DATA/TIEGCM_EVT1_2015_StPatricksDay_HAO/tiegcm_dres.s_mar2015_amie_v1_01.nc", "UN", "cm/s", "Jet",    "", "ALFA", "cm^-3", "Jet",    "Neutral Winds", SurfaceOpacity=1 )

    s = PlotGlobe.PlotGlobe( "/home/NAS/TIEGCM_DATA/TIEGCM_EF/tiegcm_dres.s_mar2015_amie_v1_01_JH.nc", "Joule_Heating", "W/m^3", "Jet",    "/home/NAS/TIEGCM_DATA/TIEGCM_EF/Daedalus_Interpolator_JH.nc", "Joule_Heating", "W/m^3", "Jet",    "Joule Heating", SurfaceOpacity=1 )

    print(s)
    return s
