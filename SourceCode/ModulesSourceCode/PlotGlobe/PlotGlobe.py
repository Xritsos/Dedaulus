'''
The source code of this file is based on https://plot.ly/~empet/14813/heatmap-plot-on-a-spherical-map/#/
The main function of this file is PlotGlobe. The others are ancillary.

Notes
-----
We can add these plot types to Plotables:
    'area', 'bar', 'barpolar', 'box', 'candlestick', 'carpet', 'choropleth', 'cone', 'contour', 'contourcarpet', 
    'funnel', 'funnelarea', 'heatmap', 'heatmapgl', 'histogram', 'histogram2d', 'histogram2dcontour', 'isosurface', 
    'mesh3d', 'ohlc', 'parcats', 'parcoords', 'pie', 'pointcloud', 'sankey', 'scatter', 'scatter3d', 'scattercarpet', 
    'scattergeo','scattergl', 'scattermapbox', 'scatterpolar','scatterpolargl', 'scatterternary', 'splom', 'streamtube', 
    'sunburst', 'surface', 'table', 'violin', 'volume', 'waterfall'

'''

from numpy import pi, sin, cos
import time
from netCDF4 import Dataset  # https://unidata.github.io/netcdf4-python/netCDF4/index.html
from netCDF4 import MFDataset
import plotly
# import plotly.plotly as py
import chart_studio.plotly as py
import csv
import numpy as np           
from scipy.io import netcdf  
from mpl_toolkits.basemap import Basemap
import warnings

EarthRadius = 6378.137 # km - global, its value will not change through out the code
LatStep  =  5 # global - its value will change after parsing the surface file. It will be declared as global inside the fnctions.
LonStep  =  5 # global - its value will change after parsing the surface file. It will be declared as global inside the fnctions.

# from plot.ly - convert degrees to radians
def degree2radians(degree):    
    return degree*pi/180

# from plot.ly - maps the points of coords (lon, lat) to points onto the sphere of radius radius
def mapping_map_to_sphere(lon, lat, radius=1):  
    lon=np.array(lon, dtype=np.float64)
    lat=np.array(lat, dtype=np.float64)
    lon=degree2radians(lon)
    lat=degree2radians(lat)
    xs=radius*cos(lon)*cos(lat)
    ys=radius*sin(lon)*cos(lat)
    zs=radius*sin(lat)
    return xs, ys, zs

# Make shortcut to Basemap object, not specifying projection type
m = Basemap() 

# from plot.ly - Functions converting coastline/country polygons to lon/lat traces
# pos arg 1. (poly_paths): paths to polygons
# pos arg 2. (N_poly): number of polygon to convert
def polygons_to_traces(poly_paths, N_poly):
    # init. plotting list
    lons=[]
    lats=[]
    for i_poly in range(N_poly):
        poly_path = poly_paths[i_poly]
        # get the Basemap coordinates of each segment
        coords_cc = np.array(
            [(vertex[0],vertex[1]) for (vertex,code) in poly_path.iter_segments(simplify=False)]
        )
        # convert coordinates to lon/lat by 'inverting' the Basemap projection
        lon_cc, lat_cc = m(coords_cc[:,0],coords_cc[:,1], inverse=True)
        lats.extend(lat_cc.tolist()+[None]) 
        lons.extend(lon_cc.tolist()+[None])
    return lons, lats

# from plot.ly - Function generating coastline lon/lat 
def get_coastline_traces():
    poly_paths = m.drawcoastlines().get_paths() # coastline polygon paths
    N_poly = 91  # use only the 91st biggest coastlines (i.e. no rivers)
    cc_lons, cc_lats= polygons_to_traces(poly_paths, N_poly)
    return cc_lons, cc_lats

# from plot.ly - Function generating country lon/lat 
def get_country_traces():
    poly_paths = m.drawcountries().get_paths() # country polygon paths
    N_poly = len(poly_paths)  # use all countries
    country_lons, country_lats= polygons_to_traces(poly_paths, N_poly)
    return country_lons, country_lats

###############

'''
Creates a 3D plot of an earth globe. Can plot a sphere surface and/or a satellite orbit. 
The surface and the orbit are colored according to the selected variable values in the data files. 
The data files can be of CSV o NetCDF4 format.
The same or different variables can be selected for plotting at the surface and the orbit.
The same or different colorscales can be selected for the surface and the orbit.
The same or different value range can be selected for the surface and the orbit by assigning the same or different colorbar titles.
Valid Colorscale Names: ‘Blackbody’, ‘Bluered’, ‘Blues’, ‘Earth’, ‘Electric’, ‘Greens’, ‘Greys’, ‘Hot’, ‘Jet’, ‘Picnic’, ‘Portland’, ‘Rainbow’, ‘RdBu’, ‘Reds’, ‘Viridis’, ‘YlGnBu’, ‘YlOrRd’
ARGUMENTS:
  SurfaceFilename: The file which contains data for a surface. If empty string then no surface will be plotted. 
                   CSV format: Time,Lat,Lon,Alt,value. Contains the data for the sphere surface. 
                   NetCDF format: see Daedalus User Manual
  SurfaceVariableToPlot: The name of the variable to read from the surface data file and plot upon the globe.
  SurfaceColorbarTitle: A title to display above the colorbar which refers to the surface data
  SurfaceColorscaleName: The name of the Colorscale to use for the surface data. 
                         In case an empty string is passed then a default HeatMap colorscale will be applied.
                         In case None is passed then all points will be black irrespective of value.
  OrbitFilename: counterpart of the corresponding argument for the Surface data
  OrbitVariableToPlot: counterpart of the corresponding argument for the Surface data 
  OrbitColorbarTitle: counterpart of the corresponding argument for the Surface data 
  OrbitColorscaleName: counterpart of the corresponding argument for the Surface data
  PlotTitle: A title which is displayed on the top of the plot.
RETURNS: a string containing information about the Data
'''
def PlotGlobe( SurfaceFilename, SurfaceVariableToPlot, SurfaceColorbarTitle, SurfaceColorscaleName, OrbitFilename, OrbitVariableToPlot, OrbitColorbarTitle, OrbitColorscaleName, PlotTitle ):
    result = ""
    startSecs = time.time()
    
    # define colorscales for ploting
    colorscaleWhite=[[0.0, '#ffffff'], [1.0, '#ffffff']]
    colorscaleBlack=[[0.0, '#000000'], [1.0, '#000000']]
    if SurfaceColorscaleName is None:
        SurfaceColorscaleName = colorscaleBlack
    elif len( SurfaceColorscaleName ) == 0: 
        SurfaceColorscaleName=[[0.0, '#313695'], [0.07692307692307693, '#3a67af'], [0.15384615384615385, '#5994c5'], [0.23076923076923078, '#84bbd8'], [0.3076923076923077, '#afdbea'], [0.38461538461538464, '#d8eff5'], [0.46153846153846156, '#d6ffe1'], [0.5384615384615384, '#fef4ac'], [0.6153846153846154, '#fed987'], [0.6923076923076923, '#fdb264'], [0.7692307692307693, '#f78249'], [0.8461538461538461, '#e75435'], [0.9230769230769231, '#cc2727'], [1.0, '#a50026']]
    if OrbitColorscaleName is None:
        OrbitColorscaleName = colorscaleBlack
    elif len( OrbitColorscaleName ) == 0: 
        OrbitColorscaleName=[[0.0, '#313695'], [0.07692307692307693, '#3a67af'], [0.15384615384615385, '#5994c5'], [0.23076923076923078, '#84bbd8'], [0.3076923076923077, '#afdbea'], [0.38461538461538464, '#d8eff5'], [0.46153846153846156, '#d6ffe1'], [0.5384615384615384, '#fef4ac'], [0.6153846153846154, '#fed987'], [0.6923076923076923, '#fdb264'], [0.7692307692307693, '#f78249'], [0.8461538461538461, '#e75435'], [0.9230769230769231, '#cc2727'], [1.0, '#a50026']]
        
        
    #### create the earth surface
    # construct the values for longitude and latitude
    global LatStep
    global LonStep
    if len(SurfaceFilename) > 0:        
        LatStep, LonStep = CalculateLatLonSteps( SurfaceFilename )
    lat = np.arange(   87.5,  -88.5, -LatStep )
    lon = np.arange( -180.0,  180.0,  LonStep )
    # To ensure color continuity we extend the lon list with [180] (its last value was lon[-1]=177.5). In this way we can identify lon=-180 with lon=180.
    # We do the same with latitudes. We extend both directions with [90] and [-90] in order to have values for the poles.
    clons = np.array( lon.tolist() + [180]        , dtype=np.float64)
    clats = np.array( [90] + lat.tolist() + [-90] , dtype=np.float64)
    clons, clats=np.meshgrid(clons, clats)
    earthX, earthY, earthZ = mapping_map_to_sphere(clons, clats, radius=EarthRadius)
    earthS = np.zeros(clons.shape, dtype=np.float64)
    EarthSurface=dict(type='surface',
        x = earthX, y = earthY, z = earthZ,
        colorscale = colorscaleWhite, surfacecolor = earthS,
        showscale = False, cmin=-20, cmax=20,
    )

    # Get list of of coastline, country, and state lon/lat and concatenate them
    coastline_lons, coastline_lats = get_coastline_traces()
    country_lons, country_lats = get_country_traces()
    boundaries_lons = coastline_lons+[None]+country_lons
    boundaries_lats = coastline_lats+[None]+country_lats
    boundaries_dataX, boundaries_dataY, boundaries_dataZ = mapping_map_to_sphere(boundaries_lons, boundaries_lats, radius = EarthRadius+0.1) # radius is slightly greater than 1 to ensure lines visibility
    # create the visual element of the world map
    Boundaries=dict(type='scatter3d',
        x=boundaries_dataX, y=boundaries_dataY, z=boundaries_dataZ,
        mode='lines', name= "", showlegend=False, line=dict(color='black', width=1)
    )    
    
    # define the layout of the plot
    theLayout = dict(
        title = PlotTitle,
        scene = dict(
            xaxis = dict( zeroline=False ), yaxis = dict( zeroline=False ), zaxis = dict( zeroline=False ),
            aspectratio=dict(x=1, y=1,z=1), camera=dict(eye=dict(x=1.20, y=1.20, z=1.20))
        )
    )
    
    #### read the surface Data file and find the Altitude of the surface described by the data file
    Altitude = CalculateAltitudeFromData( SurfaceFilename )
        
    #### read the Data file into an Array
    SurfaceData =  SurfaceFile_to_array( SurfaceFilename, SurfaceVariableToPlot ) 
    
    #### read the Orbit Data file into an Array
    OrbitData =  OrbitFile_to_array( OrbitFilename, OrbitVariableToPlot) 
   
    #### Calculate min / max values of all plotable data 
    # calculate min/max for the surface data
    if len(SurfaceFilename) > 0:
        SurfaceMin = np.amin(SurfaceData)
        SurfaceMax = np.amax(SurfaceData)
    # calculate min/max for the orbit data
    if len(OrbitFilename) > 0:
        OrbitMin = np.amin( OrbitData[:,3] )
        OrbitMax = np.amax( OrbitData[:,3] )
    # combine if necessary
    if len(SurfaceFilename) > 0  and  len(OrbitFilename) > 0:
        if SurfaceVariableToPlot==OrbitVariableToPlot and SurfaceColorbarTitle==OrbitColorbarTitle: # user is ploting the same variable, so use a global min/max
            SurfaceMin = min( SurfaceMin, OrbitMin) 
            SurfaceMax = max( SurfaceMax, OrbitMax)
            OrbitMin = SurfaceMin
            OrbitMax = SurfaceMax
            
    # add all visual elements in a list and assign them to a figure
    Plotables = list()
    Plotables.append( EarthSurface )
    Plotables.append( Boundaries )
    if len(SurfaceFilename) > 0:
        Plotables.append( CreatePlotable_Surface(SurfaceData, Altitude, SurfaceMin, SurfaceMax, SurfaceColorscaleName, SurfaceColorbarTitle) )        
    if len(OrbitFilename) > 0:
        Plotables.append( CreatePlotable_Orbit(OrbitData, OrbitMin, OrbitMax, OrbitColorscaleName, OrbitColorbarTitle) )

    fig = dict( data=Plotables, layout=theLayout )
    # plot all
    plotly.offline.init_notebook_mode(connected=True)
    plotly.offline.iplot(fig)
    
    finishSecs = time.time()
    # be verbose
    #result = result + "Lon shape: " + str(lon.shape) + "  Lat shape: " + str(lat.shape) + "  Data shape: " + str(Data.shape) + "\n"
    if len(SurfaceFilename) > 0: result = result + "Data Min: " + str(SurfaceMin) + "  Data Max: " + str(SurfaceMax) + "\n"
    if len(OrbitFilename) > 0: result = result + "Orbit Min: " + str(OrbitMin) + "  Orbit Max: " + str(OrbitMax) + "\n"
    if len(OrbitFilename) > 0: result = result + "Number of Orbit positions: "  + str(len(OrbitData)) + "\n"    
    result = result + "Plot creation duration: " + str(finishSecs-startSecs) + " seconds.\n"
    return result;


###################################################################################################
###################################################################################################
###################################################################################################

#### parse the data file and find the Altitude of the surface described
# Arguments:
#    SurfaceFilename: the filename containing the data for the surface. Can be in csv or netCDF format.
# Returns: the Altitude (float)
def CalculateAltitudeFromData( SurfaceFilename ):
    if len(SurfaceFilename) == 0:
        result = 0
    elif SurfaceFilename.endswith( ".csv" ):
        with open(SurfaceFilename) as CSVfile:
            CSVreader = csv.reader( CSVfile )
            next( CSVreader ) # ignore the csv header
            result = float(   next( CSVreader )[3]   )
    else:
        CDFroot = Dataset( SurfaceFilename, 'r' )
        #result = float( CDFroot.Elevation )
        result = CDFroot.variables["level"][0]
        if result==0: 
            result = 2
        CDFroot.close()
    ##
    return result


# Calculates the step between succesive values of Latitudes and Longitudes as stored inside the surface file.
# The steps are absolute values, always positive.
# Different step values lead to smaller or bigger arrays which hold the surface data and display the plot.
# This function enables the automation of such an adjustment.
# Arguments:
#    SurfaceFilename: the filename containing the data for the surface. Can be in csv or netCDF format.
# Returns 2 floats: the LatitudeStep and the LongitudeStep
def CalculateLatLonSteps( SurfaceFilename ):
    theLatStep = -5
    theLonStep =  5
    if len(SurfaceFilename) == 0:
        return
    elif SurfaceFilename.endswith( ".csv" ):
        with open(SurfaceFilename) as CSVfile:
            CSVreader = csv.reader( CSVfile ) # read the csv file. format: (time lat lon alt value)
            next( CSVreader ) # ignore header
            # read data
            RawData =  [r[1:] for r in CSVreader] # read the rest file into a 2D list. Ignore 1st column (time).
            RawData = np.array( RawData, dtype=np.float64 ) # convert to 2D numpy array
            # calculate Latitude step
            Lats = np.unique( RawData[:,0:1] )
            theLatStep = abs( Lats[0] - Lats[1] )
            # calculate Longitude step
            Lons = np.unique( RawData[:,1:2] )
            theLonStep = abs( Lons[0] - Lons[1] )
    else: 
        CDFroot = Dataset( SurfaceFilename, 'r' )
        if "(unlimited)" in str(CDFroot.dimensions["lat"]):
            # calculate Latitude step
            Lats = CDFroot.variables["lat"][:]
            for i in range(0, len(Lats)):
                Lats[i] = round( Lats[i], 2 )
            Lats = np.unique( Lats )
            theLatStep = abs( Lats[0] - Lats[1] )
            # calculate Longitude step
            Lons = CDFroot.variables["lon"][:]
            for i in range(0, len(Lons)):
                Lons[i] = round( Lons[i], 2 )
            Lons = np.unique( Lons )
            theLonStep = abs( Lons[0] - Lons[1] )            
        else:
            # calculate Latitude step
            Lats = CDFroot.variables["lat"][:]
            theLatStep = abs( Lats[0] - Lats[1] )
            # calculate Longitude step
            Lons = CDFroot.variables["lon"][:]
            theLonStep = abs( Lons[0] - Lons[1] )
        CDFroot.close()
    return theLatStep, theLonStep




#### read the values of the surface data file into a 2D Array
# Arguments:
#    SurfaceFilename: the filename containing the data for the surface. Can be in csv or netCDF format.
#    VariableName: the name of the variable which will be plotted. The file may contain values for several variables.
# Returns: a 2D array containing the data to be plotted. The item Data[0,0] represents the value at Lat=87.5 and Lon=-180 etc.
def SurfaceFile_to_array( SurfaceFilename, VariableName ):
    global LatStep
    global LonStep
    if len(SurfaceFilename) == 0:
        DataGrid = None
    elif SurfaceFilename.endswith( ".csv" ):
        with open(SurfaceFilename) as CSVfile:
            CSVreader = csv.reader( open( SurfaceFilename ) ) # read the csv file. format: (time lat lon alt value)
            # read csv header to resolve the column number which corresponds to VariableName
            VariableColumn = 3 # use the 1st column containing variable values as default
            HeaderTitles = next( CSVreader )
            for i in range(0, len(HeaderTitles)):
                if HeaderTitles[i] == VariableName:
                    VariableColumn = i - 1 # we subtract by 1 because we will throw away the time column (the 1st column)
            # read the rest file into a 2D array. 
            RawData =  [r[1:] for r in CSVreader] # Ignore 1st column (time). -> get lat,lon,elevation,values
            RawData = np.array( RawData, dtype=np.float64 ) # convert to 2D numpy array
            # construct a 2D array like a grid wirh Lat and Lon axis with the variable's values inside
            Lat = np.arange(   87.5,  -88.5,  -LatStep )
            Lon = np.arange( -180.0,  180.0,   LonStep )
            DataGrid = np.zeros( (len(Lat), len(Lon)), dtype=np.float64 )
            for i in range(0, len(Lat)):
                for j in range(0, len(Lon)):
                    for x in range(0, len(RawData)):
                        if( RawData[x,0] == Lat[i]  and  RawData[x,1] == Lon[j] ):
                            DataGrid[i, j] = RawData[x, VariableColumn]
                            break
    else: 
        CDFroot = Dataset( SurfaceFilename, 'r' )
        if "(unlimited)" in str(CDFroot.dimensions["lat"]): # surface's file format is the same as the orbit's
            # read the NetCDF file into a 2D array with columns lat,lon,elevation,values
            RawData = np.vstack( (CDFroot.variables["lat"][:], CDFroot.variables["lon"][:], CDFroot.variables["level"][:], CDFroot.variables[VariableName][:] ) ).T
            # Round lat and lon columns to remove small variations which trick Panoply to see different values and plot the surface
            for i in range(0, len(RawData)):
                RawData[i, 0] = round( RawData[i, 0], 2 )
                RawData[i, 1] = round( RawData[i, 1], 2 )
            # construct a 2D array like a grid wirh Lat and Lon axis with the variable's values inside
            Lat = np.arange(   87.5,  -88.5,  -LatStep )
            Lon = np.arange( -180.0,  180.0,   LonStep )
            DataGrid = np.zeros( (len(Lat), len(Lon)), dtype=np.float64 )
            for i in range(0, len(Lat)):
                for j in range(0, len(Lon)):
                    for x in range(0, len(RawData)):
                        if( RawData[x,0] == Lat[i]  and  RawData[x,1] == Lon[j] ):
                            DataGrid[i, j] = RawData[x, 3]
                            break
        else: # the Panoply-oriented format for surfaces is used
            DataGrid = CDFroot.variables[VariableName][:] 
        CDFroot.close()
    ##
    return DataGrid



#### read the values of the orbit data file into a 1D Array
#    SurfaceFilename: the filename containing the data for the surface. Can be in csv or netCDF format.
#    VariableName: the name of the variable which will be plotted. The file may contain values for several variables.
# Returns: a 2D array containing the data to be plotted, with columns Lat,Lon,Elevation,Value
def OrbitFile_to_array( OrbitFilename, VariableName ):
    if len(OrbitFilename) == 0:
        OrbitData = None
    elif OrbitFilename.endswith( ".csv" ):    
        orbitCSVreader = csv.reader( open( OrbitFilename ) )
        next( orbitCSVreader ) # ignore the csv header
        OrbitData =  [r[1:5] for r in orbitCSVreader if len(r[4])>0] # read the rest CSV file at once into a 2D list. Ignore first column which is the time and take only the first value in case there are more. Ignore lines without value, as well.
        OrbitData = np.array( OrbitData, dtype=np.float64 ) # convert to 1D numpy array
    else:
        CDFroot = Dataset( OrbitFilename, 'r' )
        OrbitData = np.vstack( (CDFroot.variables["lat"][:], CDFroot.variables["lon"][:], CDFroot.variables["level"][:], CDFroot.variables[VariableName][:] ) ).T
        CDFroot.close()
    ##
    return OrbitData

###################################################################################################


# Creates a dictionary containing all information needed to Plotly in order to plot a spherical surface around the earth
# with data from the surface-data-file.
# Arguments:
#     Data: the data in 2D array to be plotted. The item Data[0,0] represents the value at Lat=87.5 and Lon=-180. This array can be cosntructed by the function SurfaceFile_to_array from a csv or netCDF file.
#     Altitude: the altitude of the sphere above sea level
#     MinValue: the minimum value of the data. Needed because there may be a global minimum calculated upon both the orbit and the surface data.
#     MaxValue: the maximum value of the data
#     ColorScale: the colorscale name. This changes the colors which will be displayed. The colors will correspond to the values and will ne in range between the min and max values
#     ColorbarTitle: the title which will be shows above the color-bar. This bar displays the colors and their corresponding values 
def CreatePlotable_Surface( Data, Altitude, MinValue, MaxValue , ColorScale, ColorbarTitle):
    # construct the values for longitude and latitude
    global LatStep
    global LonStep
    lat = np.arange(   87.5,  -88.5,  -LatStep ) # lat = np.arange(   87.5,  -88.5,  int(-180 / len(Data   ) ) )
    lon = np.arange( -180.0,  180.0,   LonStep ) # lon = np.arange( -180.0,  180.0,  int( 360 / len(Data[0]) ) ) 
    
    #### SHIFTING
    # Shift 'lon' from [0,360] to [-180,180]
    tmp_lon = np.array([lon[n]-360 if l>=180 else lon[n] for n,l in enumerate(lon)])  # => [0,180]U[-180,2.5]
    i_east, = np.where(tmp_lon>=0)  # indices of east lon
    i_west, = np.where(tmp_lon<0)   # indices of west lon
    lon = np.hstack((tmp_lon[i_west], tmp_lon[i_east]))  # stack the 2 halves
    # Correspondingly, shift the Data array
    Data_ground = np.array(Data)
    Data = np.hstack((Data_ground[:,i_west], Data_ground[:,i_east]))
    
    # cut out a pizza slice
    #for i in range (0,16):
    #    for j in range (0,16):
    #        Data[i,j] = float('nan')
    
    # To ensure color continuity we extend the lon list with [180] (its last value was lon[-1]=177.5). In this way we can identify lon=-180 with lon=180.
    # We do the same with latitudes. We extend both directions with [90] and [-90] in order to have values for the poles.
    clons = np.array( lon.tolist() + [180]        , dtype=np.float64)
    clats = np.array( [90] + lat.tolist() + [-90] , dtype=np.float64)
    clons, clats=np.meshgrid(clons, clats)
    # Map the meshgrids clons, clats onto the sphere
    XS, YS, ZS = mapping_map_to_sphere(clons, clats, radius=EarthRadius+Altitude)
    # for color continuity
    nrows, ncolumns=clons.shape
    DATA = np.zeros(clons.shape, dtype=np.float64)
    DATA[1:nrows-1, :ncolumns-1] = np.copy(np.array(Data,  dtype=np.float64)) # ignore the extended values
    DATA[1:nrows-1,  ncolumns-1] = np.copy(Data[:, 0]) # ignore the extended values

    # Create a sphere above earth which will be colored in accordance with the data
    DataSphere=dict(type='surface', x = XS,  y = YS,  z = ZS,
        colorscale = ColorScale, surfacecolor = DATA, opacity = 0.90,
        cmin = MinValue, cmax = MaxValue,
        colorbar=dict(thickness=20, len=0.75, ticklen=4, title=ColorbarTitle),
    )
    #if len(ColorbarTitle) == 0 : DataSphere["showscale"] = False

    return DataSphere
    

###########################################################################################################


# Creates a dictionary containing all information needed to Plotly in order to plot a spherical surface around the earth
# with data from the surface-data-file.
# Arguments:
#     Data: the data in 2D array to be plotted. The item Data[0,0] represents the value at Lat=87.5 and Lon=-180. This array can be cosntructed by the function SurfaceFile_to_array from a csv or netCDF file.
#     MinValue: the minimum value of the data. Needed because there may be a global minimum calculated upon both the orbit and the surface data.
#     MaxValue: the maximum value of the data
#     ColorScale: the colorscale name. This changes the colors which will be displayed. The colors will correspond to the values and will ne in range between the min and max values
#     ColorbarTitle: the title which will be shows above the color-bar. This bar displays the colors and their corresponding values 
def CreatePlotable_Orbit( OrbitData, MinValue, MaxValue, ColorScale, ColorbarTitle ):    
    # process orbit-data in order to plot them in relation with the globe: Convert lat,lon,alt to x,y,z
    for i in range(0, len(OrbitData)): OrbitData[i, 2] = OrbitData[i, 2] + EarthRadius # form radius from earth center using altitude
    tmplon = degree2radians( OrbitData[:,1] )  
    tmplat = degree2radians( OrbitData[:,0] )    
    tmprad = OrbitData[:,2]
    OrbitX = tmprad * cos(tmplon) * cos(tmplat)
    OrbitY = tmprad * sin(tmplon) * cos(tmplat)
    OrbitZ = tmprad * sin(tmplat)
    # create the orbit scatter points for the plot
    OrbitScatter = dict( type = "scatter3d", mode = "markers", x = OrbitX,  y = OrbitY,  z = OrbitZ, showlegend = False, 
        marker = dict( 
            size=3, color = OrbitData[:,3], colorscale = ColorScale,  
            cmin = MinValue, cmax = MaxValue,
            colorbar=dict(thickness=20, len=0.75, ticklen=4, title=dict(text=ColorbarTitle,side="top"), xanchor="center", x=0) # x must be between [-2, 3]
        ),
    )
    return OrbitScatter


