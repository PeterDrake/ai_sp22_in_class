from unittest import TestCase
from tictactoe import *


class Test(TestCase):

    def test_generates_successor(self):
        before = 'XOX......'
        after = successor(before, 'O', 5)
        self.assertEqual('XOX..O...', after)
