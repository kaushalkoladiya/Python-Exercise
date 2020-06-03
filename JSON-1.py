import json
num = [1,3,7,9,2,0,6,8]
fileName = '/storage/emulated/0/Xender/python/num.json'
with open(fileName,'w') as f:
	json.dump(num,f)
	