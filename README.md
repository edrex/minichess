Some parts of this software are adapted from PyChess.
In particular data.py is based on ldata.py in PyChess.
Also some PyChess tests were adapted.

See LICENSE for licensing information.

## INSTALL

minichess should be on the python path, while tests can be anywhere. 

I wrote a small suite of tests which helped to keep the bugs out.
To run the test suite without installing (tested on Python 2.5):
    cd tests
    sh run run_tests.py # sets PYTHONPATH

## STRATEGIES

4 strategies are included:

 * Random: chooses a legal move at random
 * Flat: chooses a move with a high static value
 * NegaMax: standard adversary search
  * iterative deepening until a time limit is hit
  * overshoots the time limit so has unpredictable timing
 * AlphaBeta: NegaMax optimized to trim search branches which aren't relevant

## COMPETITION

 * The engine will play games with itself or humans via skirmish.py
 * Also plays on the IMCS server:
  * Game between my AlphaBeta and NegaMax strategies:
          http://wiki.cs.pdx.edu/minichess/logs/3261
  * Game between two AlphaBeta instances:
          http://wiki.cs.pdx.edu/minichess/logs/3264
 * I haven't implemented any dynamic time management:
   Both strategies take the next run that overshoots 3.0s,
   however long it takes. This can lead to draws in competition,
   especially against a tough opponent.
      
## Minichess implementation

 * Move generation is simple and slow, using a generator to "feel around" the board.
 * The board is represented by an "augmented" 7x10=70 element array,
      which allows easy detection of "falling off the board".
 * Moves are reversible, so there is only one state, which is modified incrementally.
      Moves are stored bitwise in a single int32.

## Performance

Currently AlphaBeta only reaches 6 plies in reasonable time. Further optimizations
such as TT, opening book, and endgame DB should help.

Python isn't ideal for highly recursive algorithms.
Potential speedups can also come from:

 * Applying Psycho (Python JIT compiler)
 * Profiling to detect hotspots for optimization
 * Optimizing data structures and precomputing lots of stuff in lookup tables(bitboards etc)
