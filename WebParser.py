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
		self.driver = webdriver.Chrome(keys_and_strings.PATH_TO_DRIVER)  # initiate a driver, in this case Firefox    <<...lmfao firefox
		self.driver.set_window_size(width=1280, height=720)   # if window too narrow : dropdown doesnt appear !
		# headless??  problem with width ^^^ ?

		# login info
		if self.which_mode == 1:
			self.url = 'https://eclass-sandbox.noc.uoa.gr/'
			self.elem_usr 	= 'uname'
			self.elem_pass 	= 'pass'
			self.val_usr	= 'stud11'
			self.val_pass 	= 'teststudpass'

		# initiate
		self.driver.get(self.url) # go to the url

		# login
		username_field = self.driver.find_element_by_name(self.elem_usr)
		password_field = self.driver.find_element_by_name(self.elem_pass)
		username_field.send_keys(self.val_usr)
		password_field.send_keys(self.val_pass)
		password_field.send_keys(Keys.RETURN)

	# todo :  design this ::: <<make alot of functions>>    (to return stuff according to usecases)
	def get_element(self , course_name : str = '') -> str:

		# get list of courses from main page
		webelem_courses = self.driver.find_elements_by_xpath('//table/tbody/tr/td/b/a')
		# #webelem_courses = self.driver.find_elements_by_class_name('text-left')

		# click on the course with name = [ most similar to the string parameter {:course_name}  ]
		# https://www.datacamp.com/community/tutorials/fuzzy-string-python
		for c in webelem_courses:
			if c.text == course_name:
				c.click()

		w_side_categories = self.driver.find_elements_by_class_name('list-group-item')
		# indexes :::       0=anakoinwseis   1=ergasies   2=ergasies      5=plhrofories
		w_side_categories[ 0 ].click()

		return 'gg'


if __name__ == "__main__":

	wb = SeleniumWebParser()

	print(wb.get_element('Εισαγωγή στον Προγραμματισμό'))
