import asyncio

import discord

import ChatbotService as df
from other import keys_and_strings


class TextApp:
	# 0 = echo     1 = dialogflow
	available_modes = ['Echo', 'AI']
	mode: int

	def __init__(self, default_mode=0):
		print("> Starting Discord")
		self.bot_token = keys_and_strings.DC_BOT_TOKEN
		self.client = discord.Client()
		self.mode = default_mode

		# todo : remove
		self.ai_service = df.ChatbotService('MyDiBot')

		for guild in self.client.guilds:
			print(guild.name)

		@asyncio.coroutine
		@self.client.event
		async def on_ready():
			print('We have logged in as {0.user}'.format(self.client))

		@asyncio.coroutine
		@self.client.event
		async def on_message(message: discord.message):

			# This message came from this bot
			if message.author == self.client.user:
				return

			# This message came from other user, and its fom me
			if message.content.startswith(';'):

				text = message.content[1:]

				if text == 'mention':
					# curr_user = message.author.get

					# await self.client.
					curr_channel: discord.channel.DMChannel = message.channel
					# u : discord.user.User = message.author
					await curr_channel.send(message.author.mention)
					return

				if text == 'mode':
					# goto next mode
					self.mode = (self.mode + 1) % len(self.available_modes)

					await message.channel.send(':warning:  Mode --> ' + self.available_modes[self.mode] + ' :warning:')
					return

				if self.mode == 0:
					# echo back mode
					await message.channel.send('Echo= `' + text + '`')
					return

				if self.mode == 1:
					# dialogflow mode  //todo REMOVE dialogflow class from this file
					answer: str = self.ai_service.ask(text)
					await message.channel.send('AI= `' + answer + '`')
					return

				# sender : discord.message. = message.author
				print('::', message.author.name)

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
