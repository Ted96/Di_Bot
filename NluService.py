import os

import dialogflow_v2 as dialogflow

from other import keys_and_strings


class NluService:

	def __init__(self, name: str = 'dibot_dialogflowNLUservice'):

		# Authenticate this program
		os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = keys_and_strings.PATH_TO_GOOGLE_JSON

		self.session_client : dialogflow.SessionsClient = dialogflow.SessionsClient()
		self.session_name : str = name

		print('> Starting DFlow  //session=', self.session_name)

	def get_intent(self, question: str):
		# get intent for question

		# remove from here?  :
		current_session = self.session_client.session_path(keys_and_strings.PROJECT_ID, self.session_name)

		text_input = dialogflow.types.TextInput(text=question, language_code='en-US')
		query = dialogflow.types.QueryInput(text=text_input)
		response = self.session_client.detect_intent(session=current_session, query_input=query)

		############ debug ##################
		print('\nQ = {}'.format(response.query_result.query_text))
		print('A = {}'.format(response.query_result.fulfillment_text))
		print('DF_Intent= {} ({:0.1f}%)\n'.format(
			response.query_result.intent.display_name,
			response.query_result.intent_detection_confidence * 100))
		#####################################

		return response.query_result.intent.display_name


if __name__ == "__main__":

	mybot = NluService('wtfdoitypehere')
	print('//MAIN : intent=', mybot.get_intent('What is your name?'))
	print('--End Dflow--')
