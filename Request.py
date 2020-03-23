import NluService as dialogflow
import WebParser


class Request:

	def __init__(self, sender_id: str, message_channel, question: str, intent: str = '', parameter: str = '',
				 answer: str = ''):
		self.sender_id = sender_id
		self.message_channel = message_channel
		self.question = question
		self.intent = intent
		self.parameter = parameter
		self.answer = answer

	def print(self):
		print(" --------- Req ---------\n\tfrom=\t", self.sender_id, '\n\t??? =\t', self.question, "\n\tnlu =\t",
			  self.intent + ' /', self.parameter, '\n\tans =\t', self.answer, '\n- - - - - - - - - - - - -', sep='')


def handle_request(req: Request):
	# global inited
	# global nlu

	req.print()

	# ----------------------- 1 ----------------------------
	# get intent from NLU
	nlu = dialogflow.NluService('session_user__#' + req.sender_id)
	req.intent, req.parameter = nlu.get_intent(req.question , req.sender_id)

	# ----------------------- 2 ----------------------------
	# get data, depending on intent
	req.answer = action_switcher(req.intent, req.parameter)

	# ----------------------- 3 ----------------------------
	# return answer, send it back to user
	return req.answer


def action_switcher(intent: str, parameter: str):
	global index
	global myd

	# print('\taction_switcher()')
	# An rwthsei gia to faq
	if intent == "faq-location":
		return "Your university is located here: " + \
			   "https://www.google.com/maps/place/Department+of+Informatics+and+Telecommunications/@37.968141,23.7643221,17z"

	elif intent == "mystudies-grade":

		if parameter == '':
			return "please ask \"what is my grade on <course>\""

		wb = WebParser.SeleniumWebParser()
		grade = wb.get_grade_of(parameter)

		return 'Your grade is ' + grade

	elif intent == 'eclass-deadlines':
		return """
		The deadline for your assignments in ΗΛΕΚΤΡΟΜΑΓΝΗΤΙΣΜΟΣ, ΟΠΤΙΚΗ, ΣΥΓΧΡΟΝΗ ΦΥΣΙΚΗ are:
		3η Εργασία Φυσικής
		Time remaining: 32 days 22 hours 31 minutes

		"""

	elif intent == "mystudies-grade-avg":

		wb = WebParser.SeleniumWebParser()
		grade = wb.get_average_grades()

		print('exit from func gpa, res = ', grade)

		return 'Your gpa is ' + grade

	elif intent == "mystudies-courses_declaration":
		pass

	elif intent == "eclass-announcement-course":

		wb = WebParser.SeleniumWebParser()
		announcement = wb.get_eclass_element(0 , parameter )

		return """Most recent announcement from """ + parameter + """ : 
		""" + announcement

	elif intent == "eclass-deadline" or intent=="eclass-announcements ":
		return "Not implemented yet."
		pass

	elif intent == 'faq-pps':
		return "The university courses can be found here: http://www.di.uoa.gr/undergraduate/coursesnew"

	elif intent == "test__name":
		return 'Hello I am DiBot!'

	elif intent == 'help':
		return """
- name (whats ur name?) 
- faq: university location (where is university?)
- faq: curriculum (what courses are offered here?)'
- eclass: course deadlines (whats my next deadlines on <course> )
- eclass: course announcements (any news from course <course> )
- mystudies: course grade (whats my grade on <course>)
- mystudies: average grade (what is my gpa)
"""

	return "I din't quite understand :( "
