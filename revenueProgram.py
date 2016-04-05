''' 
This example requires a solver capable of handling quadratics. I have tested and certified that cplex works.

The SCD group has quickly developed their novel proprietary scheduling/control software and are ready to
sell. Now the only problem is deciding on the price of the licenses. Fortunately, we can model this problem and optimize it in order to maximize revenue.

Cost of Software = 2000 + 200x    (USD)
# Licenses Sold  = 500 - 8x 
x is a price increase. For every price increase of $200, 8 less licenses will be sold.

Objective Function:
Revenue = (Cost of Software)*(# Licenses Sold)
'''

from __future__ import division
from pyomo.environ import *

model = ConcreteModel()

model.x = Var(domain = NonNegativeReals)

def cost(x):
	return 2000 + 200*x # USD

def numLicenses(x):
	return 500 - 8*x

def obj_expression(model):
	return cost(model.x)*numLicenses(model.x)

model.OBJ = Objective(rule=obj_expression, sense = maximize)

model.Constraint1 = Constraint(expr = model.x >= 1)

'''
Maximum revenue is achieved when x = 26.25:
	Cost of Software = $7,250
	# Licenses Sold  =  290
	Total Revenue    = $2,102,500
'''
