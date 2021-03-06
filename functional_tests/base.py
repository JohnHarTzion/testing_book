import sys
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

class FunctionalTests(StaticLiveServerTestCase):

	@classmethod
	def setUpClass(cls):
		for arg in sys.argv:
			if 'liveserver' in arg:
				cls.server_url = 'http://' + arg.split('=')[1]
				return
		super(FunctionalTests, cls).setUpClass()
		cls.server_url = cls.live_server_url

	def setUp(self):
		self.browser = webdriver.Chrome('.././chromedriver')
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def check_for_rows_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = self.browser.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def get_item_input_box(self):
		return self.browser.find_element_by_id('id_text')

	def assert_logged_in(self, email):
		self.browser.find_element_by_link_text('Log out')
		navbar = self.browser.find_element_by_css_selector('.navbar')
		self.assertIn(email, navbar.text)

	def assert_logged_out(self, email):
		self.browser.find_element_by_name('email')
		navbar = self.browser.find_element_by_css_selector('.navbar')
		self.assertNotIn(email, navbar.text)