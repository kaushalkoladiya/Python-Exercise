try:
	file = 'hello.txt'
	with open(file) as f:
		print(f.read())
except Exception as e:
	print(e)