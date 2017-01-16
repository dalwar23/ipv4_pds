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
# Define a function to execute import query
def executeQuery(connection,inputDirectory,inputFile):
	# Prepare a cursor object using cursor() method
	cursor = connection.cursor()
	# Create MYSQL database query string according to file name
	dbQuery = createQuery(inputDirectory,inputFile)
	fileName, extension = inputFile.split('.')
	insertTimestampQuery = 'INSERT INTO bgp_timestamp_primary (file_date) VALUES (' + fileName +')'
	# Execute SQL query using execute() method
	try:
		cursor.execute(insertTimestampQuery)
		cursor.execute(dbQuery)
		print("[ {} ] file imported successfully".format(inputFile), end='\n')
	except ValueError as e:
		print("Import Error! [ {} ] - [{}]".format(inputFile, e), end='\n')
	# Commit data to DATABASE
	connection.commit()
	# Close Cursor
	cursor.close();
# Define a function to create SQL query
def createQuery(inputDirectory,inputFile):
	tableName = 'bgp_data_primary'
	querySegment_1 = "LOAD DATA LOCAL INFILE '"
	querySegment_2 = inputDirectory + inputFile + "'"
	querySegment_3 = " INTO TABLE " + tableName
	querySegment_4 = """ FIELDS TERMINATED BY '|' """ # OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"' LINES TERMINATED BY '\\n' """
	# Now complete query by joining all the segments togather
	completeQuery = querySegment_1 + querySegment_2 + querySegment_3 + querySegment_4 #+ querySegment_5 + querySegment_6
	# return complete query
	return completeQuery
# Create a function to transfer data from views to a table
def transferData(connection, item):
	# Prepare a cursor object using cursor() method
	cursor = connection.cursor()
	# Create MYSQL database query string according to item
	dataTransferQuery = createTransferQuery(item)
	try:
		# Execute SQL query using execute() method
		cursor.execute(dataTransferQuery)
		print("[ {} ] -> [ {} ] -> OK".format(item[0],item[1]), end='\n')
	except:
		# Print Error message
		print("Data transfer Error! on table -> [ {} ]".format(item[1]), end='\n')
	# Commit data to DATABASE
	connection.commit()
	# Close Cursor
	cursor.close()
# Define a function createTransferQuery(item)
def createTransferQuery(item):
	viewName = item[0]
	tableName = item[1]
	querySegment_1 = "INSERT IGNORE INTO "
	querySegment_2 = tableName
	querySegment_3 = " SELECT * FROM "
	querySegment_4 = viewName
	completeQuery = querySegment_1 + querySegment_2 + querySegment_3 + querySegment_4
	#print(completeQuery, end='\n')
	return completeQuery	
# Create a function that will insert the data to the database
def csvImport(dbConnection,inputDirectory):
	# Create an empty list that will store csv file names
	inputFileList = []
	for file in os.listdir(inputDirectory):
		if file.endswith('.csv'):
			inputFileList.append(file)
	# Get the list of the csv and insert
	scrcNdstList = [['view_historical_data', 'historical_data'],['view_bgp_data', 'bgp_data']]
	currentQueryCount = 1
	totalQueryCount = len(inputFileList)
	print("\nImporting CSV files to DB.....\n", end='\n')
	# Call a function that will import CSV to database
	for fileName in inputFileList:
		# Print executing query message
		print("[ {} of {} ] -> ".format(currentQueryCount,totalQueryCount), end='')
		executeQuery(dbConnection,inputDirectory,fileName)
		# Transfer data from view to table
		for item in scrcNdstList:
			transferData(dbConnection,item)
		# Clean the Primary Tables to insert data
		primaryTableCleaner.truncate(dbConnection)
		currentQueryCount += 1
	gc.collect()
# -------------------------------------------------------------
# This is a standard boilerplate that calls the main() function
if __name__ == '__main__':
	main()
