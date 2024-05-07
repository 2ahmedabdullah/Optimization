from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('CBC')

# use Intvar for integer and defining bounds 0<= x <= 10 
x = solver.IntVar(0,10,'x')

# defining bounds 0<= y <= 10
y = solver.NumVar(0,10,'y')

# Constraint1: -x+2y <= 8
solver.Add(-x+2*y<=7)

# Constraint2: 2x+2y <= 14
solver.Add(2*x+y<=14)

# Constraint3: 2x-y <= 10
solver.Add(2*x-y<=10)

# Objective function Z = x + y
solver.Maximize(x+y)

results = solver.Solve()

if results==pywraplp.Solver.OPTIMAL: print('Optimal Found')

print('x:', x.solution_value())
print('y:', y.solution_value())
