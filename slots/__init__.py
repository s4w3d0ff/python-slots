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

from random import choice
import logging

logger = logging.getLogger(__name__)


class SlotMachine(object):
    """ A simple, expandable, customizable slotmachine complete with
    identifyable 'jackpot' and 'bonus' symbols.
    """

    def __init__(self, jack='BAR', bonus='!!!',
                 base=['(M)', '(N)', '(W)', '(X)', '(H)', '(O)', '(Z)'],
                 multi=3, size=(3, 1)):
        self.jack, self.bonus, self.base = jack, bonus, base
        self.multi, self.size, self.reel = multi, size, None
        self.buildReel(self.multi)

    def buildReel(self, multi):
        """ Makes the self.reel array """
        logger.info('Buliding Reel')
        # make reversed copy of 'base'
        rbase = self.base[::-1]
        # append 'bonus' to 'reversed base'
        rbase.append(self.bonus)
        # add 'reversed base'+'bonus' to 'base'
        nbase = rbase + self.base
        # append another 'bonus' to 'new base'
        nbase.append(self.bonus)
        # extend nbase num 'times'
        reel = nbase * int(multi)
        # add jackpot symbol to front
        reel.insert(0, self.jack)
        # save 'self.reel' with extra 'bonus' removed
        self.reel = reel[:-1]
        logger.debug(self.reel)

    def __call__(self):
        """ Pulls the 'handle' """
        logger.info('Spinning machine')
        # set empty display
        nCols, nRows = range(self.size[0]), range(self.size[1])
        # pick symbols and fill display
        raw = [[self.reel[i - row] for row in nRows]
               for i in [choice(range(len(self.reel))) for col in nCols]]
        # return display (turned 90 so it makes more
        # sense and easier to traverse/read)
        return [[col[i] for col in raw] for i in range(len(raw[0]))]

    def checkLine(self, line):
        """ Overwrite to fit your machine """
        if line.count(self.jack) == len(line):
            return 'jackpot'
        if line.count(self.bonus) == len(line):
            return 30
        if line.count(line[0]) == len(line):
            return 10
        return False

if __name__ == '__main__':
    from sys import argv
    s = SlotMachine()
    if len(argv) > 1:
        tally = {}
        for i in range(int(argv[1])):
            r = s.checkLine(s()[0])
            if str(r) not in tally:
                tally[str(r)] = 0
            tally[str(r)] += 1
        print(tally)
    else:
        logging.basicConfig(logging.INFO)
        r = s()[0]
        print(r)
        print(s.checkLine(r))
