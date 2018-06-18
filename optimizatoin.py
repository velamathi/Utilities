import numpy as np
from scipy.optimize import minimize
from math import sqrt


def objective(x):
    return (x[0]**2)

def constraint1(x):
    return objective([x])-81.0

x0 = [1.0]

# show initial objective
print('Initial Objective: ' + str(objective(x0)))

# optimize
b = (1,20)
bnds = [b]
con1 = {'type': 'eq', 'fun': constraint1}
cons = ([con1])
solution = minimize(objective,x0,method='SLSQP',\
                    bounds=bnds,constraints=cons)
x = solution.x

# show final objective
print('Final Objective: ' + str(objective(x)))

# print solution
print('Solution')
print('x1 = ' + str(x[0]))
