import re
from django.core import mail

from .base import FunctionalTests

TEST_EMAIL = 'edith@example.com'
SUBJECT = 'Your login link for Superlists'

class LoginTest(FunctionalTests):

	def test_can_get_email_link_to_log_in(self):
		#Edith goes to the awesome superlists site and notices a "Log in" section in the navbar for the first time.
		#It's telling her to enter her email address, so she does

		self.browser.get(self.server_url)
		self.browser.find_element_by_name('email').send_keys(TEST_EMAIL + '\n')

		#A message appears telling her an email has been sent
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Check your email', body.text)

		#She checks her email and finds a message
		email = mail.outbox[0]
		self.assertIn(TEST_EMAIL, email.to)
		self.assertEqual(email.subject, SUBJECT)

		#It has a url link in it
		self.assertIn('Use this link to log in', email.body)
		url_search = re.search(r'http://.+.+$', email.body)
		if not url_search:
			self.fail('could not find url in email body:\n{}'.format(email.body))
		url = url_search.group(0)
		self.assertIn(self.server_url, url)

		#She clicks it
		self.browser.get(url)

		#She is logged in!
		self.assert_logged_in(email=TEST_EMAIL)

		#Now she logs out
		self.browser.find_element_by_link_text('Log out').click()

		#She is logged out
		self.assert_logged_out(email=TEST_EMAIL)