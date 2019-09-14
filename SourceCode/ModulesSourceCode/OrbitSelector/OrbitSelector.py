"""
Constructs an orbit filename from the orbit properties.
The filename includes all parameters required to select the appropriate orbit.
All filenames  have the same length and same number of parameters. 
If OrbitFilename is provided then the rest arguments are ignored.
FORMAT: DAED_ORB_EVTXY_TYP_PERYYY_LATZZ_SRTQQHz_XSC.csv
DESCRIPTION:
  Parameter EvtXY values:
    EVTXS	 X Event, Single Orbit
    EVTXA    X Event, All Orbit
    EVT1Y    1st Event: St Patrick’s day event [17 Mar 2015 – 20 Mar 2015]
    EVT2Y    2nd Event
    EVT3Y    3rd Event
	...      ...
	
  Parameter TYP	values:
    LLA    Time,Latitude Longitude Altitude 
    VEL    Time,VmagVxVyVz
    PTG    Time, X_GSE, Y_GSE, Z_GSE, RamX_GSE, RamY_GSE, RamZ_GSE

  Parameter PerYYY	values:
    PER120    Perigee Altitude at 120km
    PER150    Perigee Altitude at 150km

  Parameter LatZZ values:
    LAT00    Perigee Latitude at 0°
    LAT40    Perigee Latitude at 40°
    LAT80    Perigee Latitude at 80°
	
  Parameter SRXXHZ values:
    SRT16Hz    Sampling rate 16Hz
    SRT01Hz    Sampling rate 1Hz
	
  Parameter SC values:
    MSC    Mother Spacecraft
    SSC    Sub-Spacecraft
"""
def OrbitSelector( OrbitFilename, EvtXY, TYP, PerYYY, LatZZ, SRXXHZ, SC ):
    if len(OrbitFilename)==0  and  len(EvtXY)==0 :
        return ""
    elif len(OrbitFilename) > 0:
        return "DataFiles/OrbitData/" + OrbitFilename
    else:
        return "DataFiles/OrbitData/" + "DAED_ORB_" + EvtXY + "_" + TYP + "_" + PerYYY + "_" + LatZZ + "_" + SRXXHZ + "_" + SC + ".csv"


