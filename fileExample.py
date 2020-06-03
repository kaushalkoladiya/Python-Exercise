'''
file = open('hello.txt','a')
#print(file.readline())
file.write('\n'+input('Enter Somthing:'))
file.close()
file = open('hello.txt','r')
cnt = 0
while file.readline() != '':
	cnt += 1
#print(file.readline())
#print(file.readline())
print('There are total %d lines in a File' %cnt)
'''

file = 'hello.txt'
with open(file) as f:
	lines = f.readlines()
	print(len(lines))
for line in lines:	
	print(line)
	
#print(f)