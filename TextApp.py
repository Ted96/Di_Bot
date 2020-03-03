import asyncio
from concurrent.futures.thread import ThreadPoolExecutor

import discord

import NluService as dialogflow
import WebParser
from Request import Request
from other import keys_and_strings

# Initialize the Thread_Pool that handles the requests
threads_executor = ThreadPoolExecutor(50)


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
		pass

	elif intent == "eclass-deadline":
		# input: Course
		# Kane login sto eclass kai fere to deadline gia tis ergasies enos ma8hmatos
		# output: Course Deadline
		pass

	elif intent == "test__name":
		return '*test__name*'

	return '|!|not-found-intent|!|)'


class TextApp:

	def __init__(self):
		print("> Starting Discord")
		self.bot_token = keys_and_strings.DC_BOT_TOKEN
		self.client = discord.Client()
		self.threads_executor = ThreadPoolExecutor(max_workers=50)

		@self.client.event
		async def on_ready():
			print('We have logged in as {0.user}'.format(self.client))

		@self.client.event
		async def on_message(message: discord.message):

			# This message came from this bot// continue
			if message.author == self.client.user or message == '' :
				return

			req = Request(message.author.name, message.channel, message.content[:])

			res = await asyncio.get_event_loop().run_in_executor(threads_executor, handle_request, req)

			await message.channel.send(res)

			return

	def run(self):
		self.client.run(self.bot_token)


if __name__ == "__main__":

	d = TextApp()
	d.run()
