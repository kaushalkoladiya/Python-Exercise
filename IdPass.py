import json

file = '/storage/emulated/0/Xender/python/UsernameAndPassword.json'
dict = ''
cnt = 0
try:
	print('how are you')
	with open(file,'w') as f:
		idPass = '' #list
		idPass.append(input('Enter Username:'))
		idPass.append(input('Enter Password:'))
		dict[cnt] = idPass
		cnt += 1
		json.dump(idPass,f)
except Exception as e:
	pass
	print('hello')
else:
	print(idPass)
with open(file,'r') as f:
#	username = json.load(f)
	print('hello here')