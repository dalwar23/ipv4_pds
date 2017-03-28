#!/usr/bin python3 -tt
# Character_encoding: UTF-8
# -------------------------------------------------------------
# Author: Dalwar Hossain (dalwar014@gmail.com)
# Python Interpreter: >= 3.4
# mySQL Database Version: 5.6.28
# mysql Connector Version: 2.1.5
# -------------------------------------------------------------
# Import custom library functions
# Create a function to execute transfers of data
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
# Create a function to execute updates
def executeUpdate(connection, table2Update):
    # Transfer all the data to second primary table
    srcNdstList = ['v_delegation','t_delegation_p2']
    transferData(connection,srcNdstList)

    # Get all the data from the table and find out business raltionship
    
