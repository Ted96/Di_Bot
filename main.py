from TextApp import TextAppDiscord

def main():
	# initialize everything
	# df_nlu = ChatbotService('wtfdoitypehere')
	pass

	dc_bot = TextAppDiscord()

	for text in dc_bot.run():
		print('------>' , text)

	print('------- END MAIN ----------')

if __name__ == '__main__':
	main()


# message = 	dc.message
# intent = 	df.ask( message )
# answer = 	formulate_answer( intent )
# dc.sendbackto( author , answer)
#
#
#
#
# #
# if intent:
# 	pass
# 	wb = webparser()
# 	ergasies = wb.getelement_ergasies
# 	return ergasies
# elif intent:
# 	pass
# elif intent:
# 	pass