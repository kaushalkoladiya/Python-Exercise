import json

file = '/storage/emulated/0/Xender/python/UsernameAndPassword.json'
try:	
	userName = ''	#dict
	with open(file,'w') as f:
		idPass = ''	#list
		print('inside try')
except Exception as e:
	print('sorry')