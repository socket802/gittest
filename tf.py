import json


mydict = {"apple":1, "orange":2, "banana":3}

file = open("venuelist.json", 'w')

file.write('{"index":{"_index":"love"}}\n');
json.dump(mydict, file)
file.write('\n');
file.close()

