# -*- coding: utf-8 -*-
# MENU: Add trap/Torus knot trap

from ..QTask import QTask
from pyfablib.traps.QTorusKnotTrap import QTorusKnotTrap
from PyQt5.QtGui import QVector3D


class TorusKnotTrap(QTask):
    """Add a torus knot trap to the trapping pattern"""

    def __init__(self, center3=None, p=3, q=1, **kwargs):
        super(TorusKnotTrap, self).__init__(**kwargs)
        self.center3 = center3 or (self.parent().cgh.device.xc,
                                   self.parent().cgh.device.yc,
                                   0)
        self.p = p
        self.q = q

    def complete(self):
        (xc, yc, zc) = self.center3
        trap = QTorusKnotTrap(p=self.p, q=self.q,
                               r=QVector3D(xc, yc, zc))
        self.parent().pattern.addTrap(trap)
