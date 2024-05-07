import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

model = pyo.ConcreteModel()

model.x = pyo.Var(bounds=(0,10))
model.y = pyo.Var(bounds=(0,10))
x = model.x
y = model.y

# constraint1: -x+2yx<=8
model.C1 = pyo.Constraint(expr= -x+2*y*x<=8)

# constraint2: 2x+y<=14
model.C2 = pyo.Constraint(expr= 2*x+y<=14)

# constraint3: 2x-y<=10
model.C3 = pyo.Constraint(expr= 2*x-y<=10)

# Z = x + yx
model.obj = pyo.Objective(expr= x+y*x, sense=maximize)


# download ipopt and mention the path here
opt = SolverFactory('ipopt', executable='C:\\ipopt\\bin\\ipopt.exe')
opt.solve(model)

model.pprint()

x_value = pyo.value(x)
y_value = pyo.value(y)

print('\n---------------------------------------------------------------------')
print('x=',x_value)
print('y=',y_value)