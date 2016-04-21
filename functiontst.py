#contains the following:
#fullTitleList
#graphData
#graphFunction
#searchFunction
#refineSearch
#fullSearch

import os
import matplotlib.pyplot as plt
import xlrd
import csv

def fullTitleList(data_list):
	full_title_list=[]
	for i in range(len(data_list)):
		full_title_list.append(data_list[i][0][0].encode("ascii"))
	return full_title_list

def graphData(data_list, data_names2plot):
	#list containing full data with data name and values
	tmpdata=[]

	for name in data_names2plot:
		for i in xrange(0,len(data_list)-1):
			xtmpvar=[]
			ytmpvar=[]
			if data_list[i][0][0]==name:
				for j in range(len(data_list[i])):
					if data_list[i][j][0]=="Potential applied (V)":
						for n in range (len(data_list[i])):
							if data_list[i][n][0]=="WE(1).Potential (V)":
								print "potential"
								for x in data_list[i][n]:
									xtmpvar.append(x)
							elif data_list[i][n][0]=="WE(1).Current (A)":
								print "current"
								for y in data_list[i][n]:
									ytmpvar.append(y)
					elif j==len(data_list[i]):		
						for p in range (len(data_list[i])):
							if data_list[i][p][0]=="Time (s)":
								print "time"
								for x in data_list[i][p]:
									xtmpvar.append(x)
							elif data_list[i][p][0]=="WE(1).Current (A)":
								print "current"
								for y in data_list[i][p]:
									ytmpvar.append(y)
				if len(xtmpvar)==0 or len(ytmpvar)==0:
					print "error"
				tmpdata.append(xtmpvar)
				tmpdata.append(ytmpvar)			
	return tmpdata
	
def graphFunction(tmpdata, data_labels):
	#format data_list x1,y1,x2,y2,x3,y3...etc.
	new_data_list=[]
	#format data_name_list xname1,yname1,xname2 ...
	data_name_list=[]

	for i in xrange(0,len(tmpdata)):
		tmpname=[]
		newdata=[]
		for j in xrange(0,len(tmpdata[i])):
			if j==0:
				tmpname.append(str(tmpdata[i][j]).encode("ascii"))
			else:
				newdata.append(tmpdata[i][j])
		data_name_list.append(tmpname)
		new_data_list.append(newdata)	
	count=0
	labelcount=0
	while count<len(data_name_list):	
		plt.plot(new_data_list[count],new_data_list[count+1],label=data_labels[labelcount])
		count+=2
		labelcount+=1
	#converts unicode data_name_list to ascii
	[str(x) for x in data_name_list]	

	xaxis=str(data_name_list[0]).replace('[','').replace(']','')
	yaxis=str(data_name_list[1]).replace('[','').replace(']','')

	plt.xlabel(xaxis)
	plt.ylabel(yaxis)
	plt.title(yaxis+" vs "+xaxis)
	plt.legend()
	plt.legend(bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0.)
	plt.show()  #(block=False)
	plt.draw()

def searchFunction(search_list, search_term):
#given a string list, returns list of strings which contain search term
	new_list=[]
	for i in search_list: 
		if search_term in i:
			new_list.append(i)
	return new_list

def refineSearch(search_list,continue_search_input):
#loops through search
	while continue_search_input.upper()=="YES":
		search_term=raw_input("Enter refined search\n")
                search_list=searchFunction(search_list,search_term)
                print "revised search:\n"
                print search_list
                continue_search_input=raw_input("Continue refining search? Input 'yes' to continue. Otherwise any other key.\n")
	return search_list

def fullSearch(data_list):
#automates entire title search for doexcelgraph -from potentiostat data
	data_names=[]
	userinput_addmore=raw_input("add graph data? input 'yes' to continue. Or any other key to stop.\n")
	while userinput_addmore.upper()=="YES":	
		print "Here are the data titles within the excel file\n"
        	search_list=fullTitleList(data_list)
        	print search_list 
		search_term=raw_input("\n Input your first search term for graphing:\n")
        	newtitlelist=searchFunction(search_list, search_term)
       	 	print "new title list:\n"
		print newtitlelist
		refineinput=raw_input("Refine search? 'yes' or any other key for no.\n")	
		if refineinput.upper()=="YES":
			newtitlelist=refineSearch(newtitlelist,"YES")	
		print newtitlelist
		saveinput=raw_input("Save the current data names? 'yes' or any other key for no\n")
		if saveinput.upper()=="YES":
			for i in newtitlelist:
				data_names.append(i)
		userinput_addmore=raw_input("add graph data? input 'yes' to continue. Or any other key to stop.\n")

	return data_names	

def directoryList(search_criteria):
#returns list of closed files in current directory that meet search criteria
	file_list=[]
	for fn in os.listdir('.'):
       	 	if search_criteria in fn and not "~" in fn:
                	file_list.append(fn)
	return file_list

