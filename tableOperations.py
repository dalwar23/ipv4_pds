#!/usr/bin python3 -tt
# Character_encoding: UTF-8
# -------------------------------------------------------------
# Author: Dalwar Hossain (dalwar014@gmail.com)
# Python Interpreter: >= 3.4
# mySQL Database Version: 5.6.28
# mysql Connector Version: 2.1.5
# -------------------------------------------------------------
# Import custom library functions
import dbConnection
import progressBar
# Create a function to update delegation table
def updateDelegationTable(bRelationList, table2Update):
	# Create DB connection
	cnx = dbConnection.connect()
	# Create a cursor
	cursor = cnx.cursor()
	# Progressbar length and iteration value
	l = len(bRelationList)
	i = 0
	# Create query to update table
	for item in bRelationList:
		updateQuery = createUpdateQuery(item, table2Update)
		#print('{}'.format(updateQuery), end='\n')
		try:
			# Execute cursor
			cursor.execute(updateQuery)
		except Exception as err:
			print('Can not update primary table with bsuiness relation info. ERROR - {}'.format(err))
		# Increase progressbar iterator and show progress bar
		i += 1
		progressBar.printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete')
	# Commit data to DATABASE
	cnx.commit()
	# Close Cursor
	cursor.close()
# define createUpdateQuery(item)
def createUpdateQuery(item, table2Update):
	# Create update query
	querySegment_1 = "UPDATE "
	querySegment_2 = table2Update
	querySegment_3 = " SET as_rel = '"
	querySegment_4 = str(item[2])
	querySegment_5 = "' WHERE delegator = "
	querySegment_6 = str(item[0])
	querySegment_7 = " AND delegatee = "
	querySegment_8 = str(item[1])
	completeUpdateQuery = querySegment_1 + querySegment_2 + querySegment_3 + querySegment_4 + querySegment_5 + querySegment_6 + querySegment_7 + querySegment_8
	return completeUpdateQuery
# Create a function to retrive business relations
def getBusinessRel(delegationList):
	# Create DB connection
	cnx = dbConnection.connect()
	# Create a cursor
	cursor = cnx.cursor()
	# Create a list with business relation data
	bRelationList = []
	# Progressbar length/iteration value
	l = len(delegationList)
	i = 0
	#progressBar.printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
	# Create a query for business raltionship
	for item in delegationList:
		tmpList = []
		bRelQuery = createBRelQuery(item[0], item[1])
		try:
			# execute the query
			cursor.execute(bRelQuery)
			rows = cursor.fetchmany(size=1)
			if rows:
				for row in rows:
					as_rel_type = row[0]
					tmpList.append(item[0])
					tmpList.append(item[1])
					tmpList.append(as_rel_type)
			else:
				tmpList.append(item[0])
				tmpList.append(item[1])
				tmpList.append('undefined')
			bRelationList.append(tmpList)
		except Exception as err:
			print('Cursor problem occured while retiving business ralation info. ERROR - {}'.format(err))
		# increase the progressbar iterator and show updated progressbar
		i +=1
		progressBar.printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete')
	return bRelationList
	# Commit data to DATABASE
	cnx.commit()
	# Close Cursor
	cursor.close()
# Create a function to search for business relations
def getDelegationdata(table2Update):
	# Create DB connection
	cnx = dbConnection.connect()
	# Create a cursor for repeated query execution
	cursor = cnx.cursor()
	# Create a query to get deleation info
	delegationQuery = createDelegationQuery(table2Update)
	try:
		# Execute SQL query
		cursor.execute(delegationQuery)
		delegationList = []
		for row in cursor:
			tmpList = []
			delegator = row[0]
			delegatee = row[1]
			tmpList.append(delegator)
			tmpList.append(delegatee)
			if tmpList and tmpList not in delegationList:
				delegationList.append(tmpList)
	except:
		# Print error message
		print("Data update ERROR! on table -> [ {} ]".format(table2Update), end='\n')
	return delegationList
	# Commit data to DATABASE
	cnx.commit()
	# Close Cursor
	cursor.close()
# Define function createDelegationQuery(delegationTable)
def createDelegationQuery(delegationTable):
	# Create query
	querySegment_1 = "SELECT delegator, delegatee FROM "
	querySegment_2 = delegationTable
	querySegment_3 = " GROUP BY delegator, delegatee"
	completeDelegationQuery = querySegment_1 + querySegment_2 + querySegment_3
	return completeDelegationQuery
# Define function to create b_relQuery
def createBRelQuery(delegator, delegatee):
	# Create query
	querySegment_1 = "SELECT as_rel_type FROM t_business_rel_s1 "
	querySegment_2 = "WHERE as_1 = "
	querySegment_3 = str(delegator)
	querySegment_4 = " AND "
	querySegment_5 = "as_2 = "
	querySegment_6 = str(delegatee)

	completeBRelQuery = querySegment_1 + querySegment_2 + querySegment_3 + querySegment_4 + querySegment_5 + querySegment_6
	return completeBRelQuery

# Create a function to execute transfers of data
def transferData(item):
	# create the DB connection
	cnx = dbConnection.connect()
	# Prepare a cursor object using cursor() method
	cursor = cnx.cursor()
	# Create MYSQL database query string according to item
	dataTransferQuery = createTransferQuery(item)
	try:
		# Execute SQL query using execute() method
		cursor.execute(dataTransferQuery)
		print("[ {} ] -> [ {} ] -> OK".format(item[0],item[1]), end='\n')
	except Exception as err :
		# Print Error message
		print("Data transfer Error!{} from [ {} ] on table -> [ {} ]".format(err, item[0],item[1]), end='\n')
	# Commit data to DATABASE
	cnx.commit()
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
	completeTransferQuery = querySegment_1 + querySegment_2 + querySegment_3 + querySegment_4
	#print(completeQuery, end='\n')
	return completeTransferQuery
# Create a function to execute updates
def executeUpdate(table2Update):
	# Transfer all the data to second primary table
	srcNdstList = ['v_delegation','t_delegation_p2']
	transferData(srcNdstList)
	print("\nGetting delegation info for business relations.....", end='\n')
	# Get all the data from the table and find out business raltionship
	delegationList = getDelegationdata(table2Update)
	print("\nGenerating for business relation info.....\n", end='\n')
	# Get business relations
	bRelationList = getBusinessRel(delegationList)
	print("\nUpdating business relation info.....\n", end='\n')
	# update table with business relations
	updateDelegationTable(bRelationList, table2Update)
# -------------------------------------------------------------
# This is a standard boilerplate that calls the main() function
if __name__ == '__main__':
	main()
