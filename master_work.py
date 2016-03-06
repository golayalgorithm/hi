#master_searchterm.py searches the master.csv file for matching terms in the data titles at the user requests.
#returns the datacolumns at which terms match user input term

import matplotlib.pyplot as plt
import xlrd
import csv

input_phrase=raw_input("input search phrase to search in master data file ...will return csv of data as [input].txt and titles of data as [input]_titles.txt\n")
input_phrase2="_"+raw_input("input t for transmission a for absorption")
input_phrase3=raw_input("input any other identifiers here or forever be silent.")
input2=""

if input_phrase2=="_t":
	input2="% Transmission"
elif input_phrase2=="_a":
	input2="Absorption"
else:
	print "error. input not in selection.  graphing all"
	input_phrase2=""
input_phrase5="su8"
input_phrase4="n"   #raw_input("any not qualifiers? (y/n)")
if input_phrase4=="y":
	input_phrase5=raw_input("enter your not qualifier")	

def masterList():
	master_list=[]
	#reads master.csv file and splits at each comma and ends into "master_list" list.
	file_reader=csv.reader(open('master.csv','rb'),delimiter=',')
	for i in file_reader:
		master_list.append(i)
	return master_list

def newTitleList(master_list,input_phrase):
	new_title_list=[]
	count=0
	
	#master_list[0] is the full title list
	for j in master_list[0]:
		#need to include wavelengths of different lengths and ito for each>> to make arrays for graphing
		if input_phrase.lower() in j.lower() and input_phrase2.lower() in j.lower() and input_phrase3.lower() in j.lower() and not input_phrase5.lower() in j.lower():
			newcount=count
			for i in xrange(0, len(master_list[0])):
				if "Wavelength".lower() in master_list[0][newcount].lower():
					new_title_list.append(master_list[0][newcount])		
					break
				else:
					newcount-=1
			new_title_list.append(j)
		count+=1
	return new_title_list

def dataRow(master_list,input_phrase):

	datarow=[]
	count=0

	#title strings are referred to as title_list list.
	#title_list=master_list[0]

	#records instances where substring matches data tile and records column of occurence. 
	for j in master_list[0]:
		#need to include wavelengths of different lengths and ito for each>> to make arrays for graphing
		if input_phrase.lower() in j.lower() and input_phrase2.lower() in j.lower() and input_phrase3.lower() in j.lower() and not input_phrase5.lower() in j.lower():
			newcount=count
			for i in xrange(0, len(master_list[0])):
				if "Wavelength".lower() in master_list[0][newcount].lower():
					datarow.append(newcount)		
					break
				else:
					newcount-=1
			datarow.append(count)
		count+=1
	return datarow

def newOnlyDataMaster(master_list):
	new_only_data_master=[]
	
	print "len x\n"
	print len(master_list[0])
	print "len y\n"
	print len(master_list)

	for i in xrange(0, len(master_list[0])):
		tmp=[]
		for j in xrange(1, len(master_list)):
			if master_list[j][i]=="":
				break
			else:
				
				tmp.append(master_list[j][i])

		new_only_data_master.append(tmp)
		
	return new_only_data_master

def makeCSV(new_title_list):
	
	master_list=masterList()
	datarow=dataRow(master_list,input_phrase)

	fullNewData=[]

	for j in datarow:
		tmpDataInstance=[]
		for i in xrange(1,len(master_list)):
			if master_list[i][j]=="":
				break
			else:
				tmpDataInstance.append(master_list[i][j])
		fullNewData.append(tmpDataInstance)

	with open(input_phrase+".txt",'w+') as fl:
		fl.write("%s\n" % fullNewData)
	fl.close()

	with open(input_phrase+"_titles.txt",'w+') as fl_t:
		fl_t.write("%s\n" % new_title_list)
	fl_t.close()

def makeGraph(new_only_data_master,dataRow,new_title_list):
	count=0
	while count<len(new_title_list):
		plt.plot(new_only_data_master[dataRow[count]],new_only_data_master[dataRow[count+1]],label=new_title_list[count+1])
		count+=2
	plt.xlabel(new_title_list[0])
        plt.ylabel(input2)
        plt.title(input_phrase+" "+input_phrase3)
        plt.legend()
	#plt.legend(bbox_to_anchor=(0.,1.02,1.,.102),loc=3,ncol=2,mode="expand",borderaxespad=0.)
	plt.legend(bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0.)
        plt.show()
print input_phrase2
print newTitleList(masterList(),input_phrase)
#print dataRow(masterList(),input_phrase)
makeCSV(newTitleList(masterList(),input_phrase))
makeGraph(newOnlyDataMaster(masterList()),dataRow(masterList(),input_phrase),newTitleList(masterList(),input_phrase))
