class AnonymousClass:
	def __init__(self,question):
		self.question = question
		self.responses = []
		
	def showQuestion(self):
		print(self.question)
	
	def takeResponse(self,response):
		self.responses.append(response)
	
	def responseResult(self):
		print('Survey:')
		for x in self.responses:
			print(' ' + x)
'''		
obj = AnonymousClass('how are you')
obj.showQuestion()
obj.takeResponse("i'm fine")
obj.responseResult()
'''
