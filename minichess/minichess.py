from numpy import *
import re
from sys import stdin, stdout
from optparse import OptionParser

from data import *
from State import *
from move import *
from eval import *
from movegen import *
import strategies

def play(strategy, color=W, debug=False):
    if debug:
        logfile = open(options.strategy+'.txt', 'w')
    state = State(initial_board)
    move_regex = re.compile('^\! ([a-e][1-6])-([a-e][1-6])')
    outcome = None
    while outcome == None:
        if debug: print state
        if state.som == color:
            if game_lost(state):
                stdout.write('= %s wins\n' % colorrep[- state.som])
                outcome = -state.som
            elif game_drawn(state):
                stdout.write('Draw\n')
                outcome = 0
            else:
                move = strategy(state)[0]
                state.move(move)
                #if debug:
                #    logfile.write( '! %s-%s\n' % (repc[FCORD(move)], repc[TCORD(move)]))
                #    logfile.flush()
                stdout.write('! %s-%s\n' % (repc[FCORD(move)], repc[TCORD(move)]))
            stdout.flush()
        else:
            match = None
            while not match:
                line = stdin.readline()
                if debug:
                    logfile.write(line)
                    logfile.flush()
                match = move_regex.match(line)
            t, f = match.groups()
            tcord, fcord = rep2c[t], rep2c[f]
            move = new_move(tcord, fcord, state.board[fcord])
            if move in gen_moves(state):
                state.move(move)
            else:
                stdout.write("bad move")
                stdout.flush()

parser = OptionParser()
parser.add_option("-c", "--color", dest="color",
                  help="color to play", default='W')
parser.add_option("-s", "--strategy", dest="strategy",
                  help="strategy to use",  default='alphabeta')
parser.add_option("-d", "--debug", dest="debug", action="store_true", default=False, help="output what is happening")
(options, args) = parser.parse_args()

if options.color == 'W':
    color = W
elif options.color == 'B': 
    color = B
else:
    raise RuntimeError("bad color")
strategy = getattr(strategies, options.strategy)

play(strategy, color, options.debug)

