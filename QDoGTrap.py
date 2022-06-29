# -*- coding: utf-8 -*-

"""QDoGTrap.py: DoG Trap"""

from .QTrap import QTrap
import numpy as np
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtGui import (QPainterPath, QFont, QTransform)


class QDoGTrap(QTrap):

    def __init__(self, sigma=40, tau=20, alpha=1, **kwargs):
        super(QDoGTrap, self).__init__(alpha=alpha, **kwargs)
        self._sigma = sigma
        self._tau = tau
        self.registerProperty('sigma', tooltip=True)
        self.registerProperty('tau', tooltip=True)

    def updateStructure(self):
        n_m = 1.49
        f = 1e-6/48e-9
        rho = self.cgh.qr
        u = self.sigma**2 * np.exp((1j * self.sigma * rho / (2 * np.pi * f * n_m))**2) - self.tau**2 * np.exp((1j * self.tau * rho / (2 * np.pi * f * n_m))**2)
        phi = np.angle(np.cos(u)-1/(np.sin(u)))
        self.structure = np.exp(1j * phi)

    def plotSymbol(self):
        sym = QPainterPath()
        font = QFont('Sans Serif', 10, QFont.Black)
        sym.addText(0, 0, font, 'D')
        # Scale symbol to unit square
        box = sym.boundingRect()
        scale = 1./max(box.width(), box.height())
        tr = QTransform().scale(scale, scale)
        # Center symbol on (0, 0)
        tr.translate(-box.x() - box.width()/2., -box.y() - box.height()/2.)
        return tr.map(sym)

    @pyqtProperty(float)
    def sigma(self):
        return self._sigma

    @sigma.setter
    def sigma(self, sigma):
        self._sigma = sigma
        self.updateStructure()

    @pyqtProperty(int)
    def tau(self):
        return self._tau

    @tau.setter
    def tau(self, tau):
        self._tau = tau
        self.updateStructure()
