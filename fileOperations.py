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
import gzip
# -------------------------------------------------------------
# Define a function to extract the files
def extractFiles(gzFileLocation,fList, csvFileLocation, trackerFileLocation):
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
# Define checkFiles() function to detemine whether file exists
# or not if so then return the names in a list
def checkFiles(gzFileLocation, csvFileLocation, trackerFileLocation):
	# List 'xxxxyyzz.gz' files
	if os.listdir(gzFileLocation):
		fList = os.listdir(gzFileLocation)
		# Check against gz-file tracker is there any new files
		try:
			gzTrackerFile = trackerFileLocation + 'gz-Tracker.txt'
			with open(gzTrackerFile,'r') as gzTracker:
				oldgzFiles = gzTracker.read().splitlines()
				#print ('{}'.format(oldgzFiles), end = '\n')
		except:
			print('gz data tracker file not found!', end = '\n')
		# Compare two lists of files to find out the newly added file
		gzFileSet = set(oldgzFiles)
		newgzFiles = [x for x in fList if x not in gzFileSet]
		if newgzFiles:
			extractFiles(gzFileLocation, newgzFiles, csvFileLocation, trackerFileLocation)
		else:
			print('No new gz data file detected!', end = '\n')
	else:
		print("Data directory [{}] is empty!".format(gzFileLocation), end = '\n')
# -------------------------------------------------------------
# This is a standard boilerplate that calls the main() function
if __name__ == '__main__':
	main()
