import time
import datetime
import requests

url  = 'http://raw.githubusercontent.com/socket802/gittest/master/dta.txt'

def GetTF(url):
	r = requests.get(url)

	#print(r.text)
	rawdata = r.text.split("\n")

	#data size
	length = len(rawdata)
	print(rawdata[5])
	print(rawdata[length-1])

	#data split
	tmp = rawdata[length-1].split(" ")
	print(tmp)

	#timestamp sereal value
	ttme = datetime.datetime.fromtimestamp(1577804400)
	print(ttme.isoformat())

	#data output
	input = tmp[2]
	output = tmp[3]
	

	#taple output
	return input,output
	
	#KVS output
	
	
print(GetTF(url))




#for line in r.text.split("\n"):
#    print line