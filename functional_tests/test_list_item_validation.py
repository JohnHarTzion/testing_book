from .base import FunctionalTests


class ItemValidationTest(FunctionalTests):

	def test_cannot_add_empty_list_items(self):
		#Edith goes to the home page and accidentally tries to submit an empty list item. She hits enter on the empty input box

		#The home page refreshes, and there is an error message saying that list items cannot be blank

		#She tries again with some text for the item, which now works

		#Preversely, she now decides to submit a second blank list item

		#She recieves a similar warning on the list

		#And she can correct it by filling in some text
		self.fail("write me!")