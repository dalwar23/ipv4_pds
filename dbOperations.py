#!/usr/bin python3 -tt
# Character_encoding: UTF-8
# -------------------------------------------------------------
# Author: Dalwar Hossain (dalwar014@gmail.com)
# Python Interpreter: >= 3.4
# mySQL Database Version: 5.6.28
# mysql Connector Version: 2.1.5
# -------------------------------------------------------------
# Import custom library functions
import primaryTableCleaner
import importCsv2Db
# Create a function to execute the threads
def executeThreads(dbConnection):
	# Clean the Primary Tables to insert data
	primaryTableCleaner.truncate(dbConnection)
	# Insert data from file to database
	importCsv2Db.csvImport(dbConnection)
# -------------------------------------------------------------
# This is a standard boilerplate that calls the main() function
if __name__ == '__main__':
	main()
