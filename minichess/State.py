import re

from move import *
from data import *

class State:

    def __init__(self, board = EMPTY_BOARD):
        """Initialize a new state using a board string in the format used by the class (examples see data.py)"""

        # expand rows as separate subgroups
        # since re only saves last hit per subgroup
        row_pattern = '([%s]{%d})' % (''.join(reppieces.values()), COLS)
        board_pattern = '^\s*(\d+)\s+([WB])\s+%s\s*$$' % ('\s+'.join([row_pattern] * ROWS))
        board_regex = re.compile(board_pattern)
        try:
            groups = board_regex.match(board).groups()
        except:
            print "Failed to parse board:"
            print board
            raise
        if groups[1] == 'W':
            self.som = W
        elif groups[1] == 'B':
            self.som = B

        else: raise "no side"
        self.turn = int(groups[0])

        boardStr = ''.join(groups[2:])

        # initialize an augmented board
        self.board = [OFFB] * FSQUARES
        for cord in xrange(SQUARES):
            self.board[fcords[cord]] = rep2p[boardStr[cord]]

        self.history = []

    def move(self, move):
        if PROMOTION(move):
            self.board[TCORD(move)] = QUEEN * self.som
        else:
            self.board[TCORD(move)] = self.board[FCORD(move)]
        self.board[FCORD(move)] = EMPTY
        self.som = -self.som
        self.turn += 1
        self.history.append(move)

    def unmove(self):
        move = self.history.pop()
        self.som = -self.som
        self.turn -= 1
        if PROMOTION(move):
            self.board[FCORD(move)] = PAWN * self.som
        else:
            self.board[FCORD(move)] = self.board[TCORD(move)]
        self.board[TCORD(move)] = TPIECE(move)

    def __str__(self):
        return '%d %s\n%s' % \
            (self.turn, colorrep[self.som], \
            '\n'.join((''.join((reppieces[self.board[cord]] for cord in row)) for row in ROWCORDS )))

    def color(self, cord):
        square = self.board[cord]
        if square == EMPTY:
            return 0
        elif square > 0: return W
        elif square < 0 and square != OFFB: return B
        else:
            print self
            raise IndexError("Seeking color of illegal square %d (%s)" % (cord, repc[cord]))
        