# coding:UTF-8
import json
import csv
import os
import sys
import time

def GetPerf(row):

	with open(sys.argv[1] + '-ng.csv', 'a') as w:
		writer = csv.writer(w)
		writer.writerow(row)

#main
celldb = dict()


#import cell databese
with open(sys.argv[1]) as r:
	reader = csv.reader(r)
	for row in reader:
		#celldb.update({"802115": { "cid":"802115", "tac":"1545", "pci":"123" , "geo":[141.292534094, 43.0773043276], "perf":"大阪府", "city":"大阪市"}})
		celldb.update( { row[4] : { "cid":row[4],   "tac":row[3], "pci":row[5], "geo":[row[6],        row[7]       ], "perf":row[8],   "city":row[8]  }})
		#print(celldb)

#acct no for loop mogi data
insertdata = dict()
notmatchcounter = 0

tel     = "819012476666"
apn     = "biglobe.jp"
type    = "Start(2)"
mnomcc  = "44050"
sgsnip = "100.64.0.1"
ggsnip = "100.64.0.2"
sharedip = "100.64.0.3"
imei    = "43245525254535455342"
context = "au_sgn_ctx"
timestamp = "aaa"


#test case (celldb not match)
uli = "1919511088"

#test case (celldb match)
#uli = "191951107"


try:
	insertdata.update({"tel":tel, "apn":apn, "type":type, "mnomcc":mnomcc, "sgsnip":sgsnip, "ggsnip":ggsnip, "sharedip":sharedip, "imei":imei, "context":context, "cell":celldb[uli], "time":timestamp})
	print(celldb[uli])
	print(insertdata)

except KeyError:
	notmatchcounter += 1
	damy = { "cid":"802115", "tac":"1545", "pci":"123" , "geo":[141.292534094, 43.0773043276], "perf":"虚無", "city":"大阪市"}
	insertdata.update({"tel":tel, "apn":apn, "type":type, "mnomcc":mnomcc, "sgsnip":sgsnip, "ggsnip":ggsnip, "sharedip":sharedip, "imei":imei, "context":context, "cell":damy, "time":timestamp})
	print(insertdata)
