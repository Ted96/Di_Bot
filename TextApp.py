import asyncio

import discord

import NluService as df
from other import keys_and_strings


class TextApp:
	# 0 = echo     1 = dialogflow
	available_modes = ['Echo', 'AI']
	mode: int

	def __init__(self, default_mode=1):
		print("> Starting Discord")
		self.bot_token = keys_and_strings.DC_BOT_TOKEN
		self.client = discord.Client()
		self.mode = default_mode

		# todo : remove
		self.ai_service = df.NluService('MyDiBot')

		for guild in self.client.guilds:
			print(guild.name)

		@self.client.event
		async def on_ready():
			print('We have logged in as {0.user}'.format(self.client))

		@self.client.event
		async def on_message(message: discord.message):

			# This message came from this bot
			if message.author == self.client.user:
				return

			# This message came from other user, and its for me
			# if message.content.startswith(';'):

			text = message.content[:]
			curr_channel: discord.channel.DMChannel = message.channel
			# sender : discord.message. = message.author

			if text == 'mode':
				# goto next mode
				self.mode = (self.mode + 1) % len(self.available_modes)
				await curr_channel.send(':warning:  Mode --> ' + self.available_modes[self.mode] + ' :warning:')
				return

			if self.mode == 0:				# echo back mode
				await curr_channel.send('Echo= `' + text + '`')
				return

			if self.mode == 1:
				# dialogflow mode  //todo REMOVE dialogflow class from this file
				answer: str = self.ai_service.get_intent(text)

				# switch here ()

				await curr_channel.send('AI= `<' + answer + '>`')
				return

			print('((', message.author.name, '))')

	def run(self):

		# self.client.run(self.bot_token)

		loop = asyncio.get_event_loop()
		try:
			a = loop.run_until_complete(self.client.start(self.bot_token))
			print(a)
		except KeyboardInterrupt:
			loop.run_until_complete(self.client.logout())
		# cancel all tasks lingering
		finally:
			loop.close()

	def __exit__(self, exc_type, exc_val, exc_tb):
		print('????? exiting ???????')

	def __del__(self):
		print('????? deleting ???????')


if __name__ == "__main__":
	d = TextApp(0)
	d.run()
	exit()
