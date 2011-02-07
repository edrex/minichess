from random import choice
from time import clock

from data import *
from movegen import *
from eval import *

def random(state):
    moves = list(gen_moves(state))
    if len(moves):
        return choice(list(gen_moves(state)))
    else: return None

def flat(state):
    hiscore = -100000
    bestmoves = []
    for move in gen_moves(state):
        state.move(move)
        score = -value(state)
        state.unmove()
        if score > hiscore:
            hiscore = score
            bestmoves = [move]
        elif score == hiscore:
            bestmoves.append(move)
    if len(bestmoves):
        return choice(bestmoves)

def negamax(s, t=3.0):
    stime = clock()
    d = 0
    while clock() - stime < t:
        d += 1
        hiscore = -10000
        for m in gen_moves(s):
            s.move(m)
            score = -_negamax(s, d-1)
            s.unmove()
            #print move_string(m), score
            if score > hiscore:
                hiscore = score
                best_move = m
    return best_move, d, clock() - stime

def _negamax(s, d=2):
    if game_lost(s):
        return -9999
    elif game_drawn(s) or d==0:
        return value(s)
    else:
        hiscore = -9999
        for m in gen_moves(s):
            s.move(m)
            score = -_negamax(s, d-1)
            s.unmove()
            if score > hiscore:
                hiscore = score
    return hiscore

def alphabeta(s, t=3.000):
    stime = clock()
    d = 0
    while clock() - stime < t:
        d+=1
        v = -10000
        a0 = v
        for m in gen_moves(s):
            s.move(m)
            v0 = max(v, -_alphabeta(s, d, -10000, -a0))
            s.unmove()
            a0 = max(a0, v0)
            #print move_string(m), score
            if v0 > v:
                v = v0
                m0 = m
    return m0, d, clock() - stime

def _alphabeta(s, d, a, b):
    if game_lost(s):
        return -9999
    elif game_drawn(s) or d==0:
        return value(s)
    else:
        v = -9999
        for m in gen_moves(s):
            s.move(m)
            v = -_alphabeta(s, d-1, -b, -a)
            s.unmove()
            if v > a:
                a = v
                if v >= b:
                    return v
        return v
