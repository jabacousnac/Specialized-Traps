# -*- coding: utf-8 -*-
# MENU: Add trap/Spiral trap

from ..QTask import QTask
from pyfablib.traps.QSpiralTrap import QSpiralTrap
from PyQt5.QtGui import QVector3D


class SpiralTrap(QTask):
    """Add a spiral trap to the trapping pattern"""

    def __init__(self, center3=None, a=20, n=1, **kwargs):
        super(SpiralTrap, self).__init__(**kwargs)
        self.center3 = center3 or (self.parent().cgh.device.xc,
                                   self.parent().cgh.device.yc,
                                   0)
        self.a = a
        self.n = n

    def complete(self):
        (xc, yc, zc) = self.center3
        trap = QSpiralTrap(a=self.a, n=self.n,
                               r=QVector3D(xc, yc, zc))
        self.parent().pattern.addTrap(trap)
