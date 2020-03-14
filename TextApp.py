import asyncio
from concurrent.futures.thread import ThreadPoolExecutor

import discord

from Request import Request, handle_request
from other import keys_and_strings


class TextApp:

	def __init__(self):
		print("> Starting Discord")
		self.bot_token = keys_and_strings.DC_BOT_TOKEN
		self.client = discord.Client()
		self.threads_executor = ThreadPoolExecutor(max_workers=50)

		@self.client.event
		async def on_ready():
			print('> Discord Bot = {0.user}'.format(self.client))

		@self.client.event
		async def on_message(message: discord.message):

			# Ignore your own messages and empty ones
			if message.author == self.client.user or message == '' :
				return

			req = Request(message.author.name, message.channel, message.content[:])

			res = await asyncio.get_event_loop().run_in_executor(threads_executor, handle_request, req)

			await message.channel.send(res)

			return

	def run(self):
		self.client.run(self.bot_token)


if __name__ == "__main__":

	# Initialize the Thread_Pool that handles the requests
	threads_executor = ThreadPoolExecutor(50)

	d = TextApp()
	d.run()
