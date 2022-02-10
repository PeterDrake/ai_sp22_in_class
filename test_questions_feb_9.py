from unittest import TestCase
from questions_feb_9 import *

class Test(TestCase):
    def test_add(self):
        self.assertEqual(5, add(2, 3))
