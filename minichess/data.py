reppieces = {
  0 : '.',
 -1 : 'k',
  1 : 'K',
 -2 : 'q',
  2 : 'Q',
 -3 : 'b',
  3 : 'B',
 -4 : 'r',
  4 : 'R',
 -5 : 'n',
  5 : 'N',
 -6 : 'p',
  6 : 'P',
 -9 : '#',
}

# invert charmap
rep2p = dict([[v,k] for k,v in reppieces.iteritems()])

reprows = '876543210_'
repcols = 'zabcdef'
repc = [c+r for r in reprows for c in repcols]

'''
['z_', 'a_', 'b_', 'c_', 'd_', 'e_', 'f_',
 'z0', 'a0', 'b0', 'c0', 'd0', 'e0', 'f0',
 'z1', 'a1', 'b1', 'c1', 'd1', 'e1', 'f1',
 'z2', 'a2', 'b2', 'c2', 'd2', 'e2', 'f2',
 'z3', 'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 
 'z4', 'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 
 'z5', 'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 
 'z6', 'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 
 'z7', 'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 
 'z8', 'a8', 'b8', 'c8', 'd8', 'e8', 'f8']
'''

rep2c = {}
for cord, name in enumerate(repc):
    rep2c[name] = cord

FROWS = len(reprows)
FCOLS = len(repcols)
ROWS = FROWS - 4
COLS = FCOLS - 2
SQUARES = ROWS * COLS
RAYLEN = max(ROWS,COLS)

# lookup table for full cords
fcords = [cord + 2*FCOLS + 1 + cord/COLS*2 for cord in xrange(SQUARES)]
origcords = dict([[fcords[i],i] for i in xrange(len(fcords))])
FSQUARES = (2+COLS)*(4+ROWS)

def CORD(row, col):
    return row*COLS + col

ROWCORDS = [fcords[rowst: rowst+COLS] for rowst in xrange(0, SQUARES, COLS)]

# maps between internal rep and string rep

EMPTY = 0
KING = 1
QUEEN = 2
BISHOP = 3
ROOK = 4
KNIGHT = 5
PAWN = 6
OFFB = -9

WPIECES = (KING, QUEEN, BISHOP, ROOK, KNIGHT, PAWN)
BPIECES = tuple(-p for p in WPIECES)
PIECES = WPIECES + BPIECES + (EMPTY,)
W = 1
B = -1
colorrep= {
  1 : 'W',
  -1 : 'B',
}

# fcord deltas for each dir
NORTH = -COLS-2
SOUTH = -NORTH
EAST = 1
WEST = -EAST
NW = NORTH + WEST
NE = NORTH + EAST
SW = -NE
SE = -NW

CARDINALS = [NORTH, SOUTH, EAST, WEST]
DIAGS = [NW, NE, SW, SE]
DIRS = CARDINALS + DIAGS

KD = [NORTH + 2, SOUTH + 2, NORTH -2, SOUTH -2,\
    2*NORTH + 1, 2*NORTH - 1, 2*SOUTH + 1, 2*SOUTH - 1]
TYPE_DIRS = [[], CARDINALS + DIAGS, CARDINALS + DIAGS, DIAGS, CARDINALS, KD, []]

LASTROW = {W: ROWCORDS[0], B: ROWCORDS[ROWS-1]}

initial_board = '''
0 W
kqbnr
ppppp
.....
.....
PPPPP
RNBQK
'''

EMPTY_BOARD = '''
0 W
.....
.....
.....
.....
.....
.....
'''


