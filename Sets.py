from __future__ import division
from pyomo.environ import *

model = AbstractModel()

model.A = Set()

# One way to create a set whose members will be two dimensional is to use the dimen argument:
model.B = Set(dimen=2)

# To create a set of all the numbers in set model.A doubled, one could use
def doubleA_init(model):
	return (i*2 for i in model.A)
model.C = Set(initialize = DoubleA_init)

# The initialize option can refer to a Python set, which can be returned by a function or given directly as in
model.D = Set(initialize=['red', 'green', 'blue'])

# The initialize option can also specify a function that is applied sequentially to generate set members
def Z_init(model, i):
	if i > 10:
		return Set.End
	return 2*i+1
model.Z = Set(initialize=Z_init)

# If sets are given as arguments to Set without keywords, they are interpreted as indexes for an array of sets. For example,
# to create an array of sets that is indexed by the members of the set model.A, use
model.E = Set(model.A)

# Arguments can be combined. For example, to create an array of sets with three dimensional members indexed by set model.A, use
model.F = Set(model.A, dimen=3)