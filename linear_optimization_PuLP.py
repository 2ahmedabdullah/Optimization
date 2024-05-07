import pulp as pl

model = pl.LpProblem('Ex', pl.LpMaximize)

# defining bounds 0<= x <= 10
x = pl.LpVariable('x',0,10)

# defining bounds 0<= y <= 10
y = pl.LpVariable('y',0,10)

# Constraint1: -x+2y <= 8
model += -x+2*y<=8

# Constraint2: 2x+2y <= 14
model += 2*x+y<=14

# Constraint3: 2x-y <= 10
model += 2*x-y<=10

# Objective function Z = x + y
model += x+y

status = model.solve()

x_value = pl.value(x)
y_value = pl.value(y)

print('x=',x_value)
print('y=',y_value)