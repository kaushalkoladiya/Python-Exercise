import json
fileName = '/storage/emulated/0/Xender/python/num.json'
with open(fileName) as f:
	num = json.load(f)
print(num)