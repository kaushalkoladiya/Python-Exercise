try :
	f = '/storage/emulated/0/Xender/python/hello.txt'
	with open(f) as file:
		data = file.readlines()
except Exception as e:
	print(f,'this file is not found')
	
else:
	cnt = 0
	#cntdata = data.split()
	for x in data:
		cnt += len(x.split())
	#	for y in x:
	#		print(y)
	print(cnt)
	print(len(data))