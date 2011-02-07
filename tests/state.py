import unittest

from minichess.State import *
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
""",
]
class InitStateTestCase(unittest.TestCase):

    def setUp(self):
        self.initboard = choice(test_boards)
        self.state = State(self.initboard)

    def testload(self):
        ''' compares input board with printed representation of state '''

        self.assertEqual(self.state.__str__().strip(), self.initboard.strip())

    def testgenmoves(self):
        for move in gen_moves(self.state):
            self.state.move(move)
            self.state.unmove()
            InitStateTestCase.testload(self)

    # test legal move generation?
    # manually gen movelists?
    # can use pysets for comparison
    
if __name__ == '__main__':
    unittest.main()
