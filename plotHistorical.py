#!/usr/bin python3 -tt
# Character_encoding: UTF-8
# -------------------------------------------------------------
# Author: Dalwar Hossain (dalwar014@gmail.com)
# Python Interpreter: >= 3.4
# mySQL Database Version: 5.6.28
# mysql Connector Version: 2.1.5
# -------------------------------------------------------------
# Import Built-in Libraries
import pylab as plt
# -------------------------------------------------------------
# Define a function to plot data into a graph
def plotGraph(inputFile):
	# Open file to read data to plot
	with open(inputFile, 'r') as f:
		data = f.read()
	pltData = [row for row in data.split('\n') if row]
	# define empty list to hold the labels and values
	xLabels = []
	y = []
	index = [i for i in range(len(pltData))]
	for value in pltData:
		xDates, yValues = value.split('\t')
		xLabels.append(xDates)
		y.append(int(yValues))
	plt.bar(index, y, color='g')
	plt.xticks(index,xLabels, rotation=45, ha='center')
	plt.title('Historical data over time')
	plt.xlabel('Year - Date')
	plt.ylabel('Total number of prefix')
	plt.grid()
	plt.show()
def main():
	inputFile = '/home/dalwar/Study/NPA-Project/Data/plotting-Data/historical.txt'
	plotGraph(inputFile)
# -------------------------------------------------------------
# This is a standard boilerplate that calls the main() function
if __name__ == '__main__':
	main()
