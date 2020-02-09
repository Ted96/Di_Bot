from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from other import keys_and_strings


class SeleniumWebParser:

	def __init__(self , mode=1):

		self.which_mode = mode    # 1 eclass   2 mystudies
		self.elem_usr	: str
		self.elem_pass 	: str
		self.val_usr	: str
		self.val_pass 	: str
		self.url 		: str
		self.driver = webdriver.Chrome(keys_and_strings.PATH_TO_DRIVER)  # initiate a driver, in this case Firefox

		# login info
		if self.which_mode == 1:
			self.url = 'https://eclass-sandbox.noc.uoa.gr/'
			self.elem_usr 	= 'uname'
			self.elem_pass 	= 'pass'
			self.val_usr	= 'stud11'
			self.val_pass 	= 'teststudpass'

		# initiate
		self.driver.get(self.url) # go to the url

		# locate the login form
		username_field = self.driver.find_element_by_name(self.elem_usr) # get the username field
		password_field = self.driver.find_element_by_name(self.elem_pass) # get the password field

		# log in
		username_field.send_keys(self.val_usr) # enter in your username
		password_field.send_keys(self.val_pass) # enter in your password
		password_field.send_keys(Keys.RETURN) # submit it

		# print HTML
		html = self.driver.page_source
		# print( html )

	# todo :  design this ::: <<make alot of functions>>    (to return stuff according to usecases)
	def get_element(self , elem :str = '') -> str:
		return 'gg'


if __name__ == "__main__":
	wb = SeleniumWebParser()
	print(wb.get_element())
