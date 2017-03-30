#!/usr/bin python3 -tt
# Character_encoding: UTF-8
# -------------------------------------------------------------
# Author: Dalwar Hossain (dalwar014@gmail.com)
# Python Interpreter: >= 3.4
# mySQL Database Version: 5.6.28
# mysql Connector Version: 2.1.5
# -------------------------------------------------------------
# Import addin Libraries
import mysql.connector as pymysql
#import pymysql
# -------------------------------------------------------------
# Define a connect() function
def connect():
	# Database Login Credentials
	dbHost = 'localhost' # Change (localhost to <ip address> if necessary)
	port = 3306	# Please don't change port value unless your server dictates
	userName = 'root' # Use database user name here
	passWord = 'inetnpa' # use  database password here
	databaseName = 'bgp_data' # use database name here

	# try to connect to database
	try:
		connection = pymysql.connect(user = userName, password = passWord, host = dbHost, database = databaseName)
	except:
		connection = False

	# Connection message
	if connection:
		# print("Connected to [ {}:{} -> {} ] database".format(dbHost,port,databaseName), end='\n')
		return connection
	else:
		print("Unable to connect to [ {}:{} -> {} ] database".format(dbHost,port,databaseName), end='\n')
# --------------------------------------------------------------
# This is a standard boilerplate that calls the main() function
if __name__ == '__main__':
	main()
