#!/usr/bin python3 -tt
# Character_encoding: UTF-8
# -------------------------------------------------------------
# Author: Dalwar Hossain (dalwar014@gmail.com)
# Python Interpreter: >= 3.4
# mySQL Database Version: 5.6.28
# mysql Connector Version: 2.1.5
# -------------------------------------------------------------
# Import Built-in Libraries
import os
from datetime import datetime, date, time, timedelta
import time
import gc
# Import custom library fucntions
import fileOperations
import dbConnection
import dbOperations
# ---------------------------------------------------------------
# This function is the main function - that calls other necessary
# fucntions to check and extract data
def main():
    # Start the program execution clock
	program_start_time = time.time()
	human_readable_time = time.strftime("%H:%M:%S", time.localtime(program_start_time))
	print("\nProgram clock started at -> [ {} ]".format(str(human_readable_time)),end='\n')
	
	# Print an initialization message
	print("\nInitializing program.....\n",end='\n')
	
	# Get the home directory
	baseDir = os.environ['HOME']
	
	# Define Directory separator
	commonDir = "/Study/NPA-Project/data/"
	trackerDir = "tracker-data/"
	dataDir = "gz-data/"
	csvDir = "csv-data/"
	plotDir = "plotting-data/"
	
	# Introduce the raw data file location
	gzFileLocation =  baseDir + commonDir + dataDir
	csvFileLocation = baseDir + commonDir + csvDir
	trackerFileLocation = baseDir + commonDir + trackerDir
	
	# Check the source directory for "xxxxyyzz.gz" files
	# Extracts the .gz files into .csv
	extract = fileOperations.checkFiles(gzFileLocation, csvFileLocation, trackerFileLocation)
	
	# Create connection to Database
	print("\nConnecting to Databse.....", end = '\n')
	connectionString = dbConnection.connect()
	if connectionString:
		# DB connection established
		# Bulk insert csv files from csv file list
		# Call executeThreads() to execute necessary threads
		dbOperations.executeThreads(connectionString,csvFileLocation)
	else:
		print("Connection failed!", end = '\n')
	gc.collect()
	# Print program execution time message
	program_elapsed_sec = (time.time() - program_start_time)
	#program_elapsed_min = round((program_elapsed_sec / 60),2)
	print('\nProgram executed in [ {} ] second(s).'.format(program_elapsed_sec), end='\n')

	# Print exit message
	print('\nExiting.....','Bye!', sep='\n', end='\n')
# -------------------------------------------------------------
# This is a standard boilerplate that calls the main() function
if __name__ == '__main__':
	main()
