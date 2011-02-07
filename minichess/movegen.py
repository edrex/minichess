from random import shuffle, choice

from data import *
from move import *

# an attempt at cheap randomization
randcords = []
for i in xrange(50):
    randcords.append(list(fcords))
    shuffle(randcords[i])

def gen_moves(state):
    board = state.board
    som = state.som # side on move
    fcords = choice(randcords)
    for fcord in fcords:
        type = board[fcord]*som
        if type > 0:
            if type == PAWN:
                for tcord in (fcord + som*NW, fcord + som*NE):
                    if board[tcord] != OFFB and state.color(tcord) == -som:
                        yield new_move(fcord, tcord, board[tcord], tcord in LASTROW[som])
                if board[fcord + som*NORTH] == EMPTY:
                    yield new_move(fcord, fcord + som*NORTH, EMPTY, tcord in LASTROW[som])
            elif type in (QUEEN, BISHOP, ROOK):
                for dir in TYPE_DIRS[type]:
                    for tcord in (fcord + dir * i for i in xrange(1, RAYLEN)):
                        tsquare = board[tcord]
                        if tsquare == 0:
                            yield new_move(fcord, tcord)
                        elif tsquare == OFFB or state.color(tcord)==som:
                            break
                        else:
                            yield new_move(fcord, tcord, tsquare)
                            break
                if type == BISHOP: # bishop swaps
                    for tcord in (fcord+dir for dir in CARDINALS):
                        if board[tcord] == 0:
                            yield new_move(fcord, tcord)
            elif type in (KING, KNIGHT):
                for tcord in (fcord + dir for dir in TYPE_DIRS[type]):
                    if board[tcord] == OFFB:
                        pass
                    elif board[tcord] == EMPTY:
                        yield new_move(fcord, tcord)
                    elif state.color(tcord) == -som:
                        yield new_move(fcord, tcord, board[tcord])

