from data import *
# white
pvals = {
    PAWN: 100,\
    BISHOP: 300,\
    KNIGHT: 300,\
    ROOK: 500,\
    QUEEN: 900,\
    -PAWN: -100,\
    -BISHOP: -300,\
    -KNIGHT: -300,\
    -ROOK: -500,\
    -QUEEN: -900,\
    KING: 10000,\
    -KING: -10000,\
    EMPTY: 0,\
}    

def value(state):
    return state.som * sum(pvals[state.board[cord]] for cord in fcords)

def game_lost(state):
    try:
        state.board.index(KING*state.som)
        return False
    except ValueError:
        return True

def game_drawn(state):
    if state.turn >= 80:
        return True
    else:
        return False
