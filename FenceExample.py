from __future__ import division
from pyomo.environ import *

model = ConcreteModel()

model.x = Var([1,2], domain=NonNegativeReals)

# Maximize the area fenced in
model.OBJ = Objective(expr = model.x[1] * model.x[2], sense = maximize)

# You are constrained by the total amount of fence (2 sides of x and 1 side y because one side is a preexisting wall)
model.Constraint1 = Constraint(expr = 2*model.x[1] + model.x[2] <= 500)

