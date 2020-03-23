import os

import dialogflow_v2 as dialogflow

from other import keys_and_strings


class NluService:

	def __init__(self, session_id: str = 'dibot_'):
		# Authenticate this program
		os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = keys_and_strings.PATH_TO_GOOGLE_JSON

		self.client : dialogflow.SessionsClient = dialogflow.SessionsClient()
		self.session_name : str = session_id

		print('> Started DialogFlow.  //session=', self.session_name)

	def get_intent(self, question: str , session_name2 : str = '0') -> tuple :
		# get intent for question
		current_session = self.client.session_path(keys_and_strings.PROJECT_ID, self.session_name + session_name2)

		text_input = dialogflow.types.TextInput(text=question, language_code='en-US')
		query = dialogflow.types.QueryInput(text=text_input)

		response = self.client.detect_intent(session=current_session, query_input=query)

		############ debug ##################
		print('\nQ = {}'.format(response.query_result.query_text))
		print('A = {}'.format(response.query_result.fulfillment_text))
		print('DF_Intent= {} ({:0.1f}%)\n'.format(
			response.query_result.intent.display_name,
			response.query_result.intent_detection_confidence * 100))
		#####################################

		# if parameters exist, return them too
		parameter : str = ''
		if bool(response.query_result.parameters):
			parameter = response.query_result.parameters.items()[0][1]

		return response.query_result.intent.display_name, parameter


if __name__ == "__main__":

	mybot = NluService('doesnotmatterwhatitypehere')
	print('//MAIN : intent=', mybot.get_intent('What is your name?'))
	print('--End Dflow--')
