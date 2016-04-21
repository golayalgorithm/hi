#Program is user interface for automating the graphing of excel files. 
#If excel sheet has multiple sheets, program will look through all sheets to compile relevant data

import sys, os
#sys.path.append('/Users/ewburns/Documents/Imperial/CV')
import xlrd
import functiontst #eric's functions for this program.  

data_list=[]
newtitlelist=[]

#>>>>>>>>>>>>>>>>>>>>>>>>INITIALIZING<<<<<<<<<<<<<<<<<<<<<<<<<<<<

file_list=functiontst.directoryList("xlsx")
for file in file_list:
	workbook=xlrd.open_workbook(file)
	sheet_list=[]
	for i in range (workbook.nsheets):
		current_sheet=workbook.sheet_by_index(i)
		sheet_list.append(current_sheet)
	for j in range(len(sheet_list)): 
		sheet_data=[]
		for x in range(sheet_list[j].ncols):
			col=[]
			for y in range(sheet_list[j].nrows):
				col.append(sheet_list[j].cell(y,x).value)
			sheet_data.append(col)
		data_list.append(sheet_data)

#>>>>>>>>>>>>>>>>>>>>>>>>END INITIALIZE<<<<<<<<<<<<<<<<<<<<<<<<<<

#>>>>>>>USER INTERPHASE<<<<<<<	

main_user_input=raw_input("This is an automated graphing program for 060 electrostat data in an excel format. If you want to end this program type 'end' otherwise press any key.\n")


while main_user_input.upper()!="END":
	
	data_names=functiontst.fullSearch(data_list)
	print "So you want to plot these datasets?\n"
	print data_names

	input=raw_input("Input 'yes' to continue or any other key to stop\n")
	if input.upper()=="YES":
		data_labels=[]
		print "what are the data labels you want?"
		for name in data_names:
			data_labels.append(raw_input("for "+name+"?\n"))
		functiontst.graphFunction(functiontst.graphData(data_list,data_names),data_labels)
	main_user_input=raw_input("Next iteration? If you no longer want to use this program type 'end' otherwise, press any key.\n")
