import NluService as dialogflow
import WebParser


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



def handle_request(req: Request):
	# global inited
	# global nlu

	req.print()

	# ----------------------- 1 ----------------------------
	# get intent from NLU
	nlu = dialogflow.NluService('session_user__#' + req.sender_id)
	req.intent, req.parameter = nlu.get_intent(req.question)

	# ----------------------- 2 ----------------------------
	# get data, depending on intent
	req.answer = action_switcher(req.intent, req.parameter)

	# ----------------------- 3 ----------------------------
	# return answer, send it back to user
	return '==' + req.answer


def action_switcher(intent: str, parameter: str):
	global index
	global myd

	# print('\taction_switcher()')
	# An rwthsei gia to faq
	if intent == "faq":
		# input: None
		# Fere  tis erwthseis h tis apanthseis me vash to faq
		# output: The Questions And The Answers
		pass

	# alliws an rwthsei kapoion va8mo se kapoio ma8hma
	elif intent == "mystudies-grade":

		# input: Course (i.e: Psychics)
		# Kane login sto my-studies kai fere ton va8mo gia ayto to ma8hma
		# output: Course Grade
		wb = WebParser.SeleniumWebParser()
		grade = wb.get_grade_of( parameter )
		return '*grade*=' + grade

	elif intent == "mystudies-grade-avg":
		# input: Course (i.e: Psychics)
		# Kane login sto my-studies kai fere ton va8mo gia ayto to ma8hma
		# output: Course Grade

		# wb = SeleniumWebParser()
		# # thr = threading.Thread( target=wb.get_average_grades)
		#
		# ans = wb.get_average_grades()
		#
		# t = threading.Thread(name='mythread__'+str(index), target=test, args=(myd, req))
		# t.start()
		# index = index + 1
		# pos = t.getName()[-1]
		#	t.join()
		ans = WebParser.test()
		print('exit from func, res = ', ans)

		return '*gpa*='

	elif intent == "mystudies-courses_declaration":
		# input: None
		# Kane login sto my-studies kai fere tis dhlwseis gia to trexon e3amhno
		# output: Course Declarations
		pass

	elif intent == "eclass-announcements":
		# input: None
		# Kane login sto eclass kai fere ta anoucements gia ola, h ena ma8hma
		# output: Top 5 most recent announcements?
		return intent
		pass

	elif intent == "eclass-deadline":
		# input: Course
		# Kane login sto eclass kai fere to deadline gia tis ergasies enos ma8hmatos
		# output: Course Deadline
		return intent
		pass

	elif intent == 'faq-pps':
		return "check out this link for what courses are offered:---"

	elif intent == "test__name":
		return '*test__name*'

	elif intent == 'help':
		return '-name (test)' \
			   '-faq where is ...' \
			   '-faq programma spoudwn' \
			   '-eclass deadlines' \
			   '-eclass anouncements (general+course)' \
			   '-mystudies grade (average+course)'

	return intent
	#return '|!|not-found-intent|!|)'

