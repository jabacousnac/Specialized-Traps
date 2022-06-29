# -*- coding: utf-8 -*-

"""QTorusKnotTrap.py: Torus knot trap using parametric drawing tool."""

import numpy as np

try:
    from .QCuCustomTrap import QCuCustomTrap as QCustomTrap
    import cupy as cp
    cp.cuda.Device()
except Exception:
    from .QCustomTrap import QCustomTrap


class QTorusKnotTrap(QCustomTrap):

    def __init__(self, p=3, q=1, **kwargs):
        super(QTorusKnotTrap, self).__init__(**kwargs)
        self._p = p
        self._q = q
        self.registerProperty('p', tooltip=True)
        self.registerProperty('q', tooltip=True)

    @property
    def p(self):
        '''As used in (p,q) representation of torus. Also equal to crossing number/(q-1)'''
        return self._p

    @property
    def q(self):
        '''Sets brige number of torus knot'''
        return self._q

    @p.setter
    def p(self, p):
        self._p = p
        self.updateStructure()
        self.valueChanged.emit(self)

    @q.setter
    def q(self, q):
        self._q = q
        self.updateStructure()
        self.valueChanged.emit(self)

    def x_0(self, t):
        return np.cos(self.q*t) * (3 + np.cos(self.p*t))
        
    def y_0(self, t):
        return np.sin(self.q*t) * (3 + np.cos(self.p*t))

    def dx_0(self, t):
        return -np.cos(self.q*t) * (self.p*np.sin(self.p*t)) -\
        self.q*np.sin(self.q*t) * (3 + np.cos(self.p*t))

    def dy_0(self, t):
        return self.q*np.cos(self.q*t) * (3 + np.cos(self.p*t)) -\
        np.sin(self.q*t) * (self.p*np.sin(self.p*t))

    def z_0(self, t):
        return np.sin(self.p*t)

    def S(self, T):
        return self.q/(4*self.p) * (38*self.p*T + 24*np.sin(self.p*T) + np.sin(2*self.p*T))
