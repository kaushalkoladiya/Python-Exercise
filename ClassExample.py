class abc:
	def __init__(self):
		self.a=5
		self.b=1
	#	abc.dis()
	@classmethod	
	def dis(self):
		print('sum:')
#	def dis(self,sum):
#		print('hello form second display')
	@staticmethod
	def dis2():
		print('hello')
obj = abc()
#obj.dis(12)
abc.dis()
obj.dis2()