from data import *

class Piece:
    '''stored in pieces array'''
    def __init__(self, type, row, col):
        self.type = type
        self.row = row
        self.col = col

    def __str__(self):
        return "%d (%d, %d)" % (self.type, self.row, self.col)