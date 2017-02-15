import numpy as np
from scipy.interpolate import interp1d
#If we know the prob. distribution for N points large, generate a random number 
#following that distribution

def RandDist(x,X,P):
#x is a vector of random numbers from an uniform distribution
#X is a vector of points for which the probability is known
#P is the probability

	P = P/np.sum(P) #normalize
	cdf = np.cumsum(P)
	cdf, indices = np.unique(cdf, return_index=True)
	X = X[indices]
	set_interp = interp1d(cdf,X, kind='linear')
	return set_interp(x)
