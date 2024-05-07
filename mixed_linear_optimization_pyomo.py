import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

model = pyo.ConcreteModel()

# defining bounds 0<= x <= 10 (INTEGERS) new parameter added
model.x = pyo.Var(within = Integers, bounds=(0,10))

# defining bounds 0<= y <= 10 (BINARY) new parameter added
model.y = pyo.Var(within = Binary, bounds=(0,10))


x = model.x
y = model.y

# Constraint1: -x+2y <= 8
model.C1 = pyo.Constraint(expr= -x+2*y<=8)

# Constraint2: 2x+2y <= 14
model.C2 = pyo.Constraint(expr= 2*x+y<=14)

# Constraint3: 2x-y <= 10
model.C3 = pyo.Constraint(expr= 2*x-y<=10)

# Objective function Z = x + y
model.obj = pyo.Objective(expr= x+y, sense=maximize)

opt = SolverFactory('glpk')
opt.solve(model)

model.pprint()

x_value = pyo.value(x)
y_value = pyo.value(y)

print('\n---------------------------------------------------------------------')
print('x=',x_value)
print('y=',y_value)