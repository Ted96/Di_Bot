import os

import dialogflow_v2 as dialogflow

from other import keys_and_strings


class ChatbotService:
	session_client: dialogflow.SessionsClient
	session_name: str

	def __init__(self, name: str = 'dibot'):

		# Authenticate this program
		os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = keys_and_strings.PATH_TO_GOOGLE_JSON

		self.session_client = dialogflow.SessionsClient()
		self.session_name = name

		print('> Starting DFlow  //session=', self.session_name)

	def ask(self, question: str):
		# get intent for question

		answer: str

		# remove from here?
		current_session = self.session_client.session_path(keys_and_strings.PROJECT_ID, self.session_name)

		text_input = dialogflow.types.TextInput(text=question, language_code='en-US')
		query = dialogflow.types.QueryInput(text=text_input)
		response = self.session_client.detect_intent(session=current_session, query_input=query)

		answer = response.query_result.fulfillment_text

		############ debug ##################
		print('\nQ = {}'.format(response.query_result.query_text))
		print('A = {}'.format(response.query_result.fulfillment_text))
		print('DF_Intent= {} ({:0.1f}%)\n'.format(
			response.query_result.intent.display_name,
			response.query_result.intent_detection_confidence * 100))
		#####################################

		return answer


if __name__ == "__main__":

	# Authenticate this program
	# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials.PATH_TO_GOOGLE_JSON

	mybot = ChatbotService('wtfdoitypehere')

	print(mybot.ask('What is your name?'))
	# detect_intent_texts(PROJECT_ID, 'me', ['who are you?'])
	print('--End Dflow--')
