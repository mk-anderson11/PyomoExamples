from __future__ import division
from pyomo.environ import *

model = ConcreteModel()

model.x = Var([1], domain=NonNegativeReals)

model.OBJ = Objective(expr = 36*model.x[1] - model.x[1]**2, sense = maximize)

model.Constraint1 = Constraint(expr = model.x[1] >= 1)
