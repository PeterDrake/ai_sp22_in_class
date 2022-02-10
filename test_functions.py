from unittest import TestCase
from functions import *


class Test(TestCase):

    def test_longest_word(self):
        quote = ['faster', 'higher', 'stronger', 'together']
        self.assertEqual('stronger', longest_word(quote))
