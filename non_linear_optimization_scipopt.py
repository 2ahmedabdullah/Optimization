from pyscipopt import Model

model = Model('exemplo')

x = model.addVar('x')
y = model.addVar('y')
z = model.addVar('z')

model.setObjective(z, sense='maximize')

# z = x+xy
model.addCons(z==x+y*x)

# constraint1: -x+2xy<=8
model.addCons(-x+2*y*x<=8)

# constraint2: 2x+y<=14
model.addCons(2*x+y<=14)

# constraint3: 2x-y<=10
model.addCons(2*x-y<=10)

model.optimize()

sol = model.getBestSol()

print('x=',sol[x])
print('y=',sol[y])