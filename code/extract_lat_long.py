import pandas as pd
import re

Station = []
lat=[]
lon=[]
with open('./rehana_rf/rehana_RF.txt') as fd:

    # Iterate over the lines
	for line in fd:
        # Capture one-or-more characters of non-whitespace after the initial match
		match = re.search(r'LATITUDE : (\S+)', line)
		match1 = re.search(r'LONGITUDE : (\S+)', line)

        # Did we find a match?
		if match:
			weather = match.group(1)
			lat.append(weather)
			Station.append(line.split(None, 1)[0])
		if match1:
			temp=match1.group(1)
			lon.append(temp)
station_location=pd.DataFrame()
station_location['Station']=Station
station_location['lat']=lat
station_location['lon']=lon
station_location.to_csv('SPI_station.csv',index=False)
	
