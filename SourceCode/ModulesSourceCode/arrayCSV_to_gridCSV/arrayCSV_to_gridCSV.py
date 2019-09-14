import csv
import numpy as np

"""

"""
def arrayCSV_to_gridCSV( InputFilenameCSV ):
    
	if InputFilenameCSV is None:
		return None
	if len(InputFilenameCSV) == 0:
		return ""
    
	outCSVfilename = InputFilenameCSV[0:-4] + "_grid" +".csv"

	# read the csv file. format: (time lat lon alt value)
	CSVreader = csv.reader( open( InputFilenameCSV ) )
	next( CSVreader ) # ignore the csv header
	Data =  [r[1:] for r in CSVreader] # read the rest CSV file at once into a 2D list. Ignore first column which is the time
	Data = np.array( Data, dtype=np.float64 ) # convert to 2D numpy array
	
	# TODO: Look at the data and find out the step for lat and lon values
	LatStep  = 5
	LonStep  = 5
	
	Lat = np.arange(   87.5,  -88.5,  -1*LatStep )
	Lon = np.arange( -180.0,  180.0,     LonStep )
	
	f = open( outCSVfilename, "w")
	for i in range(0, len(Lat)):
		for j in range(0, len(Lon)):
			for x in range(0, len(Data)):
				#if i==1: print(Data[x,0] , Lat[i]  )
				if( Data[x,0] == Lat[i]  and  Data[x,1] == Lon[j] ):
					if j>0: f.write( ", " )
					f.write( str(Data[x,3]) )
		f.write( "\n" )
	f.close()
	
	return outCSVfilename


# example of usage:
#arrayCSV_to_gridCSV( "../../DataFiles/sphere_IRIresult.csv" )