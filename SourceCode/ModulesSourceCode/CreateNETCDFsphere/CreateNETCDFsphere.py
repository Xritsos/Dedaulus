

from netCDF4 import Dataset  # https://unidata.github.io/netcdf4-python/netCDF4/index.html
from datetime import datetime
import numpy as np
import shutil 

'''
Creates a NetCDF file 
Time and Alt are fixed values given as arguments and Lat and Lon are produced for the whole globe accodring to steps specified.
CDFfilename: string, the filename to be written (overwrite mode)
fixedDatetimeString: string, the date-time fixed text with format as example: "Mar 17 2015 00:12:00.000000000". Fixed value for every entry. If this is an empty string then no file is created and empty string and zeros are returned.
fixedAltitude: float positive, kilometers above earth. Fixed value for every entry.
LatitudeStep: float positive, Latiude values range between 87.5 and -88.5. The step is how Lat should be incremented at each iteration.
LongitudeStep: float positive, Longitude values range between -180 and 180.  The step is how Lon should be incremented at each iteration.
RETURNS: the filename it has written (same as the argument)
         the altitude (same as the argument)
'''
def CreateNETCDFsphere( CDFfilename, fixedDatetimeString, fixedAltitude, LatitudeStep, LongitudeStep ):
    # convert the Time-string to Unix Timestamp
    aTimeString = fixedDatetimeString[:-6] + " " + "+0000" # indicate explicity that this is UTC time
    TimeObj = datetime.strptime( aTimeString, "%b %d %Y %H:%M:%S.%f %z" ) 
    FixedTimestamp = float( datetime.timestamp(TimeObj) ) * 1000  # timestamp in milliseconds

    # copy the standard surface file to a temporary location, where we will process it
    shutil.copyfile( "SurfaceTemplate.nc", CDFfilename )

    # open file
    CDFroot =  Dataset( CDFfilename, "a")

    # update general attributes
    CDFroot.Type = "surface"
    CDFroot.Calculated = "no" # reset state
    CDFroot.ResetTime = str(datetime.now()) # log

    # fill with pre-fabricated data for all Latitude-Lonitude pairs according to their respective steps
    n = 0;
    for i in np.arange(87.5, -92.5, -5.0):
        for j in np.arange(-180.0,  180.0, 5.0):
            CDFroot.variables["lat"][n] = i + 0.00000001*n
            CDFroot.variables["lon"][n] = j + 0.00000001*n
            #print( round(float(CDFroot.variables["lat"][n]),2), "    ",  round(float(CDFroot.variables["lon"][n]),2) )
            CDFroot.variables["time"][n] = FixedTimestamp + n
            CDFroot.variables["level"][n] = fixedAltitude
            CDFroot.variables["ALFA"][n] = np.random.random_sample() # assign random values for test purposes
            n = n + 1

    # close file
    CDFroot.close() 
    
    
    
    #CDFroot = Dataset( CDFfilename, 'r' )
    #print( CDFroot.variables["lat"][:] )
    #CDFroot.close()
    
       
    return  CDFfilename, fixedAltitude
