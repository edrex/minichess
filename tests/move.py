import unittest
from random import choice, randrange

from minichess.move import *

class MoveTestCase(unittest.TestCase):
    '''
    could be randomized
    how to pass in different boards?
    '''

    def setUp(self):
        self.f, self.t, self.p, self.prom = randrange(SQUARES), randrange(SQUARES), choice(PIECES), choice((True, False))
        self.move = new_move(self.f, self.t, self.p, self.prom)

    def testtcord(self):
        self.assertEqual(TCORD(self.move), self.t)

    def testfcord(self):
        self.assertEqual(FCORD(self.move), self.f)

    def testtpiece(self):
        self.assertEqual(TPIECE(self.move), self.p)

    def testprom(self):
        self.assertTrue(PROMOTION(self.move) == self.prom, "%d, %d" % (self.move, self.t))

if __name__ == '__main__':
    unittest.main()
