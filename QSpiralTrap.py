# -*- coding: utf-8 -*-

"""QSpiralTrap.py: Spiral trap using parametric drawing tool."""

import numpy as np

try:
    from .QCuCustomTrap import QCuCustomTrap as QCustomTrap
    import cupy as cp
    cp.cuda.Device()
except Exception:
    from .QCustomTrap import QCustomTrap


class QSpiralTrap(QCustomTrap):

    def __init__(self, a=20, n=1, **kwargs):
        super(QSpiralTrap, self).__init__(**kwargs)
        self._a = a
        self._n = n
        self.registerProperty('a', tooltip=True)
        self.registerProperty('n', tooltip=True)

    @property
    def a(self):
        '''Sets size of spiral.'''
        return self._a

    @property
    def n(self):
        '''Sets winding number of spiral'''
        return self._n

    @a.setter
    def a(self, a):
        self._a = a
        self.updateStructure()
        self.valueChanged.emit(self)

    @n.setter
    def n(self, n):
        self._n = n
        self.updateStructure()
        self.valueChanged.emit(self)

    def x_0(self, t):
        return self.a/2 * t * np.cos(self.n*np.pi*t)

    def dx_0(self, t):
        return self.a/2 * np.cos(self.n*np.pi*t) -\
               self.n/2*np.pi*self.a*t * np.sin(self.n*np.pi*t)

    def y_0(self, t):
        return self.a/2 * t * np.sin(self.n*np.pi*t)

    def dy_0(self, t):
        return self.a/2 * np.sin(self.n*np.pi*t) +\
                self.n/2*np.pi*self.a*t * np.cos(self.n*np.pi*t)

    def z_0(self, t):
        return t

    def S(self, T):
        return self.n*np.pi/12 * (self.a)**2 * T**3
