#    Copyright (C) 2017  https://github.com/s4w3d0ff
#    BTC: 15D8VaZco22GTLVrFMAehXyif6EGf8GMYV
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
import logging
import tqdm
try:
    from numpy.random import RandomState
except:
    logging.warning('Could not find numpy.random, using random.SystemRandom')
    from random import SystemRandom as RandomState

logger = logging.getLogger(__name__)


class SlotMachine(object):
    """ A simple, expandable, customizable slotmachine complete with
    identifyable 'jackpot' and 'bonus' symbols.
    """

    def __init__(self, jack='BAR', bonus='!!!',
                 base=['(M)', '(N)', '(W)', '(X)', '(H)', '(O)', '(Z)'],
                 multi=3, size=(3, 1), randomState=None):
        self.jack, self.bonus, self.base = jack, bonus, base
        self.multi, self.size = multi, size
        self.reel = self.buildReel()
        if randomState:
            self.randomState = randomState
        else:
            self.randomState = RandomState()
        self.count = 0
        self.sinceJack = 0
        self.odds = None
        self.lastSpin = None

    def buildReel(self):
        """ Makes the self.reel array """
        logger.info('Building Reel')
        # make reversed copy of 'base'
        rbase = self.base[::-1]
        # append 'bonus' to 'reversed base'
        rbase.append(self.bonus)
        # add 'reversed base'+'bonus' to 'base'
        nbase = rbase + self.base
        # append another 'bonus' to 'new base'
        nbase.append(self.bonus)
        # extend nbase num 'times'
        reel = nbase * int(self.multi)
        # add jackpot symbol to front
        reel.insert(0, self.jack)
        # return 'reel' with extra 'bonus' removed
        return reel[:-1]

    def __call__(self):
        """ Pulls the 'handle' """
        logger.debug('Spinning machine')
        # set empty display
        nCols, nRows = range(self.size[0]), range(self.size[1])
        # pick symbols and fill display
        raw = [[self.reel[i - row] for row in nRows]
               for i in [self.randomState.choice(range(len(self.reel)))
                         for col in nCols]]
        self.count += 1
        self.sinceJack += 1
        # return display (turned 90 so it makes more
        # sense and easier to traverse/read)
        self.lastSpin = [[col[i] for col in raw] for i in range(len(raw[0]))]
        return self.lastSpin

    def checkLine(self, line):
        """ Overwrite to fit your machine """
        if line.count(self.jack) == len(line):
            self.sinceJack = 0
            return 'jackpot'
        if line.count(self.bonus) == len(line):
            return 30
        if line.count(line[0]) == len(line):
            return 10
        return False

    def calcOdds(self, times=1000000):
        tally = {}
        logger.info('Calculating odds...')
        for i in tqdm.trange(times):
            r = self.checkLine(self.__call__()[0])
            if str(r) not in tally:
                tally[str(r)] = 0
            tally[str(r)] += 1
        self.odds = tally
        self.count = 0
        self.sinceJack = 0


if __name__ == '__main__':
    from sys import argv
    s = SlotMachine()
    if len(argv) > 1:
        s.calcOdds(argv[1])
        print(s.odds)
    else:
        logging.basicConfig(level=logging.INFO)
        r = s()[0]
        print(r)
        print(s.checkLine(r))
