import unittest

from minichess.data import *
from random import choice

class DataTestCase(unittest.TestCase):
    '''
    could be randomized
    how to pass in different boards?
    '''

    def setUp(self):
        pass

    def testCords(self):
        rc = choice(repc)
        rp = choice(reppieces.values())
        
        self.assertEqual(rc, repc[rep2c[rc]])
        self.assertEqual(rp, reppieces[rep2p[rp]])

if __name__ == '__main__':
    unittest.main()
