from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from other import keys_and_strings


def test() -> str :

	# print('\n ++ thread ' , index)

	wb = SeleniumWebParser()
	answer = wb.get_average_grades()

	# global_dicc[str(index)] = ans

	return answer


class SeleniumWebParser:

	def __init__(self):
		chrome_options = webdriver.ChromeOptions()
		prefs = {"profile.managed_default_content_settings.images": 2}
		chrome_options.add_experimental_option("prefs", prefs)

		self.driver = webdriver.Chrome(keys_and_strings.PATH_TO_DRIVER, options=chrome_options)
		self.driver.set_window_size(width=1280, height=720)  # if window too narrow : dropdown doesnt appear !
		# todo: headless??  problem with width  (left menu) ^^^ ?

	def login_website(self, site : int):

		# mystudies
		if site == 1 :
			from other import mycredentials
			url = 'https://my-studies.uoa.gr/secr3w/connect.aspx'
			elem_usr = 'username'
			elem_pass = 'password'
			val_usr = mycredentials.hidden_u
			val_pass = mycredentials.hidden_p
		else :  # site == 2:
			url = 'https://eclass-sandbox.noc.uoa.gr/'
			elem_usr = 'uname'
			elem_pass = 'pass'
			val_usr = 'stud11'
			val_pass = 'teststudpass'

		# initiate
		self.driver.get(url)  # go to the url

		# login
		username_field = self.driver.find_element_by_name(elem_usr)
		password_field = self.driver.find_element_by_name(elem_pass)
		username_field.send_keys(val_usr)
		password_field.send_keys(val_pass)
		password_field.send_keys(Keys.RETURN)


	def get_average_grades(self) -> str:
		# mystudies : get average grade

		self.login_website(1)

		sum_grades: float = 0
		counter = 0

		self.driver.get('https://my-studies.uoa.gr/Secr3w/app/accHistory/default.aspx')
		self.driver.switch_to.frame('accmain')
		all_tr_rows = self.driver.find_elements_by_xpath('//table/tbody/tr')

		for row in all_tr_rows:
			if not str(row.text).endswith('\n '):
				continue  # this row is not a course-grade

			td_columns = row.text.split('\n')

			course: str = td_columns[0]
			course = course[course.find('- ') + 2:  course.rfind('(')]

			# string compare -->  check if course ==  {:course_name}
			grade: str = td_columns[1]
			grade = grade[grade.find('(') + 1:   grade.find(')')]

			if ',' in grade or '.' in grade:
				grade: float = float(grade.replace(',', '.'))
			else:
				grade: int = int(grade)

			if grade < 5:
				continue

			print("\t__WB__ //mystudies: ", course, '\t= ', grade)

			sum_grades = sum_grades + grade
			counter = counter + 1

		self.driver.close()
		# this takes alot of time :: self.driver.quit()

		return str((sum_grades / counter).__round__(2))

	def get_grade_of(self, course_name: str = '') -> str:

		self.login_website(1)

		# mystudies : get grade
		grade: str = '0'

		self.driver.get('https://my-studies.uoa.gr/Secr3w/app/accHistory/default.aspx')
		self.driver.switch_to.frame('accmain')
		all_tr_rows = self.driver.find_elements_by_xpath('//table/tbody/tr')

		for row in all_tr_rows:
			if not str(row.text).endswith('\n '):
				continue  # this row is not a course-grade

			td_columns = row.text.split('\n')

			course: str = td_columns[0]
			course = course[course.find('- ') + 2:  course.rfind('(')]

			# string compare -->  check if course ==  {:course_name}
			if course_name.upper() in course:
				grade = td_columns[1]
				grade = grade[grade.find('(') + 1:   grade.find(')')]
				print("\t__WB__ //mystudies  found : ", course_name, '\t= ', grade)
				break

		return grade

	def get_element(self, course_name: str = '') -> str:

		self.login_website(2)

		# eclass : get anakoinwseis  +  ergasies  +  plhrofories ma8hmatos

		# get list of courses from main page
		webelem_courses = self.driver.find_elements_by_xpath('//table/tbody/tr/td/b/a')
		# #webelem_courses = self.driver.find_elements_by_class_name('text-left')

		#  string compare --> click on the course with name = [ most similar to the string parameter {:course_name}  ]
		# https://www.datacamp.com/community/tutorials/fuzzy-string-python
		for c in webelem_courses:
			if c.text == course_name:
				c.click()

		w_side_categories = self.driver.find_elements_by_class_name('list-group-item')
		# indexes :::       0=anakoinwseis   1=ergasies   2=ergasies      5=plhrofories
		w_side_categories[0].click()

		return 'gg'


if __name__ == "__main__":

	wb = SeleniumWebParser()

	print("\n\n", wb.get_average_grades(), "/10")   # ok
# print(wb.get_grade_of('Εισαγωγη στον Προγραμματισμο')) # ok  <greeklish
