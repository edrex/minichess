# -*- coding: UTF-8 -*-

import re

from data import *

def TCORD (move): return move & 127
def FCORD (move): return move >> 7 & 127
def PROMOTION (move): return move >> 14 & 1
def TPIECE (move): return move >> 18

################################################################################
#   The format of a move is as follows - from left:                            #
#   3 bits:  taken piece type                                                  #
#   2 bits:  flags                                                             #
#   7 bits:  cord to move from                                                 #
#   7 bits:  cord to move to                                                   #
################################################################################

shiftedFromCords = []
for i in xrange(FSQUARES):
    shiftedFromCords.append(i << 7)

shiftedPieces = {}
for i in PIECES:
    shiftedPieces[i] = i << 18

shiftedProm = 1<<14

def new_move (fromcord, tocord, piece = EMPTY, promote=False):
    move = shiftedPieces[piece] + shiftedFromCords[fromcord] + tocord
    if promote:
        move += shiftedProm
    return move

def move_string (move):
    """ Returns a string rep of a move """
    f = repc[FCORD(move)]
    t = repc[TCORD(move)]
    return "%s-%s %d %s" % (f, t, PROMOTION(move), reppieces[TPIECE(move)])

