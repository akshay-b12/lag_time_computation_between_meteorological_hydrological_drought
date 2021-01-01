The entire project is organized into following folders:

1. dataset: Contains entire data files related to precipitaiton and runoff of Krishna River basin. Contains following folders and files:
	- Discharge: Discharge csv files of all the stations
	- precipitation.txt: Contains precipitation data
	- Discharge loctions Krishna Basin.csv : Latitude and longitudes of all those discharge stations whose data is availabe in Discharge folder.
	- SPI_stations: Latitude and longitudes of all the stations whose precipitation data is present in precipitation.txt file.
	
2. cluster-3: A sample data of a cluster taken from the available dataset and used for demonstration of the implemented work. Contains following files:

	- csv files of the precipitation data for the locations selected, to form a cluster based on their closeness to the discharge station. Extracted from ./dataset/precipitation.txt using the code in ./code/convert_tocsv.py. Copy the data of the required station from precipitation.txt into a station_name.txt file. Then give this station_name.txt file in t convert_tocsv code. THe output file will be station_name.csv.
	
	- SPI and SRI pooling data and summary files generated from R code which are saved as _pool.csv and _summary.csv. These are then read by the code in jupyter notebook.
	
	- The final result fiile drought_events_pairs.csv which is written by the jupyter notebook and stores the lag time between pair of meteorological and hydrological drought events.
	
3. Code: Contains all project code implemented in python and R. Contains following code files:

	- convert_to_csv.py: Converts a variable length space separated file to csv. This is used to convert the precipitation data, manually extracted into text file, to csv file. It takes two command line arguments, an input and output text file and the csv file will be generated. Copy the precipitation data (only numbers) from precipitation.txt into a text file and run the code by providing the input and output file names as arguments.
	
	- extract_lat_long.py: Reads the precipitation.txt file and extracts latitudes and longitudes of all locations present in the file.
	Libraries required: Pandas and re
	
	- spi_class.py: Defines a class to compute the drought indices SPI and SRI. It's object is used in the main code present in lag_time.ipynb to compute SPI and SRI.
	Libraries required: Pandas, scipy version=1.1.0 (important), numpy, types, datetime
	
	- data_analysis.ipynb: This notebook shows some of the data analysis performed pn the discharge data. It reads the discharge data fiile of a particular station and shows its analysis.
	
	- lag_time.ipynb: This notebook contains the entire implementation of lag time calculation. It reads files related to precipitation data generated using convert_tocsv.py from the cluster-3 folder. It reads the discharge data of teh required station from the dataset/Discharge folder. It also reads pooling and summary data files generated from the R code from dataset/Discharge folder.
	Libraries required: Pandas, scipy version=1.1.0 (important), numpy, types, datetime
	
	- pooling.rmd: This R noteboook computes meterological and hydrological drought events using SPi and SRI values and performs pooling of these drought events. It reads ../cluster-3/spi_cluster-3.csv and ../cluster-3/sri_cluster-3.csv generated from lag_time.ipynb. Then computes drought events and performs pooling. The output of pooling is saved as spi_pool.csv, sri_pool.csv  and spi_summary.csv and sri_pool.csv. These files are then used by python code in lag_time.ipynb to compute final lag times betwenn meterological and hydrological droughts.
	Libraries required: lfstat, xts, For plotting lat, long- tidyverse, ggmap
	
4. reports: This folder contains following report files:
	- data_analysis.pdf: Pdf version of data_analysis.ipynb notebook.
	- lag_time.pdf: Pdf version of lag_time.ipynb notebook.
	- report.pdf: This is the final project report which contains the theoretical background of all the concepts used in the project and the references. Also the zipped latex file corresponding to this report is present in the folder which can be uploaded to overleaf.com and can be edited.
	
5. references: Contans all the pdf files of references used during the project and that are mentioned in the final report.
