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
from os.path import expanduser
import gzip
# -------------------------------------------------------------
# Define some variables for file operations
# Get the home directory
fullPath = os.path.abspath(__file__)
baseDir, fileName = os.path.split(fullPath)

# Get home directory
homeDir = expanduser('~')

# Define Directory separator
commonDir = "/data/"
trackerDir = "tracker-data/"
#dataDir = "gz-data/" # uncomment this line if .gz data is taken from data/gz-data directory
dataDir = "/out/delegations/"
csvDir = "csv-data/"
plotDir = "plotting-data/"

# Introduce the raw data file location
#gzFileLocation =  baseDir + commonDir + dataDir
gzFileLocation =  homeDir + dataDir
csvFileLocation = baseDir + commonDir + csvDir
trackerFileLocation = baseDir + commonDir + trackerDir

# Define a function to extract the files
def extractgzFiles(fList):
	gzTrackerFile = trackerFileLocation + 'gz-Tracker.txt'
	for f in fList:
		filePath = gzFileLocation + f
		if os.path.isfile(filePath) and os.path.exists(filePath):
			try:
				print('Reading - [{}]'.format(f), end = '\n')
				with gzip.open(filePath,'rb') as gzFile:
					data = gzFile.read()
			except:
				print('Can not open [{}] file for reading!'.format(f), end = '\n')
			try:
				fileName, extention = f.split('.')
				nFile = fileName+'.csv'
				nFilePath = csvFileLocation + nFile
				print('Creating - [{}]'.format(nFile), end = '\n')
				with open(nFilePath,'wb') as csvFile:
					csvFile.write(data)
					with open(gzTrackerFile, 'a+') as gzTracker:
						gzTracker.write(f+'\n')
						print('Writing log - [{}]'.format(f), end = '\n')
			except:
				print('Can not write data into [{}] file!'.format(nFile), end = '\n')
			print('------------------------', end = '\n')
		else:
			pass
# Define checkgzFiles() function to detemine whether new file exists
# or not if so then return the names in a list
def checkgzFiles():
	# List 'xxxxyyzz.gz' files
	if os.listdir(gzFileLocation):
		fList = [f for f in os.listdir(gzFileLocation) if f.endswith('.gz')]
		# Check against gz-file tracker is there any new files
		try:
			gzTrackerFile = trackerFileLocation + 'gz-Tracker.txt'
			with open(gzTrackerFile,'r') as gzTracker:
				oldgzFiles = gzTracker.read().splitlines()
		except:
			print('gz data tracker file not found!', end = '\n')
		# Compare two lists of files to find out the newly added file
		gzFileSet = set(oldgzFiles)
		newgzFiles = [x for x in fList if x not in gzFileSet]
		if newgzFiles:
			extractgzFiles(newgzFiles)
		else:
			print('No new gz data file detected!', end = '\n')
	else:
		print("Data directory [{}] is empty!".format(gzFileLocation), end = '\n')
# Define csvCheck() function to detemine whether new file exists
# or not if so then return the names in a list
def csvCheck():
	# Check for new csv file and return a list of new csv files
	if os.listdir(csvFileLocation):
		fList = [f for f in os.listdir(csvFileLocation) if f.endswith('.csv')]
		# Check against gz-file tracker is there any new files
		try:
			csvTrackerFile = trackerFileLocation + 'csv-Tracker.txt'
			with open(csvTrackerFile,'r') as csvTracker:
				oldcsvFiles = csvTracker.read().splitlines()
		except:
			print('csv data tracker file not found!', end = '\n')
		# Compare two lists of files to find out the newly added file
		csvFileSet = set(oldcsvFiles)
		csvList = [x for x in fList if x not in csvFileSet]
		if csvList:
			return csvList
		else:
			print('\nNo new csv data file detected!', end = '\n')
	else:
		print("Data directory [{}] is empty!".format(csvFileLocation), end = '\n')
# define csvLogging() to log csv input to database
def csvLogging(csvList):
	# write the log file
	for f in csvList:
		try:
			csvTrackerFile = trackerFileLocation + 'csv-Tracker.txt'
			with open (csvTrackerFile, 'a+') as csvTracker:
				csvTracker.write(f+'\n')
		except:
			print('can\'t write csv log in csv tracker file!', end = '\n')
# -------------------------------------------------------------
# This is a standard boilerplate that calls the main() function
if __name__ == '__main__':
	main()
