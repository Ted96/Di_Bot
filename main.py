from Request import *
import NluService as dialogflow
from Request import *
from TextApp import TextApp
from WebParser import test

inited: int
globals()['inited'] = 0
nlu: dialogflow.NluService


def handle_request(req: Request):
	global inited
	global nlu

	req.print()

	if inited == 0:
		nlu = dialogflow.NluService('DIBOT_request')
		inited = 1

	# ----------------------- 1 ----------------------------
	# get intent from NLU
	nlu = dialogflow.NluService(req.sender_id)
	req.intent, req.parameter = nlu.get_intent(req.question)

	# ----------------------- 2 ----------------------------
	# do stuff depending on intent
	req.answer = action_switcher(req.intent, req.parameter)

	return


def action_switcher(intent: str, parameter: str):
	global index
	global myd

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
		return '*grade*'

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
		ans = test()
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
		pass

	elif intent == "eclass-deadline":
		# input: Course
		# Kane login sto eclass kai fere to deadline gia tis ergasies enos ma8hmatos
		# output: Course Deadline
		pass

	elif intent == "test__name":
		return '*test__name*'

	return '|!|not-found-intent|!|)'


if __name__ == '__main__':
	# nlu = dialogflow.NluService('main!')
	# globals()['nlu'] = nlu

	text_app = TextApp()
	text_app.run()

	print('------- END MAIN ----------')
#######################################################################
#######################################################################




	# print('\t1')
	# nlu = dialogflow.NluService( r.sender_id )
	# r.intent , wtfisthis = await nlu.get_intent(r.question)
	# print('\t\t2')
