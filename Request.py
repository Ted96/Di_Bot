class Request:

	def __init__(self, sender_id : str, message_channel, question: str, intent: str = '', parameter: str = '', answer: str = ''):
		self.sender_id = sender_id
		self.message_channel = message_channel
		self.question = question
		self.intent = intent
		self.parameter = parameter
		self.answer = answer

	def print(self):
		print(" --------- Req ---------\n\tfrom=\t", self.sender_id, '\n\t??? =\t', self.question, "\n\tnlu =\t",
			self.intent + ' /', self.parameter, '\n\tans =\t', self.answer, '\n- - - - - - - - - - - - -', sep='')
