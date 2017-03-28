#!/usr/bin python3 -tt
# Character_encoding: UTF-8
# -------------------------------------------------------------
# Author: Dalwar Hossain (dalwar014@gmail.com)
# Python Interpreter: >= 3.4
# mySQL Database Version: 5.6.28
# mysql Connector Version: 2.1.5
# -------------------------------------------------------------
# Define a function that cleans all the primary tables
def tblClnr(connection,tableName):
	# Create a cursor to execute the DB query
	cursor = connection.cursor()
	# Create MYSQL database query string according to file name
	dbQuery = createQuery(tableName)
	# Execute SQL query using execute() method
	try:
		cursor.execute(dbQuery)
		print('[ {} ] table truncated successfully'.format(tableName), end='\n')
	except:
		print('[ {} ] table truncate ERROR!'.format(tableName),end='\n')
	# Commit data to DATABASE
	connection.commit()
	# Close Cursor
	cursor.close();
# Define a function create Query to truncate tables
def createQuery(tableName):
	querySegment_1 = "TRUNCATE TABLE "
	querySegment_2 = tableName
	completeQuery = querySegment_1 + querySegment_2
	return completeQuery
def truncate(dbConnection, flag):
	# Prep database to import files
	print("\nTruncating Table(s).....\n", end='\n')
	# Truncate tables based on flag's value
	if(flag==1):
		primaryTableList = ['t_delegation_p1', 't_current_delegation_s1']
	else:
		primaryTableList = ['t_delegation_p1']
	currentQuery = 1
	totalQuery = len(primaryTableList)
	# Now loop through the names and truncate the tables
	for tableName in primaryTableList:
		# Print executing query message
		print("[ {} of {} ] -> ".format(currentQuery,totalQuery),end='')
		# Call a function that will clean all selected tables
		tblClnr(dbConnection,tableName)
		currentQuery += 1
	print ("\nAll listed table(s) truncated", end='\n')
# -------------------------------------------------------------
# This is a standard boilerplate that calls the main() function
if __name__ == '__main__':
	main()
