import unittest

from minichess.State import *
from minichess.strategies import *
from minichess.movegen import *

test_boards = [\
initial_board, \
"""
7 B
.qb.r
Pkppp
..n..
..P..
.P.PP
RNBQK
""",\
"""
15 B
.qkbr
p.ppp
Q....
..P..
P.BPP
RN.K.
""",\
"""
8 W
k.b.r
pnppp
qp...
P..p.
RPPNP
..BQK
""",\
]
class SearchTestCase(unittest.TestCase):

    def setUp(self):
        self.initboard = test_boards[3]
        #self.initboard = choice(test_boards)
        self.state = State(self.initboard)

    def testnegamax(self):
        ''' test deep negamax search '''
        m, d, t = negamax(self.state, t=3.0)
        print ' d = %d, time = %ds' % (d, t)

        self.assertEqual(self.state.__str__().strip(), self.initboard.strip())

    def testalphabeta(self):
        m, d, t = alphabeta(self.state, t=3.0)
        print ' d = %d time = %ds' % (d, t)
        self.assertEqual(self.state.__str__().strip(), self.initboard.strip())


    # test legal move generation?
    # manually gen movelists?
    # can use pysets for comparison
    
if __name__ == '__main__':
    unittest.main()
