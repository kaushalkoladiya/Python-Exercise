import unittest
from TestCasePkg import AnonymousClass

class abc(unittest.TestCase):
	def test(self):
		question = 'Which language you Speak.'
		obj = AnonymousClass(question)
		obj.showQuestion()
		obj.takeResponse('English')
		obj.responseResult()
		self.assertIn('English',obj.responses)
		
#abc().test()
unittest.main()