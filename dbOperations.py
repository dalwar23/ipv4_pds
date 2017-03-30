#!/usr/bin python3 -tt
# Character_encoding: UTF-8
# -------------------------------------------------------------
# Author: Dalwar Hossain (dalwar014@gmail.com)
# Python Interpreter: >= 3.4
# mySQL Database Version: 5.6.28
# mysql Connector Version: 2.1.5
# -------------------------------------------------------------
# import library
import gc
# Import custom library functions
import importCsv2Db
import dbConnection
# Create a function to execute the threads
def executeThreads():
	# Create connection to Database
	print("\nConnecting to Databse.....", end = '\n')
	cnx = dbConnection.connect()
	if cnx:
		# Insert data from file to database
		importCsv2Db.csvImport(cnx)
	else:
		print("Connection failed!", end = '\n')
	gc.collect()
# -------------------------------------------------------------
# This is a standard boilerplate that calls the main() function
if __name__ == '__main__':
	main()
