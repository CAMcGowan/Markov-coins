import numpy as np

def number_of_flips(n_flips, n_same):
	''' Takes the number of times the coin is flipped and the amount
	required  to be the same, returns a probability matrix of results'''
	# define the varibles
	pn = p0_gen(n_same)
	m = m_gen(n_same)
	# loop the number of flips
	for i in range(n_flips):
		pn = np.dot(pn,m)
	print('P'+str(n_flips)+': ',pn)
	return pn

def m_gen(n):
	''' Generates the markov matrix '''
	# Initalize an empty n by n matrix
	matrix = np.array([])
	#create the first row
	row_1 = np.ones(n)/2
	row_1[-1] = 0
	matrix = np.append(matrix, row_1, axis=0)
	# create the subsequent rows
	for i in range(n-1):
		row = np.zeros(n)
		row[i] = 0.5
		matrix = np.append(matrix, row, axis=0)
	# convert to a n by n matrix
	matrix = matrix.reshape(n,n)
	matrix[-1][-1] = 1
	matrix = matrix.transpose()
	return matrix

def p0_gen(n):
	''' Generates P0 depending on number the same'''
	p0 = np.zeros(n)
	p0[0] = 1
	return p0
	
# Example
number_of_flips(2,3)