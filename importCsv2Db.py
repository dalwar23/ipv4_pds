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
import gc
# Import custom library functions
import primaryTableCleaner
import fileOperations
import tableOperations
# Define a function to execute import query
def executeImportQuery(connection,inputDirectory,inputFile):
	# Prepare a cursor object using cursor() method
	cursor = connection.cursor()
	# Create MYSQL database query string according to file name
	dbQuery = createImportQuery(inputDirectory,inputFile)
	# Execute SQL query using execute() method
	try:
		cursor.execute(dbQuery)
		print("[ {} ] file imported successfully".format(inputFile), end='\n')
	except ValueError as e:
		print("Import Error! [ {} ] - [{}]".format(inputFile, e), end='\n')
	# Commit data to DATABASE
	connection.commit()
	# Close Cursor
	cursor.close();
# Define a function to create SQL query
def createImportQuery(inputDirectory,inputFile):
	tableName = 't_delegation_p1'
	querySegment_1 = "LOAD DATA LOCAL INFILE '"
	querySegment_2 = inputDirectory + inputFile + "'"
	querySegment_3 = " INTO TABLE " + tableName
	querySegment_4 = """ FIELDS TERMINATED BY '|' """ # OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"' LINES TERMINATED BY '\\n' """
	# Now complete query by joining all the segments togather
	completeImportQuery = querySegment_1 + querySegment_2 + querySegment_3 + querySegment_4 #+ querySegment_5 + querySegment_6
	# return complete query
	return completeImportQuery
# Create a function that will insert the data to the database
def csvImport(dbConnection):
	# Create empty list that will store csv file names, and logs
	csvList = []
	csvLog = []
	inputDirectory = fileOperations.csvFileLocation
	for f in os.listdir(inputDirectory):
		if f.endswith('.csv'):
			csvList.append(f)
	# check and match csv files for new files
	inputFileList = fileOperations.csvCheck()
	if inputFileList:
		# Create list of tables for data transfer
		srcNdstList = [['v_historical', 't_historical_s1'],['t_delegation_p2', 't_delegation_s1'],['v_delegation_2', 't_current_delegation_s1']]
		cSrcNdstList = [['v_delegation_2', 't_current_delegation_s1']]
		table2Update = 't_delegation_p2'
		# Create query count
		currentQueryCount = 1
		totalQueryCount = len(inputFileList)
		print("\nImporting CSV files to DB.....\n", end='\n')
		# Call a function that will import CSV to database
		for fileName in inputFileList:
			# Clean the Primary Tables to insert data
			primaryTableCleaner.truncate(dbConnection, flag=1)
			# Print executing query message
			print("\n[ {} of {} ] -> ".format(currentQueryCount,totalQueryCount), end='')
			# Import csv file to primary table
			executeImportQuery(dbConnection, inputDirectory, fileName)
			# Transfer data from view to table
			if(fileName.endswith('01.csv')):
				# Transfer data to a second table and update it
				tableOperations.executeUpdate(table2Update)
				for item in srcNdstList:
					tableOperations.transferData(item)
			else:
				for item in cSrcNdstList:
					tableOperations.transferData(item)
			# Clean the Primary Tables to insert data
			primaryTableCleaner.truncate(dbConnection, flag=0)
			csvLog.append(fileName)
			currentQueryCount += 1
		# write the log file
		print("Writing csv log...", end = '\n')
		fileOperations.csvLogging(csvLog)
		gc.collect()
# -------------------------------------------------------------
# This is a standard boilerplate that calls the main() function
if __name__ == '__main__':
	main()
