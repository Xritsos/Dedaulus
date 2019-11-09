import ipywidgets as widgets


def Construct_MSISE00():
	#Create Containers
	MSISE00_Panel = widgets.Box()
	MSISE00_Panel.layout.overflow_x = 'scroll'
	MSISE00_Panel.layout.flex_flow = 'row'
	MSISE00_Panel.layout.display = 'flex'
	########
	## GUI code for module 'OrbitSelector'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	global WIDGET_OrbitSelector_Filename
	WIDGET_OrbitSelector_Filename = widgets.Text()
	WIDGET_OrbitSelector_Filename.description = 'Filename'
	WIDGET_OrbitSelector_Filename.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_Filename,)
	global WIDGET_OrbitSelector_EvtXY
	WIDGET_OrbitSelector_EvtXY = widgets.Dropdown( options=['', 'Evt0', 'Evt1', 'Evt2', 'Evt3', 'Evt4', 'Evt5', 'Evt6', 'Evt7', 'Evt8', 'Evt9'], description='Variable')
	WIDGET_OrbitSelector_EvtXY.description = 'EvtXY'
	WIDGET_OrbitSelector_EvtXY.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_EvtXY,)
	global WIDGET_OrbitSelector_TYP
	WIDGET_OrbitSelector_TYP = widgets.Dropdown( options=['LLA', 'VEL', 'PTG'], description='Variable')
	WIDGET_OrbitSelector_TYP.description = 'TYP'
	WIDGET_OrbitSelector_TYP.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_TYP,)
	global WIDGET_OrbitSelector_PerYYY
	WIDGET_OrbitSelector_PerYYY = widgets.Dropdown( options=['Per120', 'Per150'], description='Variable')
	WIDGET_OrbitSelector_PerYYY.description = 'PerYYY'
	WIDGET_OrbitSelector_PerYYY.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_PerYYY,)
	global WIDGET_OrbitSelector_LatZZ
	WIDGET_OrbitSelector_LatZZ = widgets.Dropdown( options=['Lat00', 'Lat40', 'Lat80'],  description='Variable')
	WIDGET_OrbitSelector_LatZZ.description = 'LatZZ'
	WIDGET_OrbitSelector_LatZZ.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_LatZZ,)
	global WIDGET_OrbitSelector_SRXXHZ
	WIDGET_OrbitSelector_SRXXHZ = widgets.Dropdown( options=['Srt16Hz', 'Srt01Hz'],  description='Variable')
	WIDGET_OrbitSelector_SRXXHZ.description = 'SRXXHZ'
	WIDGET_OrbitSelector_SRXXHZ.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_SRXXHZ,)
	global WIDGET_OrbitSelector_SC
	WIDGET_OrbitSelector_SC = widgets.Dropdown( options=['Msc', 'Ssc'],  description='Variable')
	WIDGET_OrbitSelector_SC.description = 'SC'
	WIDGET_OrbitSelector_SC.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_SC,)
	MSISE00_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	OrbitSelector_Btn = widgets.Button (
		description='OrbitSelector',
		tooltip="Constructs and returns an orbit full-path filename from the orbit properties.\nThe filename includes all parameters required to select the appropriate orbit.\nAll filenames  have the same length and same number of parameters. \nIn case OrbitFilename and EvtXY are empty then an empty string is returned.\nFILE FORMAT: DAED_ORB_EVTXY_TYP_PERYYY_LATZZ_SRTQQHz_XSC.csv\n  Parameter OrbitFilename:\n    If it is not empty then the rest arguments are ignored. \n    If it contains slashes then is is assumed it is a full path name and it is returned as it is.\n    If it does not contain slashes then the orbits path is added.\n    \n  Parameter EvtXY values:\n    EVTXS    X Event, Single Orbit\n    EVTXA    X Event, All Orbit\n    EVT1Y    1st Event: St Patrick’s day event [17 Mar 2015 – 20 Mar 2015]\n    EVT2Y    2nd Event ...  ...\n \n  Parameter TYP values:\n    LLA    Time,Latitude Longitude Altitude \n    VEL    Time,VmagVxVyVz\n    PTG    Time, X_GSE, Y_GSE, Z_GSE, RamX_GSE, RamY_GSE, RamZ_GSE\n  Parameter PerYYY values:\n    PER120, PER150    Perigee Altitude at 120km or 150km\n  Parameter LatZZ values:\n    LAT00, LAT40, LAT80    Perigee Latitude at 0°, 40° or 80°\n \n  Parameter SRXXHZ values:\n    SRT16Hz, SRT01Hz    Sampling rate 16Hz or 1HZ\n \n  Parameter SC values:\n    MSC    Mother Spacecraft\n    SSC    Sub-Spacecraft\n",
	)
	OrbitSelector_Btn.layout.min_width = '200px'
	OrbitSelector_Btn.style.button_color = 'YellowGreen'
	MSISE00_Panel.children += (OrbitSelector_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_OrbitSelector_OrbitFilename = widgets.Label(value='  --> OrbitFilename  ')
	WIDGET_OrbitSelector_OrbitFilename.layout.border = '1px dashed green'
	WIDGET_OrbitSelector_OrbitFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_OrbitSelector_OrbitFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_OrbitSelector_OrbitFilename,)
	MSISE00_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'MSISE00'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_MSISE00_CSVfilename_forOrbit = widgets.Label(value='  OrbitSelector.OrbitFilename --> CSVfilename_forOrbit  ')
	WIDGET_MSISE00_CSVfilename_forOrbit.layout.border = '1px dashed blue'
	WIDGET_MSISE00_CSVfilename_forOrbit.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_MSISE00_CSVfilename_forOrbit,)
	global WIDGET_MSISE00_Variable_forOrbit
	WIDGET_MSISE00_Variable_forOrbit = widgets.Dropdown( options=['', 'Tn', 'O','O2','N2', 'rho'], value='', description='Variable')
	WIDGET_MSISE00_Variable_forOrbit.description = 'Variable_forOrbit'
	WIDGET_MSISE00_Variable_forOrbit.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_MSISE00_Variable_forOrbit,)
	MSISE00_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	MSISE00_Btn = widgets.Button (
		description='MSISE00',
		tooltip="MSISE-90 (Mass Spectrometer - Incoherent Scatter) empirical model (MSISE)\nfilename: the CSV file to read. Format: Time,Alt,Lon,Lat. The file defines the coordinates for which the MSISE calculation will take place.\nParameter: selects which values to calculate. Possible values are:\n    ''   for all\n    'Tn'  for Neutral Temperature\n    'O' for Oxygen atoms\n    'O2' for Oxygen molecules\n    'N2' for Nitrogen molecules\n    'rho' for Mass Densities\nReturns: the name of the CSV file which contains the calculated values. Format: Time,Alt,Lon,Lat,Tn,O,O2,N2,rho",
	)
	MSISE00_Btn.layout.min_width = '200px'
	MSISE00_Btn.style.button_color = 'gold'
	MSISE00_Panel.children += (MSISE00_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_MSISE00_ObitResultCSV = widgets.Label(value='  --> ObitResultCSV  ')
	WIDGET_MSISE00_ObitResultCSV.layout.border = '1px dashed green'
	WIDGET_MSISE00_ObitResultCSV.layout.margin ='0px 40px 0px 0px' 
	WIDGET_MSISE00_ObitResultCSV.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_MSISE00_ObitResultCSV,)
	MSISE00_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'CreateCSV_Sphere'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	global WIDGET_CreateCSV_Sphere_CSVfilename
	WIDGET_CreateCSV_Sphere_CSVfilename = widgets.Text(value="")
	WIDGET_CreateCSV_Sphere_CSVfilename.description = 'CSVfilename'
	WIDGET_CreateCSV_Sphere_CSVfilename.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_CreateCSV_Sphere_CSVfilename,)
	global WIDGET_CreateCSV_Sphere_fixedDatetimeString
	WIDGET_CreateCSV_Sphere_fixedDatetimeString = widgets.Text(value="Mar 17 2015 00:50:00.000000000")
	WIDGET_CreateCSV_Sphere_fixedDatetimeString.description = 'fixedDatetimeString'
	WIDGET_CreateCSV_Sphere_fixedDatetimeString.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_CreateCSV_Sphere_fixedDatetimeString,)
	global WIDGET_CreateCSV_Sphere_fixedAltitude
	WIDGET_CreateCSV_Sphere_fixedAltitude = widgets.FloatText(value=120)
	WIDGET_CreateCSV_Sphere_fixedAltitude.description = 'fixedAltitude'
	WIDGET_CreateCSV_Sphere_fixedAltitude.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_CreateCSV_Sphere_fixedAltitude,)
	global WIDGET_CreateCSV_Sphere_LatitudeStep
	WIDGET_CreateCSV_Sphere_LatitudeStep = widgets.FloatText(value=5)
	WIDGET_CreateCSV_Sphere_LatitudeStep.description = 'LatitudeStep'
	WIDGET_CreateCSV_Sphere_LatitudeStep.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_CreateCSV_Sphere_LatitudeStep,)
	global WIDGET_CreateCSV_Sphere_LongitudeStep
	WIDGET_CreateCSV_Sphere_LongitudeStep = widgets.FloatText(value=5)
	WIDGET_CreateCSV_Sphere_LongitudeStep.description = 'LongitudeStep'
	WIDGET_CreateCSV_Sphere_LongitudeStep.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_CreateCSV_Sphere_LongitudeStep,)
	MSISE00_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	CreateCSV_Sphere_Btn = widgets.Button (
		description='CreateCSV_Sphere',
		tooltip="Creates a CSV file with the format [Time, Lat, Lon, Alt]\nTime and Alt are fixed values given as arguments and Lat and Lon are produced for the whole globe accodring to steps specified.\nCSVfilename: string, the csv filename to be written (overwrite mode)\nfixedDatetimeString: string, the date-time fixed text with format as example: Mar 17 2015 00:12:00.000. Fixed value for every csv entry.\nfixedAltitude: float positive, kilometers above earth. Fixed value for every csv entry.\nLatitudeStep: float positive, Latiude values range between 87.5 and -88.5. The step is how Lat should be incremented at each iteration.\nLongitudeStep: float positive, Longitude values range between -180 and 180.  The step is how Lon should be incremented at each iteration.\nRETURNS: the filename it has written (same as the argument)\n         the altitude (same as the argument)\n         the number of lines written",
	)
	CreateCSV_Sphere_Btn.layout.min_width = '200px'
	CreateCSV_Sphere_Btn.style.button_color = 'gold'
	MSISE00_Panel.children += (CreateCSV_Sphere_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_CreateCSV_Sphere_theCSVfilename = widgets.Label(value='  --> theCSVfilename  ')
	WIDGET_CreateCSV_Sphere_theCSVfilename.layout.border = '1px dashed green'
	WIDGET_CreateCSV_Sphere_theCSVfilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_CreateCSV_Sphere_theCSVfilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_CreateCSV_Sphere_theCSVfilename,)
	WIDGET_CreateCSV_Sphere_theAltitude = widgets.Label(value='  --> theAltitude  ')
	WIDGET_CreateCSV_Sphere_theAltitude.layout.border = '1px dashed green'
	WIDGET_CreateCSV_Sphere_theAltitude.layout.margin ='0px 40px 0px 0px' 
	WIDGET_CreateCSV_Sphere_theAltitude.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_CreateCSV_Sphere_theAltitude,)
	WIDGET_CreateCSV_Sphere_NumberOfLinesWritten = widgets.Label(value='  --> NumberOfLinesWritten  ')
	WIDGET_CreateCSV_Sphere_NumberOfLinesWritten.layout.border = '1px dashed green'
	WIDGET_CreateCSV_Sphere_NumberOfLinesWritten.layout.margin ='0px 40px 0px 0px' 
	WIDGET_CreateCSV_Sphere_NumberOfLinesWritten.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_CreateCSV_Sphere_NumberOfLinesWritten,)
	MSISE00_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'MSISE00'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_MSISE00_CSVfilename_forMeshgrid = widgets.Label(value='  CreateCSV_Sphere.theCSVfilename --> CSVfilename_forMeshgrid  ')
	WIDGET_MSISE00_CSVfilename_forMeshgrid.layout.border = '1px dashed blue'
	WIDGET_MSISE00_CSVfilename_forMeshgrid.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_MSISE00_CSVfilename_forMeshgrid,)
	global WIDGET_MSISE00_Variable_forMeshgrid
	WIDGET_MSISE00_Variable_forMeshgrid = widgets.Dropdown( options=['', 'Tn', 'O','O2','N2', 'rho'], value='', description='Variable')
	WIDGET_MSISE00_Variable_forMeshgrid.description = 'Variable_forMeshgrid'
	WIDGET_MSISE00_Variable_forMeshgrid.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_MSISE00_Variable_forMeshgrid,)
	MSISE00_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	MSISE00_Btn = widgets.Button (
		description='MSISE00',
		tooltip="MSISE-90 (Mass Spectrometer - Incoherent Scatter) empirical model (MSISE)\nfilename: the CSV file to read. Format: Time,Alt,Lon,Lat. The file defines the coordinates for which the MSISE calculation will take place.\nParameter: selects which values to calculate. Possible values are:\n    ''   for all\n    'Tn'  for Neutral Temperature\n    'O' for Oxygen atoms\n    'O2' for Oxygen molecules\n    'N2' for Nitrogen molecules\n    'rho' for Mass Densities\nReturns: the name of the CSV file which contains the calculated values. Format: Time,Alt,Lon,Lat,Tn,O,O2,N2,rho",
	)
	MSISE00_Btn.layout.min_width = '200px'
	MSISE00_Btn.style.button_color = 'gold'
	MSISE00_Panel.children += (MSISE00_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_MSISE00_MeshgridResultCSV = widgets.Label(value='  --> MeshgridResultCSV  ')
	WIDGET_MSISE00_MeshgridResultCSV.layout.border = '1px dashed green'
	WIDGET_MSISE00_MeshgridResultCSV.layout.margin ='0px 40px 0px 0px' 
	WIDGET_MSISE00_MeshgridResultCSV.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_MSISE00_MeshgridResultCSV,)
	MSISE00_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'PlotGlobe'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_PlotGlobe_CSVfilename_Meshgrid = widgets.Label(value='  MSISE00.MeshgridResultCSV --> CSVfilename_Meshgrid  ')
	WIDGET_PlotGlobe_CSVfilename_Meshgrid.layout.border = '1px dashed blue'
	WIDGET_PlotGlobe_CSVfilename_Meshgrid.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_PlotGlobe_CSVfilename_Meshgrid,)
	WIDGET_PlotGlobe_CSVfilename_Orbit = widgets.Label(value='  MSISE00.ObitResultCSV --> CSVfilename_Orbit  ')
	WIDGET_PlotGlobe_CSVfilename_Orbit.layout.border = '1px dashed blue'
	WIDGET_PlotGlobe_CSVfilename_Orbit.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_PlotGlobe_CSVfilename_Orbit,)
	global WIDGET_PlotGlobe_PlotTitle
	WIDGET_PlotGlobe_PlotTitle = widgets.Text()
	WIDGET_PlotGlobe_PlotTitle.description = 'PlotTitle'
	WIDGET_PlotGlobe_PlotTitle.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_PlotGlobe_PlotTitle,)
	global WIDGET_PlotGlobe_ColorbarTitle
	WIDGET_PlotGlobe_ColorbarTitle = widgets.Text()
	WIDGET_PlotGlobe_ColorbarTitle.description = 'ColorbarTitle'
	WIDGET_PlotGlobe_ColorbarTitle.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_PlotGlobe_ColorbarTitle,)
	global WIDGET_PlotGlobe_ColorscaleName
	WIDGET_PlotGlobe_ColorscaleName = widgets.Text(value="Jet")
	WIDGET_PlotGlobe_ColorscaleName.description = 'ColorscaleName'
	WIDGET_PlotGlobe_ColorscaleName.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_PlotGlobe_ColorscaleName,)
	MSISE00_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	PlotGlobe_Btn = widgets.Button (
		description='PlotGlobe',
		tooltip="Creates a 3D plot of an earth globe, a sphere surface and a satellite orbit. The surface and the orbit are colored according to the data values in the CSV files.\n  DataCSVfilename: format: Time,Lat,Lon,Alt,value. Contains the data for the sphere surface. If empty then no surface will be plotted.\n  OrbitDataCSVfilename: format: Time,Lat,Lon,Alt,value. Contains the data for the orbit. If empty then no orbit will be plotted.\n  PlotTitle: the title of the plot. It will be displayed at the top of the globe.\n  ColorbarTitle: the title of the colorbar beside the globe. Usually contains measuremnt units\n  ColorscaleName: valid values are: ‘Blackbody’, ‘Bluered’, ‘Blues’, ‘Earth’, ‘Electric’, ‘Greens’, ‘Greys’, ‘Hot’, ‘Jet’, ‘Picnic’, ‘Portland’, ‘Rainbow’, ‘RdBu’, ‘Reds’, ‘Viridis’, ‘YlGnBu’, ‘YlOrRd’\n                  In case an empty string is passed then a default HeatMap colorscale will be applied.\n                  In case None is passed then all points will be black irrespective of value.\n  RETURNS: a string containing information about the Data",
	)
	PlotGlobe_Btn.layout.min_width = '200px'
	PlotGlobe_Btn.style.button_color = 'deeppink'
	MSISE00_Panel.children += (PlotGlobe_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	MSISE00_Panel.children += (OutputsPanel,)
	return MSISE00_Panel


def Construct_TopLevel():
	#Create Containers
	TopLevel_Panel = widgets.Box()
	TopLevel_Panel.layout.overflow_x = 'scroll'
	TopLevel_Panel.layout.flex_flow = 'row'
	TopLevel_Panel.layout.display = 'flex'
	########
	## GUI code for module 'OrbitSelector'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	global WIDGET_OrbitSelector_Filename
	WIDGET_OrbitSelector_Filename = widgets.Text("DAED_ORB_Evt0_LLA_Per150_Lat80_Srt01Hz_Msc.csv")
	WIDGET_OrbitSelector_Filename.description = 'Filename'
	WIDGET_OrbitSelector_Filename.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_Filename,)
	global WIDGET_OrbitSelector_EvtXY
	WIDGET_OrbitSelector_EvtXY = widgets.Dropdown( options=['Evt0', 'Evt1', 'Evt2', 'Evt3', 'Evt4', 'Evt5', 'Evt6', 'Evt7', 'Evt8', 'Evt9'], description='Variable')
	WIDGET_OrbitSelector_EvtXY.description = 'EvtXY'
	WIDGET_OrbitSelector_EvtXY.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_EvtXY,)
	global WIDGET_OrbitSelector_TYP
	WIDGET_OrbitSelector_TYP = widgets.Dropdown( options=['LLA', 'VEL', 'PTG'], description='Variable')
	WIDGET_OrbitSelector_TYP.description = 'TYP'
	WIDGET_OrbitSelector_TYP.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_TYP,)
	global WIDGET_OrbitSelector_PerYYY
	WIDGET_OrbitSelector_PerYYY = widgets.Dropdown( options=['Per120', 'Per150'], description='Variable')
	WIDGET_OrbitSelector_PerYYY.description = 'PerYYY'
	WIDGET_OrbitSelector_PerYYY.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_PerYYY,)
	global WIDGET_OrbitSelector_LatZZ
	WIDGET_OrbitSelector_LatZZ = widgets.Dropdown( options=['Lat00', 'Lat40', 'Lat80'],  description='Variable')
	WIDGET_OrbitSelector_LatZZ.description = 'LatZZ'
	WIDGET_OrbitSelector_LatZZ.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_LatZZ,)
	global WIDGET_OrbitSelector_SRXXHZ
	WIDGET_OrbitSelector_SRXXHZ = widgets.Dropdown( options=['Srt16Hz', 'Srt01Hz'],  description='Variable')
	WIDGET_OrbitSelector_SRXXHZ.description = 'SRXXHZ'
	WIDGET_OrbitSelector_SRXXHZ.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_SRXXHZ,)
	global WIDGET_OrbitSelector_SC
	WIDGET_OrbitSelector_SC = widgets.Dropdown( options=['Msc', 'Ssc'],  description='Variable')
	WIDGET_OrbitSelector_SC.description = 'SC'
	WIDGET_OrbitSelector_SC.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_SC,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	OrbitSelector_Btn = widgets.Button (
		description='OrbitSelector',
		tooltip="Constructs and returns an orbit full-path filename from the orbit properties.\nThe filename includes all parameters required to select the appropriate orbit.\nAll filenames  have the same length and same number of parameters. \nIn case OrbitFilename and EvtXY are empty then an empty string is returned.\nFILE FORMAT: DAED_ORB_EVTXY_TYP_PERYYY_LATZZ_SRTQQHz_XSC.csv\n  Parameter OrbitFilename:\n    If it is not empty then the rest arguments are ignored. \n    If it contains slashes then is is assumed it is a full path name and it is returned as it is.\n    If it does not contain slashes then the orbits path is added.\n    \n  Parameter EvtXY values:\n    EVTXS    X Event, Single Orbit\n    EVTXA    X Event, All Orbit\n    EVT1Y    1st Event: St Patrick’s day event [17 Mar 2015 – 20 Mar 2015]\n    EVT2Y    2nd Event ...  ...\n \n  Parameter TYP values:\n    LLA    Time,Latitude Longitude Altitude \n    VEL    Time,VmagVxVyVz\n    PTG    Time, X_GSE, Y_GSE, Z_GSE, RamX_GSE, RamY_GSE, RamZ_GSE\n  Parameter PerYYY values:\n    PER120, PER150    Perigee Altitude at 120km or 150km\n  Parameter LatZZ values:\n    LAT00, LAT40, LAT80    Perigee Latitude at 0°, 40° or 80°\n \n  Parameter SRXXHZ values:\n    SRT16Hz, SRT01Hz    Sampling rate 16Hz or 1HZ\n \n  Parameter SC values:\n    MSC    Mother Spacecraft\n    SSC    Sub-Spacecraft\n",
	)
	OrbitSelector_Btn.layout.min_width = '200px'
	OrbitSelector_Btn.style.button_color = 'YellowGreen'
	TopLevel_Panel.children += (OrbitSelector_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_OrbitSelector_OrbitFilename = widgets.Label(value='  --> OrbitFilename  ')
	WIDGET_OrbitSelector_OrbitFilename.layout.border = '1px dashed green'
	WIDGET_OrbitSelector_OrbitFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_OrbitSelector_OrbitFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_OrbitSelector_OrbitFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'Interpolator'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	global WIDGET_Interpolator_model
	WIDGET_Interpolator_model = widgets.Text(value="TIEGCM")
	WIDGET_Interpolator_model.description = 'model'
	WIDGET_Interpolator_model.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Interpolator_model,)
	global WIDGET_Interpolator_model_data_file
	WIDGET_Interpolator_model_data_file = widgets.Text(value="tiegcm_s_24900.nc")
	WIDGET_Interpolator_model_data_file.description = 'model_data_file'
	WIDGET_Interpolator_model_data_file.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Interpolator_model_data_file,)
	WIDGET_Interpolator_orbit_file = widgets.Label(value='  OrbitSelector.OrbitFilename --> orbit_file  ')
	WIDGET_Interpolator_orbit_file.layout.border = '1px dashed blue'
	WIDGET_Interpolator_orbit_file.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_Interpolator_orbit_file,)
	global WIDGET_Interpolator_save
	WIDGET_Interpolator_save = widgets.Checkbox( value=True, description='Save')
	WIDGET_Interpolator_save.description = 'save'
	WIDGET_Interpolator_save.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Interpolator_save,)
	global WIDGET_Interpolator_VAR
	WIDGET_Interpolator_VAR = widgets.Text(value="O2")
	WIDGET_Interpolator_VAR.description = 'VAR'
	WIDGET_Interpolator_VAR.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Interpolator_VAR,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	Interpolator_Btn = widgets.Button (
		description='Interpolator',
		tooltip="model-->string:: name of model eg TIEGCM\n model_data_file--> string:: model data files stored on DaedalusNAS\n orbit_file-->string :: orbit filename in Time-Lat-Lon-Alt format stored on DaedalusNAS\n save--> Logical:: if true saves interpolated values to directory\n VAR--> string:: variable to inteprolate, must be  one of the variables included in the model data\nOutputs:: Plots+ 1 csv file stored on DaedalusNAS in ModelOutputs/Interpolator",
	)
	Interpolator_Btn.layout.min_width = '200px'
	Interpolator_Btn.style.button_color = 'gold'
	TopLevel_Panel.children += (Interpolator_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_Interpolator_InterpolatorResultFilename = widgets.Label(value='  --> InterpolatorResultFilename  ')
	WIDGET_Interpolator_InterpolatorResultFilename.layout.border = '1px dashed green'
	WIDGET_Interpolator_InterpolatorResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_Interpolator_InterpolatorResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_Interpolator_InterpolatorResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'CalcDerivedValues'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_CalcDerivedValues_InputFilename = widgets.Label(value='  SGV_E.ResultFilename --> InputFilename  ')
	WIDGET_CalcDerivedValues_InputFilename.layout.border = '1px dashed blue'
	WIDGET_CalcDerivedValues_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_CalcDerivedValues_InputFilename,)
	global WIDGET_CalcDerivedValues_InputFileDescription
	WIDGET_CalcDerivedValues_InputFileDescription = widgets.Text(value="ModelData")
	WIDGET_CalcDerivedValues_InputFileDescription.description = 'InputFileDescription'
	WIDGET_CalcDerivedValues_InputFileDescription.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_CalcDerivedValues_InputFileDescription,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	CalcDerivedValues_Btn = widgets.Button (
		description='CalcDerivedValues',
		tooltip="",
	)
	CalcDerivedValues_Btn.layout.min_width = '200px'
	CalcDerivedValues_Btn.style.button_color = 'blue'
	TopLevel_Panel.children += (CalcDerivedValues_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_CalcDerivedValues_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_CalcDerivedValues_ResultFilename.layout.border = '1px dashed green'
	WIDGET_CalcDerivedValues_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_CalcDerivedValues_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_CalcDerivedValues_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'SGV_vi'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_SGV_vi_InputFilename = widgets.Label(value='  Interpolator.InterpolatorResultFilename --> InputFilename  ')
	WIDGET_SGV_vi_InputFilename.layout.border = '1px dashed blue'
	WIDGET_SGV_vi_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_SGV_vi_InputFilename,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	SGV_vi_Btn = widgets.Button (
		description='SGV_vi',
		tooltip="",
	)
	SGV_vi_Btn.layout.min_width = '200px'
	SGV_vi_Btn.style.button_color = 'orange'
	TopLevel_Panel.children += (SGV_vi_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_SGV_vi_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_SGV_vi_ResultFilename.layout.border = '1px dashed green'
	WIDGET_SGV_vi_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_SGV_vi_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_SGV_vi_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'SGV_Ti'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_SGV_Ti_InputFilename = widgets.Label(value='  Interpolator.InterpolatorResultFilename --> InputFilename  ')
	WIDGET_SGV_Ti_InputFilename.layout.border = '1px dashed blue'
	WIDGET_SGV_Ti_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_SGV_Ti_InputFilename,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	SGV_Ti_Btn = widgets.Button (
		description='SGV_Ti',
		tooltip="",
	)
	SGV_Ti_Btn.layout.min_width = '200px'
	SGV_Ti_Btn.style.button_color = 'orange'
	TopLevel_Panel.children += (SGV_Ti_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_SGV_Ti_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_SGV_Ti_ResultFilename.layout.border = '1px dashed green'
	WIDGET_SGV_Ti_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_SGV_Ti_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_SGV_Ti_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'SGV_Te'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_SGV_Te_InputFilename = widgets.Label(value='  Interpolator.InterpolatorResultFilename --> InputFilename  ')
	WIDGET_SGV_Te_InputFilename.layout.border = '1px dashed blue'
	WIDGET_SGV_Te_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_SGV_Te_InputFilename,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	SGV_Te_Btn = widgets.Button (
		description='SGV_Te',
		tooltip="",
	)
	SGV_Te_Btn.layout.min_width = '200px'
	SGV_Te_Btn.style.button_color = 'orange'
	TopLevel_Panel.children += (SGV_Te_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_SGV_Te_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_SGV_Te_ResultFilename.layout.border = '1px dashed green'
	WIDGET_SGV_Te_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_SGV_Te_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_SGV_Te_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'SGV_Ni'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_SGV_Ni_InputFilename = widgets.Label(value='  Interpolator.InterpolatorResultFilename --> InputFilename  ')
	WIDGET_SGV_Ni_InputFilename.layout.border = '1px dashed blue'
	WIDGET_SGV_Ni_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_SGV_Ni_InputFilename,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	SGV_Ni_Btn = widgets.Button (
		description='SGV_Ni',
		tooltip="",
	)
	SGV_Ni_Btn.layout.min_width = '200px'
	SGV_Ni_Btn.style.button_color = 'orange'
	TopLevel_Panel.children += (SGV_Ni_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_SGV_Ni_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_SGV_Ni_ResultFilename.layout.border = '1px dashed green'
	WIDGET_SGV_Ni_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_SGV_Ni_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_SGV_Ni_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'SGV_nix'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_SGV_nix_InputFilename = widgets.Label(value='  Interpolator.InterpolatorResultFilename --> InputFilename  ')
	WIDGET_SGV_nix_InputFilename.layout.border = '1px dashed blue'
	WIDGET_SGV_nix_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_SGV_nix_InputFilename,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	SGV_nix_Btn = widgets.Button (
		description='SGV_nix',
		tooltip="",
	)
	SGV_nix_Btn.layout.min_width = '200px'
	SGV_nix_Btn.style.button_color = 'orange'
	TopLevel_Panel.children += (SGV_nix_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_SGV_nix_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_SGV_nix_ResultFilename.layout.border = '1px dashed green'
	WIDGET_SGV_nix_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_SGV_nix_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_SGV_nix_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'SGV_Ne'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_SGV_Ne_InputFilename = widgets.Label(value='  Interpolator.InterpolatorResultFilename --> InputFilename  ')
	WIDGET_SGV_Ne_InputFilename.layout.border = '1px dashed blue'
	WIDGET_SGV_Ne_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_SGV_Ne_InputFilename,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	SGV_Ne_Btn = widgets.Button (
		description='SGV_Ne',
		tooltip="",
	)
	SGV_Ne_Btn.layout.min_width = '200px'
	SGV_Ne_Btn.style.button_color = 'orange'
	TopLevel_Panel.children += (SGV_Ne_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_SGV_Ne_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_SGV_Ne_ResultFilename.layout.border = '1px dashed green'
	WIDGET_SGV_Ne_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_SGV_Ne_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_SGV_Ne_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'SGV_TEC'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_SGV_TEC_InputFilename = widgets.Label(value='  Interpolator.InterpolatorResultFilename --> InputFilename  ')
	WIDGET_SGV_TEC_InputFilename.layout.border = '1px dashed blue'
	WIDGET_SGV_TEC_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_SGV_TEC_InputFilename,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	SGV_TEC_Btn = widgets.Button (
		description='SGV_TEC',
		tooltip="",
	)
	SGV_TEC_Btn.layout.min_width = '200px'
	SGV_TEC_Btn.style.button_color = 'orange'
	TopLevel_Panel.children += (SGV_TEC_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_SGV_TEC_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_SGV_TEC_ResultFilename.layout.border = '1px dashed green'
	WIDGET_SGV_TEC_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_SGV_TEC_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_SGV_TEC_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'SGV_un'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_SGV_un_InputFilename = widgets.Label(value='  Interpolator.InterpolatorResultFilename --> InputFilename  ')
	WIDGET_SGV_un_InputFilename.layout.border = '1px dashed blue'
	WIDGET_SGV_un_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_SGV_un_InputFilename,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	SGV_un_Btn = widgets.Button (
		description='SGV_un',
		tooltip="",
	)
	SGV_un_Btn.layout.min_width = '200px'
	SGV_un_Btn.style.button_color = 'orange'
	TopLevel_Panel.children += (SGV_un_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_SGV_un_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_SGV_un_ResultFilename.layout.border = '1px dashed green'
	WIDGET_SGV_un_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_SGV_un_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_SGV_un_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'SGV_Tn'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_SGV_Tn_InputFilename = widgets.Label(value='  Interpolator.InterpolatorResultFilename --> InputFilename  ')
	WIDGET_SGV_Tn_InputFilename.layout.border = '1px dashed blue'
	WIDGET_SGV_Tn_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_SGV_Tn_InputFilename,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	SGV_Tn_Btn = widgets.Button (
		description='SGV_Tn',
		tooltip="",
	)
	SGV_Tn_Btn.layout.min_width = '200px'
	SGV_Tn_Btn.style.button_color = 'orange'
	TopLevel_Panel.children += (SGV_Tn_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_SGV_Tn_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_SGV_Tn_ResultFilename.layout.border = '1px dashed green'
	WIDGET_SGV_Tn_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_SGV_Tn_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_SGV_Tn_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'SGV_Nn'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_SGV_Nn_InputFilename = widgets.Label(value='  Interpolator.InterpolatorResultFilename --> InputFilename  ')
	WIDGET_SGV_Nn_InputFilename.layout.border = '1px dashed blue'
	WIDGET_SGV_Nn_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_SGV_Nn_InputFilename,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	SGV_Nn_Btn = widgets.Button (
		description='SGV_Nn',
		tooltip="",
	)
	SGV_Nn_Btn.layout.min_width = '200px'
	SGV_Nn_Btn.style.button_color = 'orange'
	TopLevel_Panel.children += (SGV_Nn_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_SGV_Nn_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_SGV_Nn_ResultFilename.layout.border = '1px dashed green'
	WIDGET_SGV_Nn_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_SGV_Nn_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_SGV_Nn_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'SGV_nnx'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_SGV_nnx_InputFilename = widgets.Label(value='  Interpolator.InterpolatorResultFilename --> InputFilename  ')
	WIDGET_SGV_nnx_InputFilename.layout.border = '1px dashed blue'
	WIDGET_SGV_nnx_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_SGV_nnx_InputFilename,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	SGV_nnx_Btn = widgets.Button (
		description='SGV_nnx',
		tooltip="",
	)
	SGV_nnx_Btn.layout.min_width = '200px'
	SGV_nnx_Btn.style.button_color = 'orange'
	TopLevel_Panel.children += (SGV_nnx_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_SGV_nnx_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_SGV_nnx_ResultFilename.layout.border = '1px dashed green'
	WIDGET_SGV_nnx_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_SGV_nnx_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_SGV_nnx_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'SGV_JEPP'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_SGV_JEPP_InputFilename = widgets.Label(value='  Interpolator.InterpolatorResultFilename --> InputFilename  ')
	WIDGET_SGV_JEPP_InputFilename.layout.border = '1px dashed blue'
	WIDGET_SGV_JEPP_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_SGV_JEPP_InputFilename,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	SGV_JEPP_Btn = widgets.Button (
		description='SGV_JEPP',
		tooltip="",
	)
	SGV_JEPP_Btn.layout.min_width = '200px'
	SGV_JEPP_Btn.style.button_color = 'orange'
	TopLevel_Panel.children += (SGV_JEPP_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_SGV_JEPP_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_SGV_JEPP_ResultFilename.layout.border = '1px dashed green'
	WIDGET_SGV_JEPP_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_SGV_JEPP_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_SGV_JEPP_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'SGV_B'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_SGV_B_InputFilename = widgets.Label(value='  Interpolator.InterpolatorResultFilename --> InputFilename  ')
	WIDGET_SGV_B_InputFilename.layout.border = '1px dashed blue'
	WIDGET_SGV_B_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_SGV_B_InputFilename,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	SGV_B_Btn = widgets.Button (
		description='SGV_B',
		tooltip="",
	)
	SGV_B_Btn.layout.min_width = '200px'
	SGV_B_Btn.style.button_color = 'orange'
	TopLevel_Panel.children += (SGV_B_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_SGV_B_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_SGV_B_ResultFilename.layout.border = '1px dashed green'
	WIDGET_SGV_B_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_SGV_B_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_SGV_B_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'SGV_E'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_SGV_E_InputFilename = widgets.Label(value='  Interpolator.InterpolatorResultFilename --> InputFilename  ')
	WIDGET_SGV_E_InputFilename.layout.border = '1px dashed blue'
	WIDGET_SGV_E_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_SGV_E_InputFilename,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	SGV_E_Btn = widgets.Button (
		description='SGV_E',
		tooltip="",
	)
	SGV_E_Btn.layout.min_width = '200px'
	SGV_E_Btn.style.button_color = 'orange'
	TopLevel_Panel.children += (SGV_E_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_SGV_E_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_SGV_E_ResultFilename.layout.border = '1px dashed green'
	WIDGET_SGV_E_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_SGV_E_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_SGV_E_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'CalcDerivedValues'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_CalcDerivedValues_InputFilename = widgets.Label(value='  SGV_E.ResultFilename --> InputFilename  ')
	WIDGET_CalcDerivedValues_InputFilename.layout.border = '1px dashed blue'
	WIDGET_CalcDerivedValues_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_CalcDerivedValues_InputFilename,)
	global WIDGET_CalcDerivedValues_InputFileDescription
	WIDGET_CalcDerivedValues_InputFileDescription = widgets.Text(value="SyntheticTruth")
	WIDGET_CalcDerivedValues_InputFileDescription.description = 'InputFileDescription'
	WIDGET_CalcDerivedValues_InputFileDescription.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_CalcDerivedValues_InputFileDescription,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	CalcDerivedValues_Btn = widgets.Button (
		description='CalcDerivedValues',
		tooltip="",
	)
	CalcDerivedValues_Btn.layout.min_width = '200px'
	CalcDerivedValues_Btn.style.button_color = 'blue'
	TopLevel_Panel.children += (CalcDerivedValues_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_CalcDerivedValues_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_CalcDerivedValues_ResultFilename.layout.border = '1px dashed green'
	WIDGET_CalcDerivedValues_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_CalcDerivedValues_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_CalcDerivedValues_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'EnvToInsTrasnfer'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_EnvToInsTrasnfer_OritFilename = widgets.Label(value='  OrbitSelector.OrbitFilename --> OritFilename  ')
	WIDGET_EnvToInsTrasnfer_OritFilename.layout.border = '1px dashed blue'
	WIDGET_EnvToInsTrasnfer_OritFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_EnvToInsTrasnfer_OritFilename,)
	WIDGET_EnvToInsTrasnfer_InputFilename = widgets.Label(value='  SGV_E.SGV_E_ResultFilename --> InputFilename  ')
	WIDGET_EnvToInsTrasnfer_InputFilename.layout.border = '1px dashed blue'
	WIDGET_EnvToInsTrasnfer_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_EnvToInsTrasnfer_InputFilename,)
	global WIDGET_EnvToInsTrasnfer_PICfilename
	WIDGET_EnvToInsTrasnfer_PICfilename = widgets.Text(value="")
	WIDGET_EnvToInsTrasnfer_PICfilename.description = 'PICfilename'
	WIDGET_EnvToInsTrasnfer_PICfilename.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_EnvToInsTrasnfer_PICfilename,)
	global WIDGET_EnvToInsTrasnfer_PointingKnowledge
	WIDGET_EnvToInsTrasnfer_PointingKnowledge = widgets.Text(value="")
	WIDGET_EnvToInsTrasnfer_PointingKnowledge.description = 'PointingKnowledge'
	WIDGET_EnvToInsTrasnfer_PointingKnowledge.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_EnvToInsTrasnfer_PointingKnowledge,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	EnvToInsTrasnfer_Btn = widgets.Button (
		description='EnvToInsTrasnfer',
		tooltip="",
	)
	EnvToInsTrasnfer_Btn.layout.min_width = '200px'
	EnvToInsTrasnfer_Btn.style.button_color = 'DeepSkyBlue'
	TopLevel_Panel.children += (EnvToInsTrasnfer_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_EnvToInsTrasnfer_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_EnvToInsTrasnfer_ResultFilename.layout.border = '1px dashed green'
	WIDGET_EnvToInsTrasnfer_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_EnvToInsTrasnfer_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_EnvToInsTrasnfer_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'InstrumentIDMRPA'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_InstrumentIDMRPA_InputFilename = widgets.Label(value='  EnvToInsTrasnfer.ResultFilename --> InputFilename  ')
	WIDGET_InstrumentIDMRPA_InputFilename.layout.border = '1px dashed blue'
	WIDGET_InstrumentIDMRPA_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_InstrumentIDMRPA_InputFilename,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	InstrumentIDMRPA_Btn = widgets.Button (
		description='InstrumentIDMRPA',
		tooltip="",
	)
	InstrumentIDMRPA_Btn.layout.min_width = '200px'
	InstrumentIDMRPA_Btn.style.button_color = 'Moccasin'
	TopLevel_Panel.children += (InstrumentIDMRPA_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_InstrumentIDMRPA_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_InstrumentIDMRPA_ResultFilename.layout.border = '1px dashed green'
	WIDGET_InstrumentIDMRPA_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_InstrumentIDMRPA_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_InstrumentIDMRPA_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'InstrumentTII'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_InstrumentTII_InputFilename = widgets.Label(value='  EnvToInsTrasnfer.ResultFilename --> InputFilename  ')
	WIDGET_InstrumentTII_InputFilename.layout.border = '1px dashed blue'
	WIDGET_InstrumentTII_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_InstrumentTII_InputFilename,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	InstrumentTII_Btn = widgets.Button (
		description='InstrumentTII',
		tooltip="",
	)
	InstrumentTII_Btn.layout.min_width = '200px'
	InstrumentTII_Btn.style.button_color = 'Moccasin'
	TopLevel_Panel.children += (InstrumentTII_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_InstrumentTII_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_InstrumentTII_ResultFilename.layout.border = '1px dashed green'
	WIDGET_InstrumentTII_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_InstrumentTII_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_InstrumentTII_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'InstrumentRWSCWS'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_InstrumentRWSCWS_InputFilename = widgets.Label(value='  EnvToInsTrasnfer.ResultFilename --> InputFilename  ')
	WIDGET_InstrumentRWSCWS_InputFilename.layout.border = '1px dashed blue'
	WIDGET_InstrumentRWSCWS_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_InstrumentRWSCWS_InputFilename,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	InstrumentRWSCWS_Btn = widgets.Button (
		description='InstrumentRWSCWS',
		tooltip="",
	)
	InstrumentRWSCWS_Btn.layout.min_width = '200px'
	InstrumentRWSCWS_Btn.style.button_color = 'Moccasin'
	TopLevel_Panel.children += (InstrumentRWSCWS_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_InstrumentRWSCWS_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_InstrumentRWSCWS_ResultFilename.layout.border = '1px dashed green'
	WIDGET_InstrumentRWSCWS_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_InstrumentRWSCWS_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_InstrumentRWSCWS_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'InstrumentIMS'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_InstrumentIMS_InputFilename = widgets.Label(value='  EnvToInsTrasnfer.ResultFilename --> InputFilename  ')
	WIDGET_InstrumentIMS_InputFilename.layout.border = '1px dashed blue'
	WIDGET_InstrumentIMS_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_InstrumentIMS_InputFilename,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	InstrumentIMS_Btn = widgets.Button (
		description='InstrumentIMS',
		tooltip="",
	)
	InstrumentIMS_Btn.layout.min_width = '200px'
	InstrumentIMS_Btn.style.button_color = 'Moccasin'
	TopLevel_Panel.children += (InstrumentIMS_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_InstrumentIMS_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_InstrumentIMS_ResultFilename.layout.border = '1px dashed green'
	WIDGET_InstrumentIMS_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_InstrumentIMS_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_InstrumentIMS_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'InstrumentNMS'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_InstrumentNMS_InputFilename = widgets.Label(value='  EnvToInsTrasnfer.ResultFilename --> InputFilename  ')
	WIDGET_InstrumentNMS_InputFilename.layout.border = '1px dashed blue'
	WIDGET_InstrumentNMS_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_InstrumentNMS_InputFilename,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	InstrumentNMS_Btn = widgets.Button (
		description='InstrumentNMS',
		tooltip="",
	)
	InstrumentNMS_Btn.layout.min_width = '200px'
	InstrumentNMS_Btn.style.button_color = 'Moccasin'
	TopLevel_Panel.children += (InstrumentNMS_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_InstrumentNMS_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_InstrumentNMS_ResultFilename.layout.border = '1px dashed green'
	WIDGET_InstrumentNMS_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_InstrumentNMS_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_InstrumentNMS_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'InstrumentACC'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_InstrumentACC_InputFilename = widgets.Label(value='  EnvToInsTrasnfer.ResultFilename --> InputFilename  ')
	WIDGET_InstrumentACC_InputFilename.layout.border = '1px dashed blue'
	WIDGET_InstrumentACC_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_InstrumentACC_InputFilename,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	InstrumentACC_Btn = widgets.Button (
		description='InstrumentACC',
		tooltip="",
	)
	InstrumentACC_Btn.layout.min_width = '200px'
	InstrumentACC_Btn.style.button_color = 'Moccasin'
	TopLevel_Panel.children += (InstrumentACC_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_InstrumentACC_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_InstrumentACC_ResultFilename.layout.border = '1px dashed green'
	WIDGET_InstrumentACC_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_InstrumentACC_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_InstrumentACC_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'InstrumentEPDS3'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_InstrumentEPDS3_InputFilename = widgets.Label(value='  EnvToInsTrasnfer.ResultFilename --> InputFilename  ')
	WIDGET_InstrumentEPDS3_InputFilename.layout.border = '1px dashed blue'
	WIDGET_InstrumentEPDS3_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_InstrumentEPDS3_InputFilename,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	InstrumentEPDS3_Btn = widgets.Button (
		description='InstrumentEPDS3',
		tooltip="",
	)
	InstrumentEPDS3_Btn.layout.min_width = '200px'
	InstrumentEPDS3_Btn.style.button_color = 'Moccasin'
	TopLevel_Panel.children += (InstrumentEPDS3_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_InstrumentEPDS3_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_InstrumentEPDS3_ResultFilename.layout.border = '1px dashed green'
	WIDGET_InstrumentEPDS3_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_InstrumentEPDS3_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_InstrumentEPDS3_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'InstrumentEFI'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_InstrumentEFI_InputFilename = widgets.Label(value='  EnvToInsTrasnfer.ResultFilename --> InputFilename  ')
	WIDGET_InstrumentEFI_InputFilename.layout.border = '1px dashed blue'
	WIDGET_InstrumentEFI_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_InstrumentEFI_InputFilename,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	InstrumentEFI_Btn = widgets.Button (
		description='InstrumentEFI',
		tooltip="",
	)
	InstrumentEFI_Btn.layout.min_width = '200px'
	InstrumentEFI_Btn.style.button_color = 'Moccasin'
	TopLevel_Panel.children += (InstrumentEFI_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_InstrumentEFI_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_InstrumentEFI_ResultFilename.layout.border = '1px dashed green'
	WIDGET_InstrumentEFI_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_InstrumentEFI_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_InstrumentEFI_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'InstrumentMIP'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_InstrumentMIP_InputFilename = widgets.Label(value='  EnvToInsTrasnfer.ResultFilename --> InputFilename  ')
	WIDGET_InstrumentMIP_InputFilename.layout.border = '1px dashed blue'
	WIDGET_InstrumentMIP_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_InstrumentMIP_InputFilename,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	InstrumentMIP_Btn = widgets.Button (
		description='InstrumentMIP',
		tooltip="",
	)
	InstrumentMIP_Btn.layout.min_width = '200px'
	InstrumentMIP_Btn.style.button_color = 'Moccasin'
	TopLevel_Panel.children += (InstrumentMIP_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_InstrumentMIP_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_InstrumentMIP_ResultFilename.layout.border = '1px dashed green'
	WIDGET_InstrumentMIP_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_InstrumentMIP_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_InstrumentMIP_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'InstrumentMAG'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_InstrumentMAG_InputFilename = widgets.Label(value='  EnvToInsTrasnfer.ResultFilename --> InputFilename  ')
	WIDGET_InstrumentMAG_InputFilename.layout.border = '1px dashed blue'
	WIDGET_InstrumentMAG_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_InstrumentMAG_InputFilename,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	InstrumentMAG_Btn = widgets.Button (
		description='InstrumentMAG',
		tooltip="",
	)
	InstrumentMAG_Btn.layout.min_width = '200px'
	InstrumentMAG_Btn.style.button_color = 'Moccasin'
	TopLevel_Panel.children += (InstrumentMAG_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_InstrumentMAG_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_InstrumentMAG_ResultFilename.layout.border = '1px dashed green'
	WIDGET_InstrumentMAG_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_InstrumentMAG_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_InstrumentMAG_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'InstrumentGNSS'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_InstrumentGNSS_InputFilename = widgets.Label(value='  EnvToInsTrasnfer.ResultFilename --> InputFilename  ')
	WIDGET_InstrumentGNSS_InputFilename.layout.border = '1px dashed blue'
	WIDGET_InstrumentGNSS_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_InstrumentGNSS_InputFilename,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	InstrumentGNSS_Btn = widgets.Button (
		description='InstrumentGNSS',
		tooltip="",
	)
	InstrumentGNSS_Btn.layout.min_width = '200px'
	InstrumentGNSS_Btn.style.button_color = 'Moccasin'
	TopLevel_Panel.children += (InstrumentGNSS_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_InstrumentGNSS_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_InstrumentGNSS_ResultFilename.layout.border = '1px dashed green'
	WIDGET_InstrumentGNSS_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_InstrumentGNSS_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_InstrumentGNSS_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'CalcDerivedValues'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_CalcDerivedValues_InputFilename = widgets.Label(value='  SGV_E.ResultFilename --> InputFilename  ')
	WIDGET_CalcDerivedValues_InputFilename.layout.border = '1px dashed blue'
	WIDGET_CalcDerivedValues_InputFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_CalcDerivedValues_InputFilename,)
	global WIDGET_CalcDerivedValues_InputFileDescription
	WIDGET_CalcDerivedValues_InputFileDescription = widgets.Text(value="SyntheticScienceProducts")
	WIDGET_CalcDerivedValues_InputFileDescription.description = 'InputFileDescription'
	WIDGET_CalcDerivedValues_InputFileDescription.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_CalcDerivedValues_InputFileDescription,)
	TopLevel_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	CalcDerivedValues_Btn = widgets.Button (
		description='CalcDerivedValues',
		tooltip="",
	)
	CalcDerivedValues_Btn.layout.min_width = '200px'
	CalcDerivedValues_Btn.style.button_color = 'blue'
	TopLevel_Panel.children += (CalcDerivedValues_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_CalcDerivedValues_ResultFilename = widgets.Label(value='  --> ResultFilename  ')
	WIDGET_CalcDerivedValues_ResultFilename.layout.border = '1px dashed green'
	WIDGET_CalcDerivedValues_ResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_CalcDerivedValues_ResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_CalcDerivedValues_ResultFilename,)
	TopLevel_Panel.children += (OutputsPanel,)
	return TopLevel_Panel


def Construct_Interpolator():
	#Create Containers
	Interpolator_Panel = widgets.Box()
	Interpolator_Panel.layout.overflow_x = 'scroll'
	Interpolator_Panel.layout.flex_flow = 'row'
	Interpolator_Panel.layout.display = 'flex'
	########
	## GUI code for module 'OrbitSelector'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	global WIDGET_OrbitSelector_Filename
	WIDGET_OrbitSelector_Filename = widgets.Text("DAED_ORB_Evt0_LLA_Per150_Lat80_Srt01Hz_Msc.csv")
	WIDGET_OrbitSelector_Filename.description = 'Filename'
	WIDGET_OrbitSelector_Filename.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_Filename,)
	global WIDGET_OrbitSelector_EvtXY
	WIDGET_OrbitSelector_EvtXY = widgets.Dropdown( options=['Evt0', 'Evt1', 'Evt2', 'Evt3', 'Evt4', 'Evt5', 'Evt6', 'Evt7', 'Evt8', 'Evt9'], description='Variable')
	WIDGET_OrbitSelector_EvtXY.description = 'EvtXY'
	WIDGET_OrbitSelector_EvtXY.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_EvtXY,)
	global WIDGET_OrbitSelector_TYP
	WIDGET_OrbitSelector_TYP = widgets.Dropdown( options=['LLA', 'VEL', 'PTG'], description='Variable')
	WIDGET_OrbitSelector_TYP.description = 'TYP'
	WIDGET_OrbitSelector_TYP.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_TYP,)
	global WIDGET_OrbitSelector_PerYYY
	WIDGET_OrbitSelector_PerYYY = widgets.Dropdown( options=['Per120', 'Per150'], description='Variable')
	WIDGET_OrbitSelector_PerYYY.description = 'PerYYY'
	WIDGET_OrbitSelector_PerYYY.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_PerYYY,)
	global WIDGET_OrbitSelector_LatZZ
	WIDGET_OrbitSelector_LatZZ = widgets.Dropdown( options=['Lat00', 'Lat40', 'Lat80'],  description='Variable')
	WIDGET_OrbitSelector_LatZZ.description = 'LatZZ'
	WIDGET_OrbitSelector_LatZZ.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_LatZZ,)
	global WIDGET_OrbitSelector_SRXXHZ
	WIDGET_OrbitSelector_SRXXHZ = widgets.Dropdown( options=['Srt16Hz', 'Srt01Hz'],  description='Variable')
	WIDGET_OrbitSelector_SRXXHZ.description = 'SRXXHZ'
	WIDGET_OrbitSelector_SRXXHZ.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_SRXXHZ,)
	global WIDGET_OrbitSelector_SC
	WIDGET_OrbitSelector_SC = widgets.Dropdown( options=['Msc', 'Ssc'],  description='Variable')
	WIDGET_OrbitSelector_SC.description = 'SC'
	WIDGET_OrbitSelector_SC.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_SC,)
	Interpolator_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	OrbitSelector_Btn = widgets.Button (
		description='OrbitSelector',
		tooltip="Constructs and returns an orbit full-path filename from the orbit properties.\nThe filename includes all parameters required to select the appropriate orbit.\nAll filenames  have the same length and same number of parameters. \nIn case OrbitFilename and EvtXY are empty then an empty string is returned.\nFILE FORMAT: DAED_ORB_EVTXY_TYP_PERYYY_LATZZ_SRTQQHz_XSC.csv\n  Parameter OrbitFilename:\n    If it is not empty then the rest arguments are ignored. \n    If it contains slashes then is is assumed it is a full path name and it is returned as it is.\n    If it does not contain slashes then the orbits path is added.\n    \n  Parameter EvtXY values:\n    EVTXS    X Event, Single Orbit\n    EVTXA    X Event, All Orbit\n    EVT1Y    1st Event: St Patrick’s day event [17 Mar 2015 – 20 Mar 2015]\n    EVT2Y    2nd Event ...  ...\n \n  Parameter TYP values:\n    LLA    Time,Latitude Longitude Altitude \n    VEL    Time,VmagVxVyVz\n    PTG    Time, X_GSE, Y_GSE, Z_GSE, RamX_GSE, RamY_GSE, RamZ_GSE\n  Parameter PerYYY values:\n    PER120, PER150    Perigee Altitude at 120km or 150km\n  Parameter LatZZ values:\n    LAT00, LAT40, LAT80    Perigee Latitude at 0°, 40° or 80°\n \n  Parameter SRXXHZ values:\n    SRT16Hz, SRT01Hz    Sampling rate 16Hz or 1HZ\n \n  Parameter SC values:\n    MSC    Mother Spacecraft\n    SSC    Sub-Spacecraft\n",
	)
	OrbitSelector_Btn.layout.min_width = '200px'
	OrbitSelector_Btn.style.button_color = 'YellowGreen'
	Interpolator_Panel.children += (OrbitSelector_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_OrbitSelector_OrbitFilename = widgets.Label(value='  --> OrbitFilename  ')
	WIDGET_OrbitSelector_OrbitFilename.layout.border = '1px dashed green'
	WIDGET_OrbitSelector_OrbitFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_OrbitSelector_OrbitFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_OrbitSelector_OrbitFilename,)
	Interpolator_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'Interpolator'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	global WIDGET_Interpolator_model
	WIDGET_Interpolator_model = widgets.Text(value="TIEGCM")
	WIDGET_Interpolator_model.description = 'model'
	WIDGET_Interpolator_model.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Interpolator_model,)
	global WIDGET_Interpolator_model_data_file
	WIDGET_Interpolator_model_data_file = widgets.Text(value="tiegcm_s_24900.nc")
	WIDGET_Interpolator_model_data_file.description = 'model_data_file'
	WIDGET_Interpolator_model_data_file.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Interpolator_model_data_file,)
	WIDGET_Interpolator_orbit_file = widgets.Label(value='  OrbitSelector.OrbitFilename --> orbit_file  ')
	WIDGET_Interpolator_orbit_file.layout.border = '1px dashed blue'
	WIDGET_Interpolator_orbit_file.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_Interpolator_orbit_file,)
	global WIDGET_Interpolator_save
	WIDGET_Interpolator_save = widgets.Checkbox( value=True, description='Save')
	WIDGET_Interpolator_save.description = 'save'
	WIDGET_Interpolator_save.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Interpolator_save,)
	global WIDGET_Interpolator_VAR
	WIDGET_Interpolator_VAR = widgets.Text(value="O2")
	WIDGET_Interpolator_VAR.description = 'VAR'
	WIDGET_Interpolator_VAR.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Interpolator_VAR,)
	Interpolator_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	Interpolator_Btn = widgets.Button (
		description='Interpolator',
		tooltip="model-->string:: name of model eg TIEGCM\n model_data_file--> string:: model data files stored on DaedalusNAS\n orbit_file-->string :: orbit filename in Time-Lat-Lon-Alt format stored on DaedalusNAS\n save--> Logical:: if true saves interpolated values to directory\n VAR--> string:: variable to inteprolate, must be  one of the variables included in the model data\nOutputs:: Plots+ 1 csv file stored on DaedalusNAS in ModelOutputs/Interpolator",
	)
	Interpolator_Btn.layout.min_width = '200px'
	Interpolator_Btn.style.button_color = 'gold'
	Interpolator_Panel.children += (Interpolator_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_Interpolator_InterpolatedOrbitCSV = widgets.Label(value='  --> InterpolatedOrbitCSV  ')
	WIDGET_Interpolator_InterpolatedOrbitCSV.layout.border = '1px dashed green'
	WIDGET_Interpolator_InterpolatedOrbitCSV.layout.margin ='0px 40px 0px 0px' 
	WIDGET_Interpolator_InterpolatedOrbitCSV.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_Interpolator_InterpolatedOrbitCSV,)
	Interpolator_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'PlotGlobe'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	global WIDGET_PlotGlobe_DataCSVfilename
	WIDGET_PlotGlobe_DataCSVfilename = widgets.Text()
	WIDGET_PlotGlobe_DataCSVfilename.description = 'DataCSVfilename'
	WIDGET_PlotGlobe_DataCSVfilename.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_PlotGlobe_DataCSVfilename,)
	WIDGET_PlotGlobe_OrbitDataCSVfilename = widgets.Label(value='  Interpolator.InterpolatedOrbitCSV --> OrbitDataCSVfilename  ')
	WIDGET_PlotGlobe_OrbitDataCSVfilename.layout.border = '1px dashed blue'
	WIDGET_PlotGlobe_OrbitDataCSVfilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_PlotGlobe_OrbitDataCSVfilename,)
	global WIDGET_PlotGlobe_GraphTitle
	WIDGET_PlotGlobe_GraphTitle = widgets.Text()
	WIDGET_PlotGlobe_GraphTitle.description = 'GraphTitle'
	WIDGET_PlotGlobe_GraphTitle.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_PlotGlobe_GraphTitle,)
	global WIDGET_PlotGlobe_ColorbarTitle
	WIDGET_PlotGlobe_ColorbarTitle = widgets.Text()
	WIDGET_PlotGlobe_ColorbarTitle.description = 'ColorbarTitle'
	WIDGET_PlotGlobe_ColorbarTitle.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_PlotGlobe_ColorbarTitle,)
	global WIDGET_PlotGlobe_ColorscaleName
	WIDGET_PlotGlobe_ColorscaleName = widgets.Text(value="Jet")
	WIDGET_PlotGlobe_ColorscaleName.description = 'ColorscaleName'
	WIDGET_PlotGlobe_ColorscaleName.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_PlotGlobe_ColorscaleName,)
	Interpolator_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	PlotGlobe_Btn = widgets.Button (
		description='PlotGlobe',
		tooltip="Creates a 3D plot of an earth globe, a sphere surface and a satellite orbit. The surface and the orbit are colored according to the data values in the CSV files.\n  DataCSVfilename: format: Time,Lat,Lon,Alt,value. Contains the data for the sphere surface. If empty then no surface will be plotted.\n  OrbitDataCSVfilename: format: Time,Lat,Lon,Alt,value. Contains the data for the orbit. If empty then no orbit will be plotted.\n  PlotTitle: the title of the plot. It will be displayed at the top of the globe.\n  ColorbarTitle: the title of the colorbar beside the globe. Usually contains measuremnt units\n  ColorscaleName: valid values are: ‘Blackbody’, ‘Bluered’, ‘Blues’, ‘Earth’, ‘Electric’, ‘Greens’, ‘Greys’, ‘Hot’, ‘Jet’, ‘Picnic’, ‘Portland’, ‘Rainbow’, ‘RdBu’, ‘Reds’, ‘Viridis’, ‘YlGnBu’, ‘YlOrRd’\n                  In case an empty string is passed then a default HeatMap colorscale will be applied.\n                  In case None is passed then all points will be black irrespective of value.\n  RETURNS: a string containing information about the Data",
	)
	PlotGlobe_Btn.layout.min_width = '200px'
	PlotGlobe_Btn.style.button_color = 'deeppink'
	Interpolator_Panel.children += (PlotGlobe_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	Interpolator_Panel.children += (OutputsPanel,)
	return Interpolator_Panel


def Construct_IGRF():
	#Create Containers
	IGRF_Panel = widgets.Box()
	IGRF_Panel.layout.overflow_x = 'scroll'
	IGRF_Panel.layout.flex_flow = 'row'
	IGRF_Panel.layout.display = 'flex'
	########
	## GUI code for module 'OrbitSelector'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	global WIDGET_OrbitSelector_Filename
	WIDGET_OrbitSelector_Filename = widgets.Text()
	WIDGET_OrbitSelector_Filename.description = 'Filename'
	WIDGET_OrbitSelector_Filename.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_Filename,)
	global WIDGET_OrbitSelector_EvtXY
	WIDGET_OrbitSelector_EvtXY = widgets.Dropdown( options=['', 'Evt0', 'Evt1', 'Evt2', 'Evt3', 'Evt4', 'Evt5', 'Evt6', 'Evt7', 'Evt8', 'Evt9'], description='Variable')
	WIDGET_OrbitSelector_EvtXY.description = 'EvtXY'
	WIDGET_OrbitSelector_EvtXY.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_EvtXY,)
	global WIDGET_OrbitSelector_TYP
	WIDGET_OrbitSelector_TYP = widgets.Dropdown( options=['LLA', 'VEL', 'PTG'], description='Variable')
	WIDGET_OrbitSelector_TYP.description = 'TYP'
	WIDGET_OrbitSelector_TYP.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_TYP,)
	global WIDGET_OrbitSelector_PerYYY
	WIDGET_OrbitSelector_PerYYY = widgets.Dropdown( options=['Per120', 'Per150'], description='Variable')
	WIDGET_OrbitSelector_PerYYY.description = 'PerYYY'
	WIDGET_OrbitSelector_PerYYY.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_PerYYY,)
	global WIDGET_OrbitSelector_LatZZ
	WIDGET_OrbitSelector_LatZZ = widgets.Dropdown( options=['Lat00', 'Lat40', 'Lat80'],  description='Variable')
	WIDGET_OrbitSelector_LatZZ.description = 'LatZZ'
	WIDGET_OrbitSelector_LatZZ.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_LatZZ,)
	global WIDGET_OrbitSelector_SRXXHZ
	WIDGET_OrbitSelector_SRXXHZ = widgets.Dropdown( options=['Srt16Hz', 'Srt01Hz'],  description='Variable')
	WIDGET_OrbitSelector_SRXXHZ.description = 'SRXXHZ'
	WIDGET_OrbitSelector_SRXXHZ.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_SRXXHZ,)
	global WIDGET_OrbitSelector_SC
	WIDGET_OrbitSelector_SC = widgets.Dropdown( options=['Msc', 'Ssc'],  description='Variable')
	WIDGET_OrbitSelector_SC.description = 'SC'
	WIDGET_OrbitSelector_SC.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_SC,)
	IGRF_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	OrbitSelector_Btn = widgets.Button (
		description='OrbitSelector',
		tooltip="Constructs and returns an orbit full-path filename from the orbit properties.\nThe filename includes all parameters required to select the appropriate orbit.\nAll filenames  have the same length and same number of parameters. \nIn case OrbitFilename and EvtXY are empty then an empty string is returned.\nFILE FORMAT: DAED_ORB_EVTXY_TYP_PERYYY_LATZZ_SRTQQHz_XSC.csv\n  Parameter OrbitFilename:\n    If it is not empty then the rest arguments are ignored. \n    If it contains slashes then is is assumed it is a full path name and it is returned as it is.\n    If it does not contain slashes then the orbits path is added.\n    \n  Parameter EvtXY values:\n    EVTXS    X Event, Single Orbit\n    EVTXA    X Event, All Orbit\n    EVT1Y    1st Event: St Patrick’s day event [17 Mar 2015 – 20 Mar 2015]\n    EVT2Y    2nd Event ...  ...\n \n  Parameter TYP values:\n    LLA    Time,Latitude Longitude Altitude \n    VEL    Time,VmagVxVyVz\n    PTG    Time, X_GSE, Y_GSE, Z_GSE, RamX_GSE, RamY_GSE, RamZ_GSE\n  Parameter PerYYY values:\n    PER120, PER150    Perigee Altitude at 120km or 150km\n  Parameter LatZZ values:\n    LAT00, LAT40, LAT80    Perigee Latitude at 0°, 40° or 80°\n \n  Parameter SRXXHZ values:\n    SRT16Hz, SRT01Hz    Sampling rate 16Hz or 1HZ\n \n  Parameter SC values:\n    MSC    Mother Spacecraft\n    SSC    Sub-Spacecraft\n",
	)
	OrbitSelector_Btn.layout.min_width = '200px'
	OrbitSelector_Btn.style.button_color = 'YellowGreen'
	IGRF_Panel.children += (OrbitSelector_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_OrbitSelector_OrbitFilename = widgets.Label(value='  --> OrbitFilename  ')
	WIDGET_OrbitSelector_OrbitFilename.layout.border = '1px dashed green'
	WIDGET_OrbitSelector_OrbitFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_OrbitSelector_OrbitFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_OrbitSelector_OrbitFilename,)
	IGRF_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'IGRF'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_IGRF_CSVfilename_forOrbit = widgets.Label(value='  OrbitSelector.OrbitFilename --> CSVfilename_forOrbit  ')
	WIDGET_IGRF_CSVfilename_forOrbit.layout.border = '1px dashed blue'
	WIDGET_IGRF_CSVfilename_forOrbit.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_IGRF_CSVfilename_forOrbit,)
	global WIDGET_IGRF_Variable_forOrbit
	WIDGET_IGRF_Variable_forOrbit = widgets.Dropdown( options=['', 'B', 'Bx', 'By', 'Bz'], value='', description='Variable')
	WIDGET_IGRF_Variable_forOrbit.description = 'Variable_forOrbit'
	WIDGET_IGRF_Variable_forOrbit.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_IGRF_Variable_forOrbit,)
	IGRF_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	IGRF_Btn = widgets.Button (
		description='IGRF',
		tooltip="International Geomagnetic Reference Field empirical model (IGRF)\nfilename: the CSV file to read. Format: Time,Alt,Lon,Lat. The file defines the coordinates for which the IGRF calculation will take place.\nParameter: selects which values to calculate. Possible values are:\n    ''   for all\n    'B'  for magnetic field\n    'Bx' for magnetic field component at x axis\n    'By' for magnetic field component at y axis\n    'Bz' for magnetic field component at z axis\nReturns: the name of the CSV file which contains the calculated values. Format: Time,Alt,Lon,Lat,B,Bx,By,Bz",
	)
	IGRF_Btn.layout.min_width = '200px'
	IGRF_Btn.style.button_color = 'gold'
	IGRF_Panel.children += (IGRF_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_IGRF_OrbitResultCSV = widgets.Label(value='  --> OrbitResultCSV  ')
	WIDGET_IGRF_OrbitResultCSV.layout.border = '1px dashed green'
	WIDGET_IGRF_OrbitResultCSV.layout.margin ='0px 40px 0px 0px' 
	WIDGET_IGRF_OrbitResultCSV.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_IGRF_OrbitResultCSV,)
	IGRF_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'CreateCSV_Sphere'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	global WIDGET_CreateCSV_Sphere_CSVfilename
	WIDGET_CreateCSV_Sphere_CSVfilename = widgets.Text(value="")
	WIDGET_CreateCSV_Sphere_CSVfilename.description = 'CSVfilename'
	WIDGET_CreateCSV_Sphere_CSVfilename.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_CreateCSV_Sphere_CSVfilename,)
	global WIDGET_CreateCSV_Sphere_fixedDatetimeString
	WIDGET_CreateCSV_Sphere_fixedDatetimeString = widgets.Text(value="Mar 17 2015 00:50:00.000000000")
	WIDGET_CreateCSV_Sphere_fixedDatetimeString.description = 'fixedDatetimeString'
	WIDGET_CreateCSV_Sphere_fixedDatetimeString.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_CreateCSV_Sphere_fixedDatetimeString,)
	global WIDGET_CreateCSV_Sphere_fixedAltitude
	WIDGET_CreateCSV_Sphere_fixedAltitude = widgets.FloatText(value=120)
	WIDGET_CreateCSV_Sphere_fixedAltitude.description = 'fixedAltitude'
	WIDGET_CreateCSV_Sphere_fixedAltitude.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_CreateCSV_Sphere_fixedAltitude,)
	global WIDGET_CreateCSV_Sphere_LatitudeStep
	WIDGET_CreateCSV_Sphere_LatitudeStep = widgets.FloatText(value=5)
	WIDGET_CreateCSV_Sphere_LatitudeStep.description = 'LatitudeStep'
	WIDGET_CreateCSV_Sphere_LatitudeStep.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_CreateCSV_Sphere_LatitudeStep,)
	global WIDGET_CreateCSV_Sphere_LongitudeStep
	WIDGET_CreateCSV_Sphere_LongitudeStep = widgets.FloatText(value=5)
	WIDGET_CreateCSV_Sphere_LongitudeStep.description = 'LongitudeStep'
	WIDGET_CreateCSV_Sphere_LongitudeStep.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_CreateCSV_Sphere_LongitudeStep,)
	IGRF_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	CreateCSV_Sphere_Btn = widgets.Button (
		description='CreateCSV_Sphere',
		tooltip="Creates a CSV file with the format [Time, Lat, Lon, Alt]\nTime and Alt are fixed values given as arguments and Lat and Lon are produced for the whole globe accodring to steps specified.\nCSVfilename: string, the csv filename to be written (overwrite mode)\nfixedDatetimeString: string, the date-time fixed text with format as example: Mar 17 2015 00:12:00.000. Fixed value for every csv entry.\nfixedAltitude: float positive, kilometers above earth. Fixed value for every csv entry.\nLatitudeStep: float positive, Latiude values range between 87.5 and -88.5. The step is how Lat should be incremented at each iteration.\nLongitudeStep: float positive, Longitude values range between -180 and 180.  The step is how Lon should be incremented at each iteration.\nRETURNS: the filename it has written (same as the argument)\n         the altitude (same as the argument)\n         the number of lines written",
	)
	CreateCSV_Sphere_Btn.layout.min_width = '200px'
	CreateCSV_Sphere_Btn.style.button_color = 'gold'
	IGRF_Panel.children += (CreateCSV_Sphere_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_CreateCSV_Sphere_theCSVfilename = widgets.Label(value='  --> theCSVfilename  ')
	WIDGET_CreateCSV_Sphere_theCSVfilename.layout.border = '1px dashed green'
	WIDGET_CreateCSV_Sphere_theCSVfilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_CreateCSV_Sphere_theCSVfilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_CreateCSV_Sphere_theCSVfilename,)
	WIDGET_CreateCSV_Sphere_theAltitude = widgets.Label(value='  --> theAltitude  ')
	WIDGET_CreateCSV_Sphere_theAltitude.layout.border = '1px dashed green'
	WIDGET_CreateCSV_Sphere_theAltitude.layout.margin ='0px 40px 0px 0px' 
	WIDGET_CreateCSV_Sphere_theAltitude.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_CreateCSV_Sphere_theAltitude,)
	WIDGET_CreateCSV_Sphere_NumberOfLinesWritten = widgets.Label(value='  --> NumberOfLinesWritten  ')
	WIDGET_CreateCSV_Sphere_NumberOfLinesWritten.layout.border = '1px dashed green'
	WIDGET_CreateCSV_Sphere_NumberOfLinesWritten.layout.margin ='0px 40px 0px 0px' 
	WIDGET_CreateCSV_Sphere_NumberOfLinesWritten.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_CreateCSV_Sphere_NumberOfLinesWritten,)
	IGRF_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'IGRF'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_IGRF_CSVfilename_forMeshgrid = widgets.Label(value='  CreateCSV_Sphere.theCSVfilename --> CSVfilename_forMeshgrid  ')
	WIDGET_IGRF_CSVfilename_forMeshgrid.layout.border = '1px dashed blue'
	WIDGET_IGRF_CSVfilename_forMeshgrid.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_IGRF_CSVfilename_forMeshgrid,)
	global WIDGET_IGRF_Variable_forMeshgrid
	WIDGET_IGRF_Variable_forMeshgrid = widgets.Dropdown( options=['', 'B', 'Bx', 'By', 'Bz'], value='', description='Variable')
	WIDGET_IGRF_Variable_forMeshgrid.description = 'Variable_forMeshgrid'
	WIDGET_IGRF_Variable_forMeshgrid.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_IGRF_Variable_forMeshgrid,)
	IGRF_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	IGRF_Btn = widgets.Button (
		description='IGRF',
		tooltip="International Geomagnetic Reference Field empirical model (IGRF)\nfilename: the CSV file to read. Format: Time,Alt,Lon,Lat. The file defines the coordinates for which the IGRF calculation will take place.\nParameter: selects which values to calculate. Possible values are:\n    ''   for all\n    'B'  for magnetic field\n    'Bx' for magnetic field component at x axis\n    'By' for magnetic field component at y axis\n    'Bz' for magnetic field component at z axis\nReturns: the name of the CSV file which contains the calculated values. Format: Time,Alt,Lon,Lat,B,Bx,By,Bz",
	)
	IGRF_Btn.layout.min_width = '200px'
	IGRF_Btn.style.button_color = 'gold'
	IGRF_Panel.children += (IGRF_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_IGRF_MeshgridResultCSV = widgets.Label(value='  --> MeshgridResultCSV  ')
	WIDGET_IGRF_MeshgridResultCSV.layout.border = '1px dashed green'
	WIDGET_IGRF_MeshgridResultCSV.layout.margin ='0px 40px 0px 0px' 
	WIDGET_IGRF_MeshgridResultCSV.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_IGRF_MeshgridResultCSV,)
	IGRF_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'PlotGlobe'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_PlotGlobe_CSVfilename_Meshgrid = widgets.Label(value='  IGRF.MeshgridResultCSV --> CSVfilename_Meshgrid  ')
	WIDGET_PlotGlobe_CSVfilename_Meshgrid.layout.border = '1px dashed blue'
	WIDGET_PlotGlobe_CSVfilename_Meshgrid.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_PlotGlobe_CSVfilename_Meshgrid,)
	WIDGET_PlotGlobe_CSVfilename_Orbit = widgets.Label(value='  IGRF.OrbitResultCSV --> CSVfilename_Orbit  ')
	WIDGET_PlotGlobe_CSVfilename_Orbit.layout.border = '1px dashed blue'
	WIDGET_PlotGlobe_CSVfilename_Orbit.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_PlotGlobe_CSVfilename_Orbit,)
	global WIDGET_PlotGlobe_PlotTitle
	WIDGET_PlotGlobe_PlotTitle = widgets.Text()
	WIDGET_PlotGlobe_PlotTitle.description = 'PlotTitle'
	WIDGET_PlotGlobe_PlotTitle.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_PlotGlobe_PlotTitle,)
	global WIDGET_PlotGlobe_ColorbarTitle
	WIDGET_PlotGlobe_ColorbarTitle = widgets.Text()
	WIDGET_PlotGlobe_ColorbarTitle.description = 'ColorbarTitle'
	WIDGET_PlotGlobe_ColorbarTitle.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_PlotGlobe_ColorbarTitle,)
	global WIDGET_PlotGlobe_ColorscaleName
	WIDGET_PlotGlobe_ColorscaleName = widgets.Text(value="Jet")
	WIDGET_PlotGlobe_ColorscaleName.description = 'ColorscaleName'
	WIDGET_PlotGlobe_ColorscaleName.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_PlotGlobe_ColorscaleName,)
	IGRF_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	PlotGlobe_Btn = widgets.Button (
		description='PlotGlobe',
		tooltip="Creates a 3D plot of an earth globe, a sphere surface and a satellite orbit. The surface and the orbit are colored according to the data values in the CSV files.\n  DataCSVfilename: format: Time,Lat,Lon,Alt,value. Contains the data for the sphere surface. If empty then no surface will be plotted.\n  OrbitDataCSVfilename: format: Time,Lat,Lon,Alt,value. Contains the data for the orbit. If empty then no orbit will be plotted.\n  PlotTitle: the title of the plot. It will be displayed at the top of the globe.\n  ColorbarTitle: the title of the colorbar beside the globe. Usually contains measuremnt units\n  ColorscaleName: valid values are: ‘Blackbody’, ‘Bluered’, ‘Blues’, ‘Earth’, ‘Electric’, ‘Greens’, ‘Greys’, ‘Hot’, ‘Jet’, ‘Picnic’, ‘Portland’, ‘Rainbow’, ‘RdBu’, ‘Reds’, ‘Viridis’, ‘YlGnBu’, ‘YlOrRd’\n                  In case an empty string is passed then a default HeatMap colorscale will be applied.\n                  In case None is passed then all points will be black irrespective of value.\n  RETURNS: a string containing information about the Data",
	)
	PlotGlobe_Btn.layout.min_width = '200px'
	PlotGlobe_Btn.style.button_color = 'deeppink'
	IGRF_Panel.children += (PlotGlobe_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	IGRF_Panel.children += (OutputsPanel,)
	return IGRF_Panel


def Construct_IRI16():
	#Create Containers
	IRI16_Panel = widgets.Box()
	IRI16_Panel.layout.overflow_x = 'scroll'
	IRI16_Panel.layout.flex_flow = 'row'
	IRI16_Panel.layout.display = 'flex'
	########
	## GUI code for module 'OrbitSelector'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	global WIDGET_OrbitSelector_Filename
	WIDGET_OrbitSelector_Filename = widgets.Text()
	WIDGET_OrbitSelector_Filename.description = 'Filename'
	WIDGET_OrbitSelector_Filename.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_Filename,)
	global WIDGET_OrbitSelector_EvtXY
	WIDGET_OrbitSelector_EvtXY = widgets.Dropdown( options=['', 'Evt0', 'Evt1', 'Evt2', 'Evt3', 'Evt4', 'Evt5', 'Evt6', 'Evt7', 'Evt8', 'Evt9'], description='Variable')
	WIDGET_OrbitSelector_EvtXY.description = 'EvtXY'
	WIDGET_OrbitSelector_EvtXY.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_EvtXY,)
	global WIDGET_OrbitSelector_TYP
	WIDGET_OrbitSelector_TYP = widgets.Dropdown( options=['LLA', 'VEL', 'PTG'], description='Variable')
	WIDGET_OrbitSelector_TYP.description = 'TYP'
	WIDGET_OrbitSelector_TYP.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_TYP,)
	global WIDGET_OrbitSelector_PerYYY
	WIDGET_OrbitSelector_PerYYY = widgets.Dropdown( options=['Per120', 'Per150'], description='Variable')
	WIDGET_OrbitSelector_PerYYY.description = 'PerYYY'
	WIDGET_OrbitSelector_PerYYY.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_PerYYY,)
	global WIDGET_OrbitSelector_LatZZ
	WIDGET_OrbitSelector_LatZZ = widgets.Dropdown( options=['Lat00', 'Lat40', 'Lat80'],  description='Variable')
	WIDGET_OrbitSelector_LatZZ.description = 'LatZZ'
	WIDGET_OrbitSelector_LatZZ.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_LatZZ,)
	global WIDGET_OrbitSelector_SRXXHZ
	WIDGET_OrbitSelector_SRXXHZ = widgets.Dropdown( options=['Srt16Hz', 'Srt01Hz'],  description='Variable')
	WIDGET_OrbitSelector_SRXXHZ.description = 'SRXXHZ'
	WIDGET_OrbitSelector_SRXXHZ.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_SRXXHZ,)
	global WIDGET_OrbitSelector_SC
	WIDGET_OrbitSelector_SC = widgets.Dropdown( options=['Msc', 'Ssc'],  description='Variable')
	WIDGET_OrbitSelector_SC.description = 'SC'
	WIDGET_OrbitSelector_SC.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_SC,)
	IRI16_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	OrbitSelector_Btn = widgets.Button (
		description='OrbitSelector',
		tooltip="Constructs and returns an orbit full-path filename from the orbit properties.\nThe filename includes all parameters required to select the appropriate orbit.\nAll filenames  have the same length and same number of parameters. \nIn case OrbitFilename and EvtXY are empty then an empty string is returned.\nFILE FORMAT: DAED_ORB_EVTXY_TYP_PERYYY_LATZZ_SRTQQHz_XSC.csv\n  Parameter OrbitFilename:\n    If it is not empty then the rest arguments are ignored. \n    If it contains slashes then is is assumed it is a full path name and it is returned as it is.\n    If it does not contain slashes then the orbits path is added.\n    \n  Parameter EvtXY values:\n    EVTXS    X Event, Single Orbit\n    EVTXA    X Event, All Orbit\n    EVT1Y    1st Event: St Patrick’s day event [17 Mar 2015 – 20 Mar 2015]\n    EVT2Y    2nd Event ...  ...\n \n  Parameter TYP values:\n    LLA    Time,Latitude Longitude Altitude \n    VEL    Time,VmagVxVyVz\n    PTG    Time, X_GSE, Y_GSE, Z_GSE, RamX_GSE, RamY_GSE, RamZ_GSE\n  Parameter PerYYY values:\n    PER120, PER150    Perigee Altitude at 120km or 150km\n  Parameter LatZZ values:\n    LAT00, LAT40, LAT80    Perigee Latitude at 0°, 40° or 80°\n \n  Parameter SRXXHZ values:\n    SRT16Hz, SRT01Hz    Sampling rate 16Hz or 1HZ\n \n  Parameter SC values:\n    MSC    Mother Spacecraft\n    SSC    Sub-Spacecraft\n",
	)
	OrbitSelector_Btn.layout.min_width = '200px'
	OrbitSelector_Btn.style.button_color = 'YellowGreen'
	IRI16_Panel.children += (OrbitSelector_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_OrbitSelector_OrbitFilename = widgets.Label(value='  --> OrbitFilename  ')
	WIDGET_OrbitSelector_OrbitFilename.layout.border = '1px dashed green'
	WIDGET_OrbitSelector_OrbitFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_OrbitSelector_OrbitFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_OrbitSelector_OrbitFilename,)
	IRI16_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'Selector'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	global WIDGET_Selector_MeshgridCSVfilename
	WIDGET_Selector_MeshgridCSVfilename = widgets.Text(value="")
	WIDGET_Selector_MeshgridCSVfilename.description = 'MeshgridCSVfilename'
	WIDGET_Selector_MeshgridCSVfilename.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Selector_MeshgridCSVfilename,)
	global WIDGET_Selector_MeshgridDatetime
	WIDGET_Selector_MeshgridDatetime = widgets.Text(value="Mar 17 2015 00:50:00.000000000")
	WIDGET_Selector_MeshgridDatetime.description = 'MeshgridDatetime'
	WIDGET_Selector_MeshgridDatetime.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Selector_MeshgridDatetime,)
	global WIDGET_Selector_MeshgridAltitude
	WIDGET_Selector_MeshgridAltitude = widgets.FloatText(value=120)
	WIDGET_Selector_MeshgridAltitude.description = 'MeshgridAltitude'
	WIDGET_Selector_MeshgridAltitude.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Selector_MeshgridAltitude,)
	global WIDGET_Selector_MeshgridLatitudeStep
	WIDGET_Selector_MeshgridLatitudeStep = widgets.FloatText(value=5)
	WIDGET_Selector_MeshgridLatitudeStep.description = 'MeshgridLatitudeStep'
	WIDGET_Selector_MeshgridLatitudeStep.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Selector_MeshgridLatitudeStep,)
	global WIDGET_Selector_MeshgridLongitudeStep
	WIDGET_Selector_MeshgridLongitudeStep = widgets.FloatText(value=5)
	WIDGET_Selector_MeshgridLongitudeStep.description = 'MeshgridLongitudeStep'
	WIDGET_Selector_MeshgridLongitudeStep.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Selector_MeshgridLongitudeStep,)
	global WIDGET_Selector_NoiseWx
	WIDGET_Selector_NoiseWx = widgets.FloatText(value=0)
	WIDGET_Selector_NoiseWx.description = 'NoiseWx'
	WIDGET_Selector_NoiseWx.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Selector_NoiseWx,)
	global WIDGET_Selector_NoiseWy
	WIDGET_Selector_NoiseWy = widgets.FloatText(value=0)
	WIDGET_Selector_NoiseWy.description = 'NoiseWy'
	WIDGET_Selector_NoiseWy.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Selector_NoiseWy,)
	global WIDGET_Selector_NoiseAx
	WIDGET_Selector_NoiseAx = widgets.FloatText(value=0)
	WIDGET_Selector_NoiseAx.description = 'NoiseAx'
	WIDGET_Selector_NoiseAx.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Selector_NoiseAx,)
	global WIDGET_Selector_NoiseAy
	WIDGET_Selector_NoiseAy = widgets.FloatText(value=0)
	WIDGET_Selector_NoiseAy.description = 'NoiseAy'
	WIDGET_Selector_NoiseAy.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Selector_NoiseAy,)
	global WIDGET_Selector_IRI16_variableForMeshgrid
	WIDGET_Selector_IRI16_variableForMeshgrid = widgets.Dropdown( options=['', 'Op', 'O2p', 'Te', 'Ti', 'Ne'], value='', description='Variable')
	WIDGET_Selector_IRI16_variableForMeshgrid.description = 'IRI16_variableForMeshgrid'
	WIDGET_Selector_IRI16_variableForMeshgrid.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Selector_IRI16_variableForMeshgrid,)
	global WIDGET_Selector_IRI16_variableForOrbit
	WIDGET_Selector_IRI16_variableForOrbit = widgets.Dropdown( options=['', 'Op', 'O2p', 'Te', 'Ti', 'Ne'], value='', description='Variable')
	WIDGET_Selector_IRI16_variableForOrbit.description = 'IRI16_variableForOrbit'
	WIDGET_Selector_IRI16_variableForOrbit.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Selector_IRI16_variableForOrbit,)
	IRI16_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	Selector_Btn = widgets.Button (
		description='Selector',
		tooltip="Functions as a single point which collects all user input and distributes it to the various modules of this group",
	)
	Selector_Btn.layout.min_width = '200px'
	Selector_Btn.style.button_color = 'gold'
	IRI16_Panel.children += (Selector_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_Selector_MeshgridCSVfilenameOUT = widgets.Label(value='  --> MeshgridCSVfilenameOUT  ')
	WIDGET_Selector_MeshgridCSVfilenameOUT.layout.border = '1px dashed green'
	WIDGET_Selector_MeshgridCSVfilenameOUT.layout.margin ='0px 40px 0px 0px' 
	WIDGET_Selector_MeshgridCSVfilenameOUT.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_Selector_MeshgridCSVfilenameOUT,)
	WIDGET_Selector_MeshgridDatetimeOUT = widgets.Label(value='  --> MeshgridDatetimeOUT  ')
	WIDGET_Selector_MeshgridDatetimeOUT.layout.border = '1px dashed green'
	WIDGET_Selector_MeshgridDatetimeOUT.layout.margin ='0px 40px 0px 0px' 
	WIDGET_Selector_MeshgridDatetimeOUT.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_Selector_MeshgridDatetimeOUT,)
	WIDGET_Selector_MeshgridAltitudeOUT = widgets.Label(value='  --> MeshgridAltitudeOUT  ')
	WIDGET_Selector_MeshgridAltitudeOUT.layout.border = '1px dashed green'
	WIDGET_Selector_MeshgridAltitudeOUT.layout.margin ='0px 40px 0px 0px' 
	WIDGET_Selector_MeshgridAltitudeOUT.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_Selector_MeshgridAltitudeOUT,)
	WIDGET_Selector_MeshgridLatitudeStepOUT = widgets.Label(value='  --> MeshgridLatitudeStepOUT  ')
	WIDGET_Selector_MeshgridLatitudeStepOUT.layout.border = '1px dashed green'
	WIDGET_Selector_MeshgridLatitudeStepOUT.layout.margin ='0px 40px 0px 0px' 
	WIDGET_Selector_MeshgridLatitudeStepOUT.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_Selector_MeshgridLatitudeStepOUT,)
	WIDGET_Selector_MeshgridLongitudeStepOUT = widgets.Label(value='  --> MeshgridLongitudeStepOUT  ')
	WIDGET_Selector_MeshgridLongitudeStepOUT.layout.border = '1px dashed green'
	WIDGET_Selector_MeshgridLongitudeStepOUT.layout.margin ='0px 40px 0px 0px' 
	WIDGET_Selector_MeshgridLongitudeStepOUT.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_Selector_MeshgridLongitudeStepOUT,)
	WIDGET_Selector_NoiseWxOUT = widgets.Label(value='  --> NoiseWxOUT  ')
	WIDGET_Selector_NoiseWxOUT.layout.border = '1px dashed green'
	WIDGET_Selector_NoiseWxOUT.layout.margin ='0px 40px 0px 0px' 
	WIDGET_Selector_NoiseWxOUT.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_Selector_NoiseWxOUT,)
	WIDGET_Selector_NoiseWyOUT = widgets.Label(value='  --> NoiseWyOUT  ')
	WIDGET_Selector_NoiseWyOUT.layout.border = '1px dashed green'
	WIDGET_Selector_NoiseWyOUT.layout.margin ='0px 40px 0px 0px' 
	WIDGET_Selector_NoiseWyOUT.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_Selector_NoiseWyOUT,)
	WIDGET_Selector_NoiseAxOUT = widgets.Label(value='  --> NoiseAxOUT  ')
	WIDGET_Selector_NoiseAxOUT.layout.border = '1px dashed green'
	WIDGET_Selector_NoiseAxOUT.layout.margin ='0px 40px 0px 0px' 
	WIDGET_Selector_NoiseAxOUT.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_Selector_NoiseAxOUT,)
	WIDGET_Selector_NoiseAyOUT = widgets.Label(value='  --> NoiseAyOUT  ')
	WIDGET_Selector_NoiseAyOUT.layout.border = '1px dashed green'
	WIDGET_Selector_NoiseAyOUT.layout.margin ='0px 40px 0px 0px' 
	WIDGET_Selector_NoiseAyOUT.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_Selector_NoiseAyOUT,)
	WIDGET_Selector_IRI16_variableForMeshgrid_OUT = widgets.Label(value='  --> IRI16_variableForMeshgrid_OUT  ')
	WIDGET_Selector_IRI16_variableForMeshgrid_OUT.layout.border = '1px dashed green'
	WIDGET_Selector_IRI16_variableForMeshgrid_OUT.layout.margin ='0px 40px 0px 0px' 
	WIDGET_Selector_IRI16_variableForMeshgrid_OUT.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_Selector_IRI16_variableForMeshgrid_OUT,)
	WIDGET_Selector_IRI16_variableForOrbit_OUT = widgets.Label(value='  --> IRI16_variableForOrbit_OUT  ')
	WIDGET_Selector_IRI16_variableForOrbit_OUT.layout.border = '1px dashed green'
	WIDGET_Selector_IRI16_variableForOrbit_OUT.layout.margin ='0px 40px 0px 0px' 
	WIDGET_Selector_IRI16_variableForOrbit_OUT.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_Selector_IRI16_variableForOrbit_OUT,)
	IRI16_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'CreateCSV_Sphere'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_CreateCSV_Sphere_CSVfilename = widgets.Label(value='  Selector.MeshgridCSVfilenameOUT --> CSVfilename  ')
	WIDGET_CreateCSV_Sphere_CSVfilename.layout.border = '1px dashed blue'
	WIDGET_CreateCSV_Sphere_CSVfilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_CreateCSV_Sphere_CSVfilename,)
	WIDGET_CreateCSV_Sphere_fixedDatetimeString = widgets.Label(value='  Selector.MeshgridDatetimeOUT --> fixedDatetimeString  ')
	WIDGET_CreateCSV_Sphere_fixedDatetimeString.layout.border = '1px dashed blue'
	WIDGET_CreateCSV_Sphere_fixedDatetimeString.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_CreateCSV_Sphere_fixedDatetimeString,)
	WIDGET_CreateCSV_Sphere_fixedAltitude = widgets.Label(value='  Selector.MeshgridAltitudeOUT --> fixedAltitude  ')
	WIDGET_CreateCSV_Sphere_fixedAltitude.layout.border = '1px dashed blue'
	WIDGET_CreateCSV_Sphere_fixedAltitude.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_CreateCSV_Sphere_fixedAltitude,)
	WIDGET_CreateCSV_Sphere_LatitudeStep = widgets.Label(value='  Selector.MeshgridLatitudeStepOUT --> LatitudeStep  ')
	WIDGET_CreateCSV_Sphere_LatitudeStep.layout.border = '1px dashed blue'
	WIDGET_CreateCSV_Sphere_LatitudeStep.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_CreateCSV_Sphere_LatitudeStep,)
	WIDGET_CreateCSV_Sphere_LongitudeStep = widgets.Label(value='  Selector.MeshgridLongitudeStepOUT --> LongitudeStep  ')
	WIDGET_CreateCSV_Sphere_LongitudeStep.layout.border = '1px dashed blue'
	WIDGET_CreateCSV_Sphere_LongitudeStep.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_CreateCSV_Sphere_LongitudeStep,)
	IRI16_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	CreateCSV_Sphere_Btn = widgets.Button (
		description='CreateCSV_Sphere',
		tooltip="Creates a CSV file with the format [Time, Lat, Lon, Alt]\nTime and Alt are fixed values given as arguments and Lat and Lon are produced for the whole globe accodring to steps specified.\nCSVfilename: string, the csv filename to be written (overwrite mode)\nfixedDatetimeString: string, the date-time fixed text with format as example: Mar 17 2015 00:12:00.000. Fixed value for every csv entry.\nfixedAltitude: float positive, kilometers above earth. Fixed value for every csv entry.\nLatitudeStep: float positive, Latiude values range between 87.5 and -88.5. The step is how Lat should be incremented at each iteration.\nLongitudeStep: float positive, Longitude values range between -180 and 180.  The step is how Lon should be incremented at each iteration.\nRETURNS: the filename it has written (same as the argument)\n         the altitude (same as the argument)\n         the number of lines written",
	)
	CreateCSV_Sphere_Btn.layout.min_width = '200px'
	CreateCSV_Sphere_Btn.style.button_color = 'gold'
	IRI16_Panel.children += (CreateCSV_Sphere_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_CreateCSV_Sphere_theCSVfilename = widgets.Label(value='  --> theCSVfilename  ')
	WIDGET_CreateCSV_Sphere_theCSVfilename.layout.border = '1px dashed green'
	WIDGET_CreateCSV_Sphere_theCSVfilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_CreateCSV_Sphere_theCSVfilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_CreateCSV_Sphere_theCSVfilename,)
	WIDGET_CreateCSV_Sphere_theAltitude = widgets.Label(value='  --> theAltitude  ')
	WIDGET_CreateCSV_Sphere_theAltitude.layout.border = '1px dashed green'
	WIDGET_CreateCSV_Sphere_theAltitude.layout.margin ='0px 40px 0px 0px' 
	WIDGET_CreateCSV_Sphere_theAltitude.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_CreateCSV_Sphere_theAltitude,)
	WIDGET_CreateCSV_Sphere_NumberOfLinesWritten = widgets.Label(value='  --> NumberOfLinesWritten  ')
	WIDGET_CreateCSV_Sphere_NumberOfLinesWritten.layout.border = '1px dashed green'
	WIDGET_CreateCSV_Sphere_NumberOfLinesWritten.layout.margin ='0px 40px 0px 0px' 
	WIDGET_CreateCSV_Sphere_NumberOfLinesWritten.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_CreateCSV_Sphere_NumberOfLinesWritten,)
	IRI16_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'IRI16'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_IRI16_FilenameCSV_forMeshgrid = widgets.Label(value='  CreateCSV_Sphere.theCSVfilename --> FilenameCSV_forMeshgrid  ')
	WIDGET_IRI16_FilenameCSV_forMeshgrid.layout.border = '1px dashed blue'
	WIDGET_IRI16_FilenameCSV_forMeshgrid.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_IRI16_FilenameCSV_forMeshgrid,)
	WIDGET_IRI16_Variable_forMeshgrid = widgets.Label(value='  Selector.IRI16_variableForMeshgrid_OUT --> Variable_forMeshgrid  ')
	WIDGET_IRI16_Variable_forMeshgrid.layout.border = '1px dashed blue'
	WIDGET_IRI16_Variable_forMeshgrid.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_IRI16_Variable_forMeshgrid,)
	IRI16_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	IRI16_Btn = widgets.Button (
		description='IRI16',
		tooltip="International Reference Ionosphere empirical model (IRI)\nfilename: the CSV file to read. Format: Time,Alt,Lon,Lat. The file defines the coordinates for which the IRI calculation will take place.\nParameter: selects which values to calculate. Possible values are:\n    ''   for all\n    'Op'  for Oxygen+\n    'O2p' for Oxygen2+\n    'Te' for Electron Temperature\n    'Ti' for Ion Temperature\nReturns: the name of the CSV file which contains the calculated values. Format: Time,Alt,Lon,Lat,Op,O2p,Te,Ti",
	)
	IRI16_Btn.layout.min_width = '200px'
	IRI16_Btn.style.button_color = 'salmon'
	IRI16_Panel.children += (IRI16_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_IRI16_MeshgridResultCSV = widgets.Label(value='  --> MeshgridResultCSV  ')
	WIDGET_IRI16_MeshgridResultCSV.layout.border = '1px dashed green'
	WIDGET_IRI16_MeshgridResultCSV.layout.margin ='0px 40px 0px 0px' 
	WIDGET_IRI16_MeshgridResultCSV.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_IRI16_MeshgridResultCSV,)
	IRI16_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'IRI16'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_IRI16_CSVfilenameOrbit = widgets.Label(value='  OrbitSelector.OrbitFilename --> CSVfilenameOrbit  ')
	WIDGET_IRI16_CSVfilenameOrbit.layout.border = '1px dashed blue'
	WIDGET_IRI16_CSVfilenameOrbit.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_IRI16_CSVfilenameOrbit,)
	WIDGET_IRI16_VariableOrbit = widgets.Label(value='  Selector.IRI16_variableForOrbit_OUT --> VariableOrbit  ')
	WIDGET_IRI16_VariableOrbit.layout.border = '1px dashed blue'
	WIDGET_IRI16_VariableOrbit.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_IRI16_VariableOrbit,)
	IRI16_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	IRI16_Btn = widgets.Button (
		description='IRI16',
		tooltip="International Reference Ionosphere empirical model (IRI)\nfilename: the CSV file to read. Format: Time,Alt,Lon,Lat. The file defines the coordinates for which the IRI calculation will take place.\nParameter: selects which values to calculate. Possible values are:\n    ''   for all\n    'Op'  for Oxygen+\n    'O2p' for Oxygen2+\n    'Te' for Electron Temperature\n    'Ti' for Ion Temperature\nReturns: the name of the CSV file which contains the calculated values. Format: Time,Alt,Lon,Lat,Op,O2p,Te,Ti",
	)
	IRI16_Btn.layout.min_width = '200px'
	IRI16_Btn.style.button_color = 'salmon'
	IRI16_Panel.children += (IRI16_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_IRI16_orbitCSVfilename = widgets.Label(value='  --> orbitCSVfilename  ')
	WIDGET_IRI16_orbitCSVfilename.layout.border = '1px dashed green'
	WIDGET_IRI16_orbitCSVfilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_IRI16_orbitCSVfilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_IRI16_orbitCSVfilename,)
	IRI16_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'SubGridVariability'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_SubGridVariability_NoiseWx = widgets.Label(value='  Selector.NoiseWxOUT --> NoiseWx  ')
	WIDGET_SubGridVariability_NoiseWx.layout.border = '1px dashed blue'
	WIDGET_SubGridVariability_NoiseWx.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_SubGridVariability_NoiseWx,)
	WIDGET_SubGridVariability_NoiseWy = widgets.Label(value='  Selector.NoiseWyOUT --> NoiseWy  ')
	WIDGET_SubGridVariability_NoiseWy.layout.border = '1px dashed blue'
	WIDGET_SubGridVariability_NoiseWy.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_SubGridVariability_NoiseWy,)
	WIDGET_SubGridVariability_NoiseAx = widgets.Label(value='  Selector.NoiseAxOUT --> NoiseAx  ')
	WIDGET_SubGridVariability_NoiseAx.layout.border = '1px dashed blue'
	WIDGET_SubGridVariability_NoiseAx.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_SubGridVariability_NoiseAx,)
	WIDGET_SubGridVariability_NoiseAy = widgets.Label(value='  Selector.NoiseAyOUT --> NoiseAy  ')
	WIDGET_SubGridVariability_NoiseAy.layout.border = '1px dashed blue'
	WIDGET_SubGridVariability_NoiseAy.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_SubGridVariability_NoiseAy,)
	WIDGET_SubGridVariability_filename = widgets.Label(value='  IRI16.orbitCSVfilename --> filename  ')
	WIDGET_SubGridVariability_filename.layout.border = '1px dashed blue'
	WIDGET_SubGridVariability_filename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_SubGridVariability_filename,)
	global WIDGET_SubGridVariability_ValueName
	WIDGET_SubGridVariability_ValueName = widgets.Text()
	WIDGET_SubGridVariability_ValueName.description = 'ValueName'
	WIDGET_SubGridVariability_ValueName.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_SubGridVariability_ValueName,)
	IRI16_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	SubGridVariability_Btn = widgets.Button (
		description='SubGridVariability',
		tooltip="Inputs\n NoiseAx,NoiseAy: real:: Amplitude of noise Kind (values 0-100)\n NoiseWx,NoiseWy: real:: Wavenumber of noise Kind (values 0-1000)\n Filename: Character:: field to read orbit from\n ValueName: Character:: variable from model data to use and add SGV. Corresponds to CSV Column\nOutputs\n Plots..\nReturns\n a csv filename of format Time, Lat, Lon, Alt, value containing the altered-with-noise values",
	)
	SubGridVariability_Btn.layout.min_width = '200px'
	SubGridVariability_Btn.style.button_color = 'gold'
	IRI16_Panel.children += (SubGridVariability_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_SubGridVariability_VariabilityCSVfilename = widgets.Label(value='  --> VariabilityCSVfilename  ')
	WIDGET_SubGridVariability_VariabilityCSVfilename.layout.border = '1px dashed green'
	WIDGET_SubGridVariability_VariabilityCSVfilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_SubGridVariability_VariabilityCSVfilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_SubGridVariability_VariabilityCSVfilename,)
	IRI16_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'PlotGlobe'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_PlotGlobe_CSVfilename_Meshgrid = widgets.Label(value='  IRI16.MeshgridResultCSV --> CSVfilename_Meshgrid  ')
	WIDGET_PlotGlobe_CSVfilename_Meshgrid.layout.border = '1px dashed blue'
	WIDGET_PlotGlobe_CSVfilename_Meshgrid.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_PlotGlobe_CSVfilename_Meshgrid,)
	WIDGET_PlotGlobe_CSVfilename_Orbit = widgets.Label(value='  SubGridVariability.VariabilityCSVfilename --> CSVfilename_Orbit  ')
	WIDGET_PlotGlobe_CSVfilename_Orbit.layout.border = '1px dashed blue'
	WIDGET_PlotGlobe_CSVfilename_Orbit.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_PlotGlobe_CSVfilename_Orbit,)
	global WIDGET_PlotGlobe_PlotTitle
	WIDGET_PlotGlobe_PlotTitle = widgets.Text()
	WIDGET_PlotGlobe_PlotTitle.description = 'PlotTitle'
	WIDGET_PlotGlobe_PlotTitle.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_PlotGlobe_PlotTitle,)
	global WIDGET_PlotGlobe_ColorbarTitle
	WIDGET_PlotGlobe_ColorbarTitle = widgets.Text()
	WIDGET_PlotGlobe_ColorbarTitle.description = 'ColorbarTitle'
	WIDGET_PlotGlobe_ColorbarTitle.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_PlotGlobe_ColorbarTitle,)
	global WIDGET_PlotGlobe_ColorscaleName
	WIDGET_PlotGlobe_ColorscaleName = widgets.Text(value="Jet")
	WIDGET_PlotGlobe_ColorscaleName.description = 'ColorscaleName'
	WIDGET_PlotGlobe_ColorscaleName.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_PlotGlobe_ColorscaleName,)
	IRI16_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	PlotGlobe_Btn = widgets.Button (
		description='PlotGlobe',
		tooltip="Creates a 3D plot of an earth globe, a sphere surface and a satellite orbit. The surface and the orbit are colored according to the data values in the CSV files.\n  DataCSVfilename: format: Time,Lat,Lon,Alt,value. Contains the data for the sphere surface. If empty then no surface will be plotted.\n  OrbitDataCSVfilename: format: Time,Lat,Lon,Alt,value. Contains the data for the orbit. If empty then no orbit will be plotted.\n  PlotTitle: the title of the plot. It will be displayed at the top of the globe.\n  ColorbarTitle: the title of the colorbar beside the globe. Usually contains measuremnt units\n  ColorscaleName: valid values are: ‘Blackbody’, ‘Bluered’, ‘Blues’, ‘Earth’, ‘Electric’, ‘Greens’, ‘Greys’, ‘Hot’, ‘Jet’, ‘Picnic’, ‘Portland’, ‘Rainbow’, ‘RdBu’, ‘Reds’, ‘Viridis’, ‘YlGnBu’, ‘YlOrRd’\n                  In case an empty string is passed then a default HeatMap colorscale will be applied.\n                  In case None is passed then all points will be black irrespective of value.\n  RETURNS: a string containing information about the Data",
	)
	PlotGlobe_Btn.layout.min_width = '200px'
	PlotGlobe_Btn.style.button_color = 'deeppink'
	IRI16_Panel.children += (PlotGlobe_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	IRI16_Panel.children += (OutputsPanel,)
	return IRI16_Panel


def Construct_HWM14():
	#Create Containers
	HWM14_Panel = widgets.Box()
	HWM14_Panel.layout.overflow_x = 'scroll'
	HWM14_Panel.layout.flex_flow = 'row'
	HWM14_Panel.layout.display = 'flex'
	########
	## GUI code for module 'OrbitSelector'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	global WIDGET_OrbitSelector_Filename
	WIDGET_OrbitSelector_Filename = widgets.Text()
	WIDGET_OrbitSelector_Filename.description = 'Filename'
	WIDGET_OrbitSelector_Filename.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_Filename,)
	global WIDGET_OrbitSelector_EvtXY
	WIDGET_OrbitSelector_EvtXY = widgets.Dropdown( options=['', 'Evt0', 'Evt1', 'Evt2', 'Evt3', 'Evt4', 'Evt5', 'Evt6', 'Evt7', 'Evt8', 'Evt9'], description='Variable')
	WIDGET_OrbitSelector_EvtXY.description = 'EvtXY'
	WIDGET_OrbitSelector_EvtXY.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_EvtXY,)
	global WIDGET_OrbitSelector_TYP
	WIDGET_OrbitSelector_TYP = widgets.Dropdown( options=['LLA', 'VEL', 'PTG'], description='Variable')
	WIDGET_OrbitSelector_TYP.description = 'TYP'
	WIDGET_OrbitSelector_TYP.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_TYP,)
	global WIDGET_OrbitSelector_PerYYY
	WIDGET_OrbitSelector_PerYYY = widgets.Dropdown( options=['Per120', 'Per150'], description='Variable')
	WIDGET_OrbitSelector_PerYYY.description = 'PerYYY'
	WIDGET_OrbitSelector_PerYYY.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_PerYYY,)
	global WIDGET_OrbitSelector_LatZZ
	WIDGET_OrbitSelector_LatZZ = widgets.Dropdown( options=['Lat00', 'Lat40', 'Lat80'],  description='Variable')
	WIDGET_OrbitSelector_LatZZ.description = 'LatZZ'
	WIDGET_OrbitSelector_LatZZ.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_LatZZ,)
	global WIDGET_OrbitSelector_SRXXHZ
	WIDGET_OrbitSelector_SRXXHZ = widgets.Dropdown( options=['Srt16Hz', 'Srt01Hz'],  description='Variable')
	WIDGET_OrbitSelector_SRXXHZ.description = 'SRXXHZ'
	WIDGET_OrbitSelector_SRXXHZ.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_SRXXHZ,)
	global WIDGET_OrbitSelector_SC
	WIDGET_OrbitSelector_SC = widgets.Dropdown( options=['Msc', 'Ssc'],  description='Variable')
	WIDGET_OrbitSelector_SC.description = 'SC'
	WIDGET_OrbitSelector_SC.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_SC,)
	HWM14_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	OrbitSelector_Btn = widgets.Button (
		description='OrbitSelector',
		tooltip="Constructs and returns an orbit full-path filename from the orbit properties.\nThe filename includes all parameters required to select the appropriate orbit.\nAll filenames  have the same length and same number of parameters. \nIn case OrbitFilename and EvtXY are empty then an empty string is returned.\nFILE FORMAT: DAED_ORB_EVTXY_TYP_PERYYY_LATZZ_SRTQQHz_XSC.csv\n  Parameter OrbitFilename:\n    If it is not empty then the rest arguments are ignored. \n    If it contains slashes then is is assumed it is a full path name and it is returned as it is.\n    If it does not contain slashes then the orbits path is added.\n    \n  Parameter EvtXY values:\n    EVTXS    X Event, Single Orbit\n    EVTXA    X Event, All Orbit\n    EVT1Y    1st Event: St Patrick’s day event [17 Mar 2015 – 20 Mar 2015]\n    EVT2Y    2nd Event ...  ...\n \n  Parameter TYP values:\n    LLA    Time,Latitude Longitude Altitude \n    VEL    Time,VmagVxVyVz\n    PTG    Time, X_GSE, Y_GSE, Z_GSE, RamX_GSE, RamY_GSE, RamZ_GSE\n  Parameter PerYYY values:\n    PER120, PER150    Perigee Altitude at 120km or 150km\n  Parameter LatZZ values:\n    LAT00, LAT40, LAT80    Perigee Latitude at 0°, 40° or 80°\n \n  Parameter SRXXHZ values:\n    SRT16Hz, SRT01Hz    Sampling rate 16Hz or 1HZ\n \n  Parameter SC values:\n    MSC    Mother Spacecraft\n    SSC    Sub-Spacecraft\n",
	)
	OrbitSelector_Btn.layout.min_width = '200px'
	OrbitSelector_Btn.style.button_color = 'YellowGreen'
	HWM14_Panel.children += (OrbitSelector_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_OrbitSelector_OrbitFilename = widgets.Label(value='  --> OrbitFilename  ')
	WIDGET_OrbitSelector_OrbitFilename.layout.border = '1px dashed green'
	WIDGET_OrbitSelector_OrbitFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_OrbitSelector_OrbitFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_OrbitSelector_OrbitFilename,)
	HWM14_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'HWM14'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_HWM14_CSVfilename_forOrbit = widgets.Label(value='  OrbitSelector.OrbitFilename --> CSVfilename_forOrbit  ')
	WIDGET_HWM14_CSVfilename_forOrbit.layout.border = '1px dashed blue'
	WIDGET_HWM14_CSVfilename_forOrbit.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_HWM14_CSVfilename_forOrbit,)
	global WIDGET_HWM14_Variable_forOrbit
	WIDGET_HWM14_Variable_forOrbit = widgets.Dropdown( options=['', 'v', 'u'], value='', description='Variable')
	WIDGET_HWM14_Variable_forOrbit.description = 'Variable_forOrbit'
	WIDGET_HWM14_Variable_forOrbit.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_HWM14_Variable_forOrbit,)
	HWM14_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	HWM14_Btn = widgets.Button (
		description='HWM14',
		tooltip="Horizontal Wind Model empirical (HWM) \nfilename: the CSV file to read. Format: Time,Alt,Lon,Lat. The file defines the coordinates for which the HWM calculation will take place.\nParameter: selects which values to calculate. Possible values are:\n    ''  for all\n    'v' for meridional wind (northward) \n    'u' for zonal wind (eastward)  \nReturns: the name of the CSV file which contains the calculated values. Format: Time,Alt,Lon,Lat,v,u \n",
	)
	HWM14_Btn.layout.min_width = '200px'
	HWM14_Btn.style.button_color = 'gold'
	HWM14_Panel.children += (HWM14_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_HWM14_OrbitResultCSV = widgets.Label(value='  --> OrbitResultCSV  ')
	WIDGET_HWM14_OrbitResultCSV.layout.border = '1px dashed green'
	WIDGET_HWM14_OrbitResultCSV.layout.margin ='0px 40px 0px 0px' 
	WIDGET_HWM14_OrbitResultCSV.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_HWM14_OrbitResultCSV,)
	HWM14_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'CreateCSV_Sphere'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	global WIDGET_CreateCSV_Sphere_CSVfilename
	WIDGET_CreateCSV_Sphere_CSVfilename = widgets.Text(value="")
	WIDGET_CreateCSV_Sphere_CSVfilename.description = 'CSVfilename'
	WIDGET_CreateCSV_Sphere_CSVfilename.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_CreateCSV_Sphere_CSVfilename,)
	global WIDGET_CreateCSV_Sphere_fixedDatetimeString
	WIDGET_CreateCSV_Sphere_fixedDatetimeString = widgets.Text(value="Mar 17 2015 00:50:00.000000000")
	WIDGET_CreateCSV_Sphere_fixedDatetimeString.description = 'fixedDatetimeString'
	WIDGET_CreateCSV_Sphere_fixedDatetimeString.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_CreateCSV_Sphere_fixedDatetimeString,)
	global WIDGET_CreateCSV_Sphere_fixedAltitude
	WIDGET_CreateCSV_Sphere_fixedAltitude = widgets.FloatText(value=120)
	WIDGET_CreateCSV_Sphere_fixedAltitude.description = 'fixedAltitude'
	WIDGET_CreateCSV_Sphere_fixedAltitude.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_CreateCSV_Sphere_fixedAltitude,)
	global WIDGET_CreateCSV_Sphere_LatitudeStep
	WIDGET_CreateCSV_Sphere_LatitudeStep = widgets.FloatText(value=5)
	WIDGET_CreateCSV_Sphere_LatitudeStep.description = 'LatitudeStep'
	WIDGET_CreateCSV_Sphere_LatitudeStep.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_CreateCSV_Sphere_LatitudeStep,)
	global WIDGET_CreateCSV_Sphere_LongitudeStep
	WIDGET_CreateCSV_Sphere_LongitudeStep = widgets.FloatText(value=5)
	WIDGET_CreateCSV_Sphere_LongitudeStep.description = 'LongitudeStep'
	WIDGET_CreateCSV_Sphere_LongitudeStep.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_CreateCSV_Sphere_LongitudeStep,)
	HWM14_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	CreateCSV_Sphere_Btn = widgets.Button (
		description='CreateCSV_Sphere',
		tooltip="Creates a CSV file with the format [Time, Lat, Lon, Alt]\nTime and Alt are fixed values given as arguments and Lat and Lon are produced for the whole globe accodring to steps specified.\nCSVfilename: string, the csv filename to be written (overwrite mode)\nfixedDatetimeString: string, the date-time fixed text with format as example: Mar 17 2015 00:12:00.000. Fixed value for every csv entry.\nfixedAltitude: float positive, kilometers above earth. Fixed value for every csv entry.\nLatitudeStep: float positive, Latiude values range between 87.5 and -88.5. The step is how Lat should be incremented at each iteration.\nLongitudeStep: float positive, Longitude values range between -180 and 180.  The step is how Lon should be incremented at each iteration.\nRETURNS: the filename it has written (same as the argument)\n         the altitude (same as the argument)\n         the number of lines written",
	)
	CreateCSV_Sphere_Btn.layout.min_width = '200px'
	CreateCSV_Sphere_Btn.style.button_color = 'gold'
	HWM14_Panel.children += (CreateCSV_Sphere_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_CreateCSV_Sphere_theCSVfilename = widgets.Label(value='  --> theCSVfilename  ')
	WIDGET_CreateCSV_Sphere_theCSVfilename.layout.border = '1px dashed green'
	WIDGET_CreateCSV_Sphere_theCSVfilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_CreateCSV_Sphere_theCSVfilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_CreateCSV_Sphere_theCSVfilename,)
	WIDGET_CreateCSV_Sphere_theAltitude = widgets.Label(value='  --> theAltitude  ')
	WIDGET_CreateCSV_Sphere_theAltitude.layout.border = '1px dashed green'
	WIDGET_CreateCSV_Sphere_theAltitude.layout.margin ='0px 40px 0px 0px' 
	WIDGET_CreateCSV_Sphere_theAltitude.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_CreateCSV_Sphere_theAltitude,)
	WIDGET_CreateCSV_Sphere_NumberOfLinesWritten = widgets.Label(value='  --> NumberOfLinesWritten  ')
	WIDGET_CreateCSV_Sphere_NumberOfLinesWritten.layout.border = '1px dashed green'
	WIDGET_CreateCSV_Sphere_NumberOfLinesWritten.layout.margin ='0px 40px 0px 0px' 
	WIDGET_CreateCSV_Sphere_NumberOfLinesWritten.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_CreateCSV_Sphere_NumberOfLinesWritten,)
	HWM14_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'HWM14'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_HWM14_CSVfilename_forMeshgrid = widgets.Label(value='  CreateCSV_Sphere.theCSVfilename --> CSVfilename_forMeshgrid  ')
	WIDGET_HWM14_CSVfilename_forMeshgrid.layout.border = '1px dashed blue'
	WIDGET_HWM14_CSVfilename_forMeshgrid.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_HWM14_CSVfilename_forMeshgrid,)
	global WIDGET_HWM14_Variable_forMeshgrid
	WIDGET_HWM14_Variable_forMeshgrid = widgets.Dropdown( options=['', 'v', 'u'], value='', description='Variable')
	WIDGET_HWM14_Variable_forMeshgrid.description = 'Variable_forMeshgrid'
	WIDGET_HWM14_Variable_forMeshgrid.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_HWM14_Variable_forMeshgrid,)
	HWM14_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	HWM14_Btn = widgets.Button (
		description='HWM14',
		tooltip="Horizontal Wind Model empirical (HWM) \nfilename: the CSV file to read. Format: Time,Alt,Lon,Lat. The file defines the coordinates for which the HWM calculation will take place.\nParameter: selects which values to calculate. Possible values are:\n    ''  for all\n    'v' for meridional wind (northward) \n    'u' for zonal wind (eastward)  \nReturns: the name of the CSV file which contains the calculated values. Format: Time,Alt,Lon,Lat,v,u \n",
	)
	HWM14_Btn.layout.min_width = '200px'
	HWM14_Btn.style.button_color = 'gold'
	HWM14_Panel.children += (HWM14_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_HWM14_MeshgridResultCSV = widgets.Label(value='  --> MeshgridResultCSV  ')
	WIDGET_HWM14_MeshgridResultCSV.layout.border = '1px dashed green'
	WIDGET_HWM14_MeshgridResultCSV.layout.margin ='0px 40px 0px 0px' 
	WIDGET_HWM14_MeshgridResultCSV.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_HWM14_MeshgridResultCSV,)
	HWM14_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'PlotGlobe'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_PlotGlobe_CSVfilename_Meshgrid = widgets.Label(value='  HWM14.MeshgridResultCSV --> CSVfilename_Meshgrid  ')
	WIDGET_PlotGlobe_CSVfilename_Meshgrid.layout.border = '1px dashed blue'
	WIDGET_PlotGlobe_CSVfilename_Meshgrid.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_PlotGlobe_CSVfilename_Meshgrid,)
	WIDGET_PlotGlobe_CSVfilename_Orbit = widgets.Label(value='  HWM14.OrbitResultCSV --> CSVfilename_Orbit  ')
	WIDGET_PlotGlobe_CSVfilename_Orbit.layout.border = '1px dashed blue'
	WIDGET_PlotGlobe_CSVfilename_Orbit.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_PlotGlobe_CSVfilename_Orbit,)
	global WIDGET_PlotGlobe_PlotTitle
	WIDGET_PlotGlobe_PlotTitle = widgets.Text()
	WIDGET_PlotGlobe_PlotTitle.description = 'PlotTitle'
	WIDGET_PlotGlobe_PlotTitle.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_PlotGlobe_PlotTitle,)
	global WIDGET_PlotGlobe_ColorbarTitle
	WIDGET_PlotGlobe_ColorbarTitle = widgets.Text()
	WIDGET_PlotGlobe_ColorbarTitle.description = 'ColorbarTitle'
	WIDGET_PlotGlobe_ColorbarTitle.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_PlotGlobe_ColorbarTitle,)
	global WIDGET_PlotGlobe_ColorscaleName
	WIDGET_PlotGlobe_ColorscaleName = widgets.Text(value="Jet")
	WIDGET_PlotGlobe_ColorscaleName.description = 'ColorscaleName'
	WIDGET_PlotGlobe_ColorscaleName.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_PlotGlobe_ColorscaleName,)
	HWM14_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	PlotGlobe_Btn = widgets.Button (
		description='PlotGlobe',
		tooltip="Creates a 3D plot of an earth globe, a sphere surface and a satellite orbit. The surface and the orbit are colored according to the data values in the CSV files.\n  DataCSVfilename: format: Time,Lat,Lon,Alt,value. Contains the data for the sphere surface. If empty then no surface will be plotted.\n  OrbitDataCSVfilename: format: Time,Lat,Lon,Alt,value. Contains the data for the orbit. If empty then no orbit will be plotted.\n  PlotTitle: the title of the plot. It will be displayed at the top of the globe.\n  ColorbarTitle: the title of the colorbar beside the globe. Usually contains measuremnt units\n  ColorscaleName: valid values are: ‘Blackbody’, ‘Bluered’, ‘Blues’, ‘Earth’, ‘Electric’, ‘Greens’, ‘Greys’, ‘Hot’, ‘Jet’, ‘Picnic’, ‘Portland’, ‘Rainbow’, ‘RdBu’, ‘Reds’, ‘Viridis’, ‘YlGnBu’, ‘YlOrRd’\n                  In case an empty string is passed then a default HeatMap colorscale will be applied.\n                  In case None is passed then all points will be black irrespective of value.\n  RETURNS: a string containing information about the Data",
	)
	PlotGlobe_Btn.layout.min_width = '200px'
	PlotGlobe_Btn.style.button_color = 'deeppink'
	HWM14_Panel.children += (PlotGlobe_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	HWM14_Panel.children += (OutputsPanel,)
	return HWM14_Panel


def Construct_IRI16_NetCDF():
	#Create Containers
	IRI16_NetCDF_Panel = widgets.Box()
	IRI16_NetCDF_Panel.layout.overflow_x = 'scroll'
	IRI16_NetCDF_Panel.layout.flex_flow = 'row'
	IRI16_NetCDF_Panel.layout.display = 'flex'
	########
	## GUI code for module 'OrbitSelector'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	global WIDGET_OrbitSelector_Filename
	WIDGET_OrbitSelector_Filename = widgets.Text()
	WIDGET_OrbitSelector_Filename.description = 'Filename'
	WIDGET_OrbitSelector_Filename.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_Filename,)
	global WIDGET_OrbitSelector_EvtXY
	WIDGET_OrbitSelector_EvtXY = widgets.Dropdown( options=['', 'Evt0', 'Evt1', 'Evt2', 'Evt3', 'Evt4', 'Evt5', 'Evt6', 'Evt7', 'Evt8', 'Evt9'], description='Variable')
	WIDGET_OrbitSelector_EvtXY.description = 'EvtXY'
	WIDGET_OrbitSelector_EvtXY.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_EvtXY,)
	global WIDGET_OrbitSelector_TYP
	WIDGET_OrbitSelector_TYP = widgets.Dropdown( options=['LLA', 'VEL', 'PTG'], description='Variable')
	WIDGET_OrbitSelector_TYP.description = 'TYP'
	WIDGET_OrbitSelector_TYP.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_TYP,)
	global WIDGET_OrbitSelector_PerYYY
	WIDGET_OrbitSelector_PerYYY = widgets.Dropdown( options=['Per120', 'Per150'], description='Variable')
	WIDGET_OrbitSelector_PerYYY.description = 'PerYYY'
	WIDGET_OrbitSelector_PerYYY.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_PerYYY,)
	global WIDGET_OrbitSelector_LatZZ
	WIDGET_OrbitSelector_LatZZ = widgets.Dropdown( options=['Lat00', 'Lat40', 'Lat80'],  description='Variable')
	WIDGET_OrbitSelector_LatZZ.description = 'LatZZ'
	WIDGET_OrbitSelector_LatZZ.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_LatZZ,)
	global WIDGET_OrbitSelector_SRXXHZ
	WIDGET_OrbitSelector_SRXXHZ = widgets.Dropdown( options=['Srt16Hz', 'Srt01Hz'],  description='Variable')
	WIDGET_OrbitSelector_SRXXHZ.description = 'SRXXHZ'
	WIDGET_OrbitSelector_SRXXHZ.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_SRXXHZ,)
	global WIDGET_OrbitSelector_SC
	WIDGET_OrbitSelector_SC = widgets.Dropdown( options=['Msc', 'Ssc'],  description='Variable')
	WIDGET_OrbitSelector_SC.description = 'SC'
	WIDGET_OrbitSelector_SC.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_OrbitSelector_SC,)
	IRI16_NetCDF_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	OrbitSelector_Btn = widgets.Button (
		description='OrbitSelector',
		tooltip="Constructs and returns an orbit full-path filename from the orbit properties.\nThe filename includes all parameters required to select the appropriate orbit.\nAll filenames  have the same length and same number of parameters. \nIn case OrbitFilename and EvtXY are empty then an empty string is returned.\nFILE FORMAT: DAED_ORB_EVTXY_TYP_PERYYY_LATZZ_SRTQQHz_XSC.csv\n  Parameter OrbitFilename:\n    If it is not empty then the rest arguments are ignored. \n    If it contains slashes then is is assumed it is a full path name and it is returned as it is.\n    If it does not contain slashes then the orbits path is added.\n    \n  Parameter EvtXY values:\n    EVTXS    X Event, Single Orbit\n    EVTXA    X Event, All Orbit\n    EVT1Y    1st Event: St Patrick's day event [17 Mar 2015 – 20 Mar 2015]\n    EVT2Y    2nd Event ...  ...\n \n  Parameter TYP values:\n    LLA    Time,Latitude Longitude Altitude \n    VEL    Time,VmagVxVyVz\n    PTG    Time, X_GSE, Y_GSE, Z_GSE, RamX_GSE, RamY_GSE, RamZ_GSE\n  Parameter PerYYY values:\n    PER120, PER150    Perigee Altitude at 120km or 150km\n  Parameter LatZZ values:\n    LAT00, LAT40, LAT80    Perigee Latitude at 0°, 40° or 80°\n \n  Parameter SRXXHZ values:\n    SRT16Hz, SRT01Hz    Sampling rate 16Hz or 1HZ\n \n  Parameter SC values:\n    MSC    Mother Spacecraft\n    SSC    Sub-Spacecraft\n",
	)
	OrbitSelector_Btn.layout.min_width = '200px'
	OrbitSelector_Btn.style.button_color = 'YellowGreen'
	IRI16_NetCDF_Panel.children += (OrbitSelector_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_OrbitSelector_OrbitCSVfilename = widgets.Label(value='  --> OrbitCSVfilename  ')
	WIDGET_OrbitSelector_OrbitCSVfilename.layout.border = '1px dashed green'
	WIDGET_OrbitSelector_OrbitCSVfilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_OrbitSelector_OrbitCSVfilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_OrbitSelector_OrbitCSVfilename,)
	WIDGET_OrbitSelector_OrbitNetCDFfilename = widgets.Label(value='  --> OrbitNetCDFfilename  ')
	WIDGET_OrbitSelector_OrbitNetCDFfilename.layout.border = '1px dashed green'
	WIDGET_OrbitSelector_OrbitNetCDFfilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_OrbitSelector_OrbitNetCDFfilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_OrbitSelector_OrbitNetCDFfilename,)
	IRI16_NetCDF_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'Selector'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	global WIDGET_Selector_MeshgridFilename
	WIDGET_Selector_MeshgridFilename = widgets.Text(value="")
	WIDGET_Selector_MeshgridFilename.description = 'MeshgridFilename'
	WIDGET_Selector_MeshgridFilename.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Selector_MeshgridFilename,)
	global WIDGET_Selector_MeshgridDatetime
	WIDGET_Selector_MeshgridDatetime = widgets.Text(value="Mar 17 2015 00:50:00.000000000")
	WIDGET_Selector_MeshgridDatetime.description = 'MeshgridDatetime'
	WIDGET_Selector_MeshgridDatetime.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Selector_MeshgridDatetime,)
	global WIDGET_Selector_MeshgridAltitude
	WIDGET_Selector_MeshgridAltitude = widgets.FloatText(value=120)
	WIDGET_Selector_MeshgridAltitude.description = 'MeshgridAltitude'
	WIDGET_Selector_MeshgridAltitude.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Selector_MeshgridAltitude,)
	global WIDGET_Selector_MeshgridLatitudeStep
	WIDGET_Selector_MeshgridLatitudeStep = widgets.FloatText(value=5)
	WIDGET_Selector_MeshgridLatitudeStep.description = 'MeshgridLatitudeStep'
	WIDGET_Selector_MeshgridLatitudeStep.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Selector_MeshgridLatitudeStep,)
	global WIDGET_Selector_MeshgridLongitudeStep
	WIDGET_Selector_MeshgridLongitudeStep = widgets.FloatText(value=5)
	WIDGET_Selector_MeshgridLongitudeStep.description = 'MeshgridLongitudeStep'
	WIDGET_Selector_MeshgridLongitudeStep.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Selector_MeshgridLongitudeStep,)
	global WIDGET_Selector_NoiseWx
	WIDGET_Selector_NoiseWx = widgets.FloatText(value=0)
	WIDGET_Selector_NoiseWx.description = 'NoiseWx'
	WIDGET_Selector_NoiseWx.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Selector_NoiseWx,)
	global WIDGET_Selector_NoiseWy
	WIDGET_Selector_NoiseWy = widgets.FloatText(value=0)
	WIDGET_Selector_NoiseWy.description = 'NoiseWy'
	WIDGET_Selector_NoiseWy.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Selector_NoiseWy,)
	global WIDGET_Selector_NoiseAx
	WIDGET_Selector_NoiseAx = widgets.FloatText(value=0)
	WIDGET_Selector_NoiseAx.description = 'NoiseAx'
	WIDGET_Selector_NoiseAx.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Selector_NoiseAx,)
	global WIDGET_Selector_NoiseAy
	WIDGET_Selector_NoiseAy = widgets.FloatText(value=0)
	WIDGET_Selector_NoiseAy.description = 'NoiseAy'
	WIDGET_Selector_NoiseAy.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Selector_NoiseAy,)
	global WIDGET_Selector_IRI16_variableForMeshgrid
	WIDGET_Selector_IRI16_variableForMeshgrid = widgets.Dropdown( options=['', 'Op', 'O2p', 'Te', 'Ti', 'Ne'], value='', description='Variable')
	WIDGET_Selector_IRI16_variableForMeshgrid.description = 'IRI16_variableForMeshgrid'
	WIDGET_Selector_IRI16_variableForMeshgrid.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Selector_IRI16_variableForMeshgrid,)
	global WIDGET_Selector_IRI16_variableForOrbit
	WIDGET_Selector_IRI16_variableForOrbit = widgets.Dropdown( options=['', 'Op', 'O2p', 'Te', 'Ti', 'Ne'], value='', description='Variable')
	WIDGET_Selector_IRI16_variableForOrbit.description = 'IRI16_variableForOrbit'
	WIDGET_Selector_IRI16_variableForOrbit.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_Selector_IRI16_variableForOrbit,)
	IRI16_NetCDF_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	Selector_Btn = widgets.Button (
		description='Selector',
		tooltip="Functions as a single point which collects all user input and distributes it to the various modules of this group",
	)
	Selector_Btn.layout.min_width = '200px'
	Selector_Btn.style.button_color = 'gold'
	IRI16_NetCDF_Panel.children += (Selector_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_Selector_MeshgridfilenameOUT = widgets.Label(value='  --> MeshgridfilenameOUT  ')
	WIDGET_Selector_MeshgridfilenameOUT.layout.border = '1px dashed green'
	WIDGET_Selector_MeshgridfilenameOUT.layout.margin ='0px 40px 0px 0px' 
	WIDGET_Selector_MeshgridfilenameOUT.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_Selector_MeshgridfilenameOUT,)
	WIDGET_Selector_MeshgridDatetimeOUT = widgets.Label(value='  --> MeshgridDatetimeOUT  ')
	WIDGET_Selector_MeshgridDatetimeOUT.layout.border = '1px dashed green'
	WIDGET_Selector_MeshgridDatetimeOUT.layout.margin ='0px 40px 0px 0px' 
	WIDGET_Selector_MeshgridDatetimeOUT.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_Selector_MeshgridDatetimeOUT,)
	WIDGET_Selector_MeshgridAltitudeOUT = widgets.Label(value='  --> MeshgridAltitudeOUT  ')
	WIDGET_Selector_MeshgridAltitudeOUT.layout.border = '1px dashed green'
	WIDGET_Selector_MeshgridAltitudeOUT.layout.margin ='0px 40px 0px 0px' 
	WIDGET_Selector_MeshgridAltitudeOUT.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_Selector_MeshgridAltitudeOUT,)
	WIDGET_Selector_MeshgridLatitudeStepOUT = widgets.Label(value='  --> MeshgridLatitudeStepOUT  ')
	WIDGET_Selector_MeshgridLatitudeStepOUT.layout.border = '1px dashed green'
	WIDGET_Selector_MeshgridLatitudeStepOUT.layout.margin ='0px 40px 0px 0px' 
	WIDGET_Selector_MeshgridLatitudeStepOUT.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_Selector_MeshgridLatitudeStepOUT,)
	WIDGET_Selector_MeshgridLongitudeStepOUT = widgets.Label(value='  --> MeshgridLongitudeStepOUT  ')
	WIDGET_Selector_MeshgridLongitudeStepOUT.layout.border = '1px dashed green'
	WIDGET_Selector_MeshgridLongitudeStepOUT.layout.margin ='0px 40px 0px 0px' 
	WIDGET_Selector_MeshgridLongitudeStepOUT.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_Selector_MeshgridLongitudeStepOUT,)
	WIDGET_Selector_NoiseWxOUT = widgets.Label(value='  --> NoiseWxOUT  ')
	WIDGET_Selector_NoiseWxOUT.layout.border = '1px dashed green'
	WIDGET_Selector_NoiseWxOUT.layout.margin ='0px 40px 0px 0px' 
	WIDGET_Selector_NoiseWxOUT.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_Selector_NoiseWxOUT,)
	WIDGET_Selector_NoiseWyOUT = widgets.Label(value='  --> NoiseWyOUT  ')
	WIDGET_Selector_NoiseWyOUT.layout.border = '1px dashed green'
	WIDGET_Selector_NoiseWyOUT.layout.margin ='0px 40px 0px 0px' 
	WIDGET_Selector_NoiseWyOUT.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_Selector_NoiseWyOUT,)
	WIDGET_Selector_NoiseAxOUT = widgets.Label(value='  --> NoiseAxOUT  ')
	WIDGET_Selector_NoiseAxOUT.layout.border = '1px dashed green'
	WIDGET_Selector_NoiseAxOUT.layout.margin ='0px 40px 0px 0px' 
	WIDGET_Selector_NoiseAxOUT.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_Selector_NoiseAxOUT,)
	WIDGET_Selector_NoiseAyOUT = widgets.Label(value='  --> NoiseAyOUT  ')
	WIDGET_Selector_NoiseAyOUT.layout.border = '1px dashed green'
	WIDGET_Selector_NoiseAyOUT.layout.margin ='0px 40px 0px 0px' 
	WIDGET_Selector_NoiseAyOUT.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_Selector_NoiseAyOUT,)
	WIDGET_Selector_IRI16_variableForMeshgrid_OUT = widgets.Label(value='  --> IRI16_variableForMeshgrid_OUT  ')
	WIDGET_Selector_IRI16_variableForMeshgrid_OUT.layout.border = '1px dashed green'
	WIDGET_Selector_IRI16_variableForMeshgrid_OUT.layout.margin ='0px 40px 0px 0px' 
	WIDGET_Selector_IRI16_variableForMeshgrid_OUT.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_Selector_IRI16_variableForMeshgrid_OUT,)
	WIDGET_Selector_IRI16_variableForOrbit_OUT = widgets.Label(value='  --> IRI16_variableForOrbit_OUT  ')
	WIDGET_Selector_IRI16_variableForOrbit_OUT.layout.border = '1px dashed green'
	WIDGET_Selector_IRI16_variableForOrbit_OUT.layout.margin ='0px 40px 0px 0px' 
	WIDGET_Selector_IRI16_variableForOrbit_OUT.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_Selector_IRI16_variableForOrbit_OUT,)
	IRI16_NetCDF_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'CreateNETCDFsphere'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_CreateNETCDFsphere_CDFfilename = widgets.Label(value='  Selector.MeshgridfilenameOUT --> CDFfilename  ')
	WIDGET_CreateNETCDFsphere_CDFfilename.layout.border = '1px dashed blue'
	WIDGET_CreateNETCDFsphere_CDFfilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_CreateNETCDFsphere_CDFfilename,)
	WIDGET_CreateNETCDFsphere_fixedDatetimeString = widgets.Label(value='  Selector.MeshgridDatetimeOUT --> fixedDatetimeString  ')
	WIDGET_CreateNETCDFsphere_fixedDatetimeString.layout.border = '1px dashed blue'
	WIDGET_CreateNETCDFsphere_fixedDatetimeString.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_CreateNETCDFsphere_fixedDatetimeString,)
	WIDGET_CreateNETCDFsphere_fixedAltitude = widgets.Label(value='  Selector.MeshgridAltitudeOUT --> fixedAltitude  ')
	WIDGET_CreateNETCDFsphere_fixedAltitude.layout.border = '1px dashed blue'
	WIDGET_CreateNETCDFsphere_fixedAltitude.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_CreateNETCDFsphere_fixedAltitude,)
	WIDGET_CreateNETCDFsphere_LatitudeStep = widgets.Label(value='  Selector.MeshgridLatitudeStepOUT --> LatitudeStep  ')
	WIDGET_CreateNETCDFsphere_LatitudeStep.layout.border = '1px dashed blue'
	WIDGET_CreateNETCDFsphere_LatitudeStep.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_CreateNETCDFsphere_LatitudeStep,)
	WIDGET_CreateNETCDFsphere_LongitudeStep = widgets.Label(value='  Selector.MeshgridLongitudeStepOUT --> LongitudeStep  ')
	WIDGET_CreateNETCDFsphere_LongitudeStep.layout.border = '1px dashed blue'
	WIDGET_CreateNETCDFsphere_LongitudeStep.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_CreateNETCDFsphere_LongitudeStep,)
	IRI16_NetCDF_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	CreateNETCDFsphere_Btn = widgets.Button (
		description='CreateNETCDFsphere',
		tooltip="Creates a CSV file with the format [Time, Lat, Lon, Alt]\nTime and Alt are fixed values given as arguments and Lat and Lon are produced for the whole globe accodring to steps specified.\nCSVfilename: string, the csv filename to be written (overwrite mode)\nfixedDatetimeString: string, the date-time fixed text with format as example: Mar 17 2015 00:12:00.000. Fixed value for every csv entry.\nfixedAltitude: float positive, kilometers above earth. Fixed value for every csv entry.\nLatitudeStep: float positive, Latiude values range between 87.5 and -88.5. The step is how Lat should be incremented at each iteration.\nLongitudeStep: float positive, Longitude values range between -180 and 180.  The step is how Lon should be incremented at each iteration.\nRETURNS: the filename it has written (same as the argument)\n         the altitude (same as the argument)\n         the number of lines written",
	)
	CreateNETCDFsphere_Btn.layout.min_width = '200px'
	CreateNETCDFsphere_Btn.style.button_color = 'gold'
	IRI16_NetCDF_Panel.children += (CreateNETCDFsphere_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_CreateNETCDFsphere_theFilename = widgets.Label(value='  --> theFilename  ')
	WIDGET_CreateNETCDFsphere_theFilename.layout.border = '1px dashed green'
	WIDGET_CreateNETCDFsphere_theFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_CreateNETCDFsphere_theFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_CreateNETCDFsphere_theFilename,)
	WIDGET_CreateNETCDFsphere_theAltitude = widgets.Label(value='  --> theAltitude  ')
	WIDGET_CreateNETCDFsphere_theAltitude.layout.border = '1px dashed green'
	WIDGET_CreateNETCDFsphere_theAltitude.layout.margin ='0px 40px 0px 0px' 
	WIDGET_CreateNETCDFsphere_theAltitude.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_CreateNETCDFsphere_theAltitude,)
	IRI16_NetCDF_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'IRI16'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_IRI16_Filename_forMeshgrid = widgets.Label(value='  CreateNETCDFsphere.theFilename --> Filename_forMeshgrid  ')
	WIDGET_IRI16_Filename_forMeshgrid.layout.border = '1px dashed blue'
	WIDGET_IRI16_Filename_forMeshgrid.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_IRI16_Filename_forMeshgrid,)
	WIDGET_IRI16_Variable_forMeshgrid = widgets.Label(value='  Selector.IRI16_variableForMeshgrid_OUT --> Variable_forMeshgrid  ')
	WIDGET_IRI16_Variable_forMeshgrid.layout.border = '1px dashed blue'
	WIDGET_IRI16_Variable_forMeshgrid.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_IRI16_Variable_forMeshgrid,)
	IRI16_NetCDF_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	IRI16_Btn = widgets.Button (
		description='IRI16',
		tooltip="International Reference Ionosphere empirical model (IRI)\nfilename: the CSV file to read. Format: Time,Alt,Lon,Lat. The file defines the coordinates for which the IRI calculation will take place.\nParameter: selects which values to calculate. Possible values are:\n    ''   for all\n    'Op'  for Oxygen+\n    'O2p' for Oxygen2+\n    'Te' for Electron Temperature\n    'Ti' for Ion Temperature\nReturns: the name of the CSV file which contains the calculated values. Format: Time,Alt,Lon,Lat,Op,O2p,Te,Ti",
	)
	IRI16_Btn.layout.min_width = '200px'
	IRI16_Btn.style.button_color = 'salmon'
	IRI16_NetCDF_Panel.children += (IRI16_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_IRI16_MeshgridResultFile = widgets.Label(value='  --> MeshgridResultFile  ')
	WIDGET_IRI16_MeshgridResultFile.layout.border = '1px dashed green'
	WIDGET_IRI16_MeshgridResultFile.layout.margin ='0px 40px 0px 0px' 
	WIDGET_IRI16_MeshgridResultFile.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_IRI16_MeshgridResultFile,)
	IRI16_NetCDF_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'IRI16'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_IRI16_OrbitFilename = widgets.Label(value='  OrbitSelector.OrbitFilename --> OrbitFilename  ')
	WIDGET_IRI16_OrbitFilename.layout.border = '1px dashed blue'
	WIDGET_IRI16_OrbitFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_IRI16_OrbitFilename,)
	WIDGET_IRI16_VariableOrbit = widgets.Label(value='  Selector.IRI16_variableForOrbit_OUT --> VariableOrbit  ')
	WIDGET_IRI16_VariableOrbit.layout.border = '1px dashed blue'
	WIDGET_IRI16_VariableOrbit.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_IRI16_VariableOrbit,)
	IRI16_NetCDF_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	IRI16_Btn = widgets.Button (
		description='IRI16',
		tooltip="International Reference Ionosphere empirical model (IRI)\nfilename: the CSV file to read. Format: Time,Alt,Lon,Lat. The file defines the coordinates for which the IRI calculation will take place.\nParameter: selects which values to calculate. Possible values are:\n    ''   for all\n    'Op'  for Oxygen+\n    'O2p' for Oxygen2+\n    'Te' for Electron Temperature\n    'Ti' for Ion Temperature\nReturns: the name of the CSV file which contains the calculated values. Format: Time,Alt,Lon,Lat,Op,O2p,Te,Ti",
	)
	IRI16_Btn.layout.min_width = '200px'
	IRI16_Btn.style.button_color = 'salmon'
	IRI16_NetCDF_Panel.children += (IRI16_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_IRI16_OrbitResultFilename = widgets.Label(value='  --> OrbitResultFilename  ')
	WIDGET_IRI16_OrbitResultFilename.layout.border = '1px dashed green'
	WIDGET_IRI16_OrbitResultFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_IRI16_OrbitResultFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_IRI16_OrbitResultFilename,)
	IRI16_NetCDF_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'SubGridVariability'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_SubGridVariability_NoiseWx = widgets.Label(value='  Selector.NoiseWxOUT --> NoiseWx  ')
	WIDGET_SubGridVariability_NoiseWx.layout.border = '1px dashed blue'
	WIDGET_SubGridVariability_NoiseWx.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_SubGridVariability_NoiseWx,)
	WIDGET_SubGridVariability_NoiseWy = widgets.Label(value='  Selector.NoiseWyOUT --> NoiseWy  ')
	WIDGET_SubGridVariability_NoiseWy.layout.border = '1px dashed blue'
	WIDGET_SubGridVariability_NoiseWy.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_SubGridVariability_NoiseWy,)
	WIDGET_SubGridVariability_NoiseAx = widgets.Label(value='  Selector.NoiseAxOUT --> NoiseAx  ')
	WIDGET_SubGridVariability_NoiseAx.layout.border = '1px dashed blue'
	WIDGET_SubGridVariability_NoiseAx.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_SubGridVariability_NoiseAx,)
	WIDGET_SubGridVariability_NoiseAy = widgets.Label(value='  Selector.NoiseAyOUT --> NoiseAy  ')
	WIDGET_SubGridVariability_NoiseAy.layout.border = '1px dashed blue'
	WIDGET_SubGridVariability_NoiseAy.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_SubGridVariability_NoiseAy,)
	WIDGET_SubGridVariability_filename = widgets.Label(value='  IRI16.OrbitResultFilename --> filename  ')
	WIDGET_SubGridVariability_filename.layout.border = '1px dashed blue'
	WIDGET_SubGridVariability_filename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_SubGridVariability_filename,)
	global WIDGET_SubGridVariability_ValueName
	WIDGET_SubGridVariability_ValueName = widgets.Text()
	WIDGET_SubGridVariability_ValueName.description = 'ValueName'
	WIDGET_SubGridVariability_ValueName.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_SubGridVariability_ValueName,)
	IRI16_NetCDF_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	SubGridVariability_Btn = widgets.Button (
		description='SubGridVariability',
		tooltip="Inputs\n NoiseAx,NoiseAy: real:: Amplitude of noise Kind (values 0-100)\n NoiseWx,NoiseWy: real:: Wavenumber of noise Kind (values 0-1000)\n Filename: Character:: field to read orbit from\n ValueName: Character:: variable from model data to use and add SGV. Corresponds to CSV Column\nOutputs\n Plots..\nReturns\n a csv filename of format Time, Lat, Lon, Alt, value containing the altered-with-noise values",
	)
	SubGridVariability_Btn.layout.min_width = '200px'
	SubGridVariability_Btn.style.button_color = 'gold'
	IRI16_NetCDF_Panel.children += (SubGridVariability_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	WIDGET_SubGridVariability_VariabilityFilename = widgets.Label(value='  --> VariabilityFilename  ')
	WIDGET_SubGridVariability_VariabilityFilename.layout.border = '1px dashed green'
	WIDGET_SubGridVariability_VariabilityFilename.layout.margin ='0px 40px 0px 0px' 
	WIDGET_SubGridVariability_VariabilityFilename.layout.padding ='0px 10px 0px 10px' 
	OutputsPanel.children += (WIDGET_SubGridVariability_VariabilityFilename,)
	IRI16_NetCDF_Panel.children += (OutputsPanel,)
	########
	## GUI code for module 'PlotGlobe'
	########
	# Create widgets for module's inputs
	InputsPanel = widgets.VBox()
	InputsPanel.layout.min_width = '330px'
	WIDGET_PlotGlobe_SurfaceFilename = widgets.Label(value='  IRI16.MeshgridResultFile --> SurfaceFilename  ')
	WIDGET_PlotGlobe_SurfaceFilename.layout.border = '1px dashed blue'
	WIDGET_PlotGlobe_SurfaceFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_PlotGlobe_SurfaceFilename,)
	global WIDGET_PlotGlobe_SurfaceVariableToPlot
	WIDGET_PlotGlobe_SurfaceVariableToPlot = widgets.Text(value='ALFA')
	WIDGET_PlotGlobe_SurfaceVariableToPlot.description = 'SurfaceVariableToPlot'
	WIDGET_PlotGlobe_SurfaceVariableToPlot.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_PlotGlobe_SurfaceVariableToPlot,)
	global WIDGET_PlotGlobe_SurfaceColorbarTitle
	WIDGET_PlotGlobe_SurfaceColorbarTitle = widgets.Text()
	WIDGET_PlotGlobe_SurfaceColorbarTitle.description = 'SurfaceColorbarTitle'
	WIDGET_PlotGlobe_SurfaceColorbarTitle.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_PlotGlobe_SurfaceColorbarTitle,)
	global WIDGET_PlotGlobe_SurfaceColorscaleName
	WIDGET_PlotGlobe_SurfaceColorscaleName = widgets.Dropdown( options=['', 'None', 'Blackbody', 'Bluered', 'Blues', 'Earth', 'Electric', 'Greens', 'Greys', 'Hot', 'Jet', 'Picnic', 'Portland', 'Rainbow', 'RdBu', 'Reds', 'Viridis', 'YlGnBu', 'YlOrRd'], value='Jet', description='Variable')
	WIDGET_PlotGlobe_SurfaceColorscaleName.description = 'SurfaceColorscaleName'
	WIDGET_PlotGlobe_SurfaceColorscaleName.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_PlotGlobe_SurfaceColorscaleName,)
	WIDGET_PlotGlobe_OrbitFilename = widgets.Label(value='  SubGridVariability.VariabilityFilename --> OrbitFilename  ')
	WIDGET_PlotGlobe_OrbitFilename.layout.border = '1px dashed blue'
	WIDGET_PlotGlobe_OrbitFilename.layout.padding = '0px 10px 0px 10px'
	InputsPanel.children += (WIDGET_PlotGlobe_OrbitFilename,)
	global WIDGET_PlotGlobe_OrbitVariableToPlot
	WIDGET_PlotGlobe_OrbitVariableToPlot = widgets.Text(value='ALFA')
	WIDGET_PlotGlobe_OrbitVariableToPlot.description = 'OrbitVariableToPlot'
	WIDGET_PlotGlobe_OrbitVariableToPlot.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_PlotGlobe_OrbitVariableToPlot,)
	global WIDGET_PlotGlobe_OrbitColorbarTitle
	WIDGET_PlotGlobe_OrbitColorbarTitle = widgets.Text()
	WIDGET_PlotGlobe_OrbitColorbarTitle.description = 'OrbitColorbarTitle'
	WIDGET_PlotGlobe_OrbitColorbarTitle.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_PlotGlobe_OrbitColorbarTitle,)
	global WIDGET_PlotGlobe_OrbitColorscaleName
	WIDGET_PlotGlobe_OrbitColorscaleName = widgets.Dropdown( options=['', 'None', 'Blackbody', 'Bluered', 'Blues', 'Earth', 'Electric', 'Greens', 'Greys', 'Hot', 'Jet', 'Picnic', 'Portland', 'Rainbow', 'RdBu', 'Reds', 'Viridis', 'YlGnBu', 'YlOrRd'], value='Jet', description='Variable')
	WIDGET_PlotGlobe_OrbitColorscaleName.description = 'OrbitColorscaleName'
	WIDGET_PlotGlobe_OrbitColorscaleName.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_PlotGlobe_OrbitColorscaleName,)
	global WIDGET_PlotGlobe_PlotTitle
	WIDGET_PlotGlobe_PlotTitle = widgets.Text()
	WIDGET_PlotGlobe_PlotTitle.description = 'PlotTitle'
	WIDGET_PlotGlobe_PlotTitle.layout.border = '1px dashed blue'
	InputsPanel.children += (WIDGET_PlotGlobe_PlotTitle,)
	IRI16_NetCDF_Panel.children += (InputsPanel,)
	# Create widget for the moudle black-box body
	PlotGlobe_Btn = widgets.Button (
		description='PlotGlobe',
		tooltip="Creates a 3D plot of an earth globe. Can plot a sphere surface and/or a satellite orbit. The surface and the orbit are colored according to the data values in the data files. Different colorscales can be selected for the surface and the orbit.\nThe data files can be of CSV o NetCDF4 format.\nValid Colorscale Names: ‘Blackbody’, ‘Bluered’, ‘Blues’, ‘Earth’, ‘Electric’, ‘Greens’, ‘Greys’, ‘Hot’, ‘Jet’, ‘Picnic’, ‘Portland’, ‘Rainbow’, ‘RdBu’, ‘Reds’, ‘Viridis’, ‘YlGnBu’, ‘YlOrRd’\nARGUMENTS:\n  SurfaceFilename: The file which contains data for a surface. If empty string then no surface will be plotted. \n                   CSV format: Time,Lat,Lon,Alt,value. Contains the data for the sphere surface. \n                   NetCDF format: see Daedalus User Manual\n  SurfaceVariableToPlot: The name of the variable to read from the surface data file and plot upon the globe.\n  SurfaceColorbarTitle: A title to display above the colorbar which refers to the surface data\n  SurfaceColorscaleName: The name of the Colorscale to use for the surface data. \n                         In case an empty string is passed then a default HeatMap colorscale will be applied.\n                         In case None is passed then all points will be black irrespective of value.\n  OrbitFilename: counterpart of the corresponding argument for the Surface data\n  OrbitVariableToPlot: counterpart of the corresponding argument for the Surface data \n  OrbitColorbarTitle: counterpart of the corresponding argument for the Surface data \n  OrbitColorscaleName: counterpart of the corresponding argument for the Surface data\n  PlotTitle: A title which is displayed on the top of the plot.\nRETURNS: a string containing information about the Data",
	)
	PlotGlobe_Btn.layout.min_width = '200px'
	PlotGlobe_Btn.style.button_color = 'deeppink'
	IRI16_NetCDF_Panel.children += (PlotGlobe_Btn,)
	# Create widgets for module's outputs
	OutputsPanel = widgets.VBox()
	OutputsPanel.layout.min_width = '300px'
	IRI16_NetCDF_Panel.children += (OutputsPanel,)
	return IRI16_NetCDF_Panel


