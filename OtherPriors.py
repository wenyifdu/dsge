from __future__ import division
import numpy as np

from scipy.special import gammaln
import scipy.stats as rv
class InvGamma(object):

    def __init__(self, a, b):

        self.a = a
        self.b = b

    def logpdf(self, x):
        a = self.a
        b = self.b
        if x < 0:
            return -1000000000000

        lpdf = (np.log(2) - gammaln(b/2) + b/2*np.log(b*a**2/2)
                -(b+1)/2*np.log(x**2) - b*a**2/(2*x**2))
        return lpdf
        
    
    def rvs(self):
        rn = rv.norm.rvs(size=(int(self.b), 1))
        return np.sqrt(self.b*self.a**2 / np.sum(rn**2, 0))

