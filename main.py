import pyomo.environ as pyo

model = pyo.ConcreteModel()

# * index and param
model.i = pyo.Set(initialize=[1, 2, 3, 4, 5])
model.p = pyo.Param(model.i, initialize={1: 40_000, 2: 30_000, 3: 60_000, 4: 0, 5: 0})

# * D Variables
model.x = pyo.Var(model.i, domain=pyo.NonNegativeIntegers)
model.y = pyo.Var(model.i, domain=pyo.NonNegativeIntegers)
model.a = pyo.Var(model.i, domain=pyo.NonNegativeIntegers)
model.b = pyo.Var(model.i, domain=pyo.NonNegativeIntegers)
model.c = pyo.Var(model.i, domain=pyo.NonNegativeIntegers)
model.d = pyo.Var(model.i, domain=pyo.NonNegativeIntegers)

model.obj = pyo.Objective(
    expr=200 * sum((model.x[i] + model.y[i]) for i in model.i), sense=pyo.minimize
)


# * Constraints
def const1_rule(model, i):
    return model.a[i] <= model.x[i] * 40 * 4


model.const1 = pyo.Constraint(model.i, rule=const1_rule)


def const2_rule(model, i):
    return model.b[i] <= model.y[i] * 40 * 6


model.const2 = pyo.Constraint(model.i, rule=const2_rule)

# * Preprocess Constraints
model.const3 = pyo.Constraint(expr=model.d[1] == model.a[1] + model.c[1])
model.const4 = pyo.Constraint(expr=model.d[2] + model.c[1] == model.a[2] + model.c[2])
model.const5 = pyo.Constraint(expr=model.d[3] + model.c[2] == model.a[3] + model.c[3])
model.const6 = pyo.Constraint(expr=model.d[4] + model.c[3] == model.a[4] + model.c[4])
model.const7 = pyo.Constraint(expr=model.d[5] + model.c[4] == model.a[5] + model.c[5])
model.const8 = pyo.Constraint(expr=model.c[5] == 0)

# * Save Constraints
model.const9 = pyo.Constraint(expr=model.a[1] == model.b[1] + model.d[1])
model.const10 = pyo.Constraint(expr=model.a[2] + model.d[1] == model.b[2] + model.d[2])
model.const11 = pyo.Constraint(expr=model.a[3] + model.d[2] == model.b[3] + model.d[3])
model.const12 = pyo.Constraint(expr=model.a[4] + model.d[3] == model.b[4] + model.d[4])
model.const13 = pyo.Constraint(expr=model.a[5] + model.d[4] == model.b[5] + model.d[5])
model.const14 = pyo.Constraint(expr=model.d[5] == 0)

solver = pyo.SolverFactory("glpk", executable="/usr/bin/glpsol")

result = solver.solve(model)

print("Solver's status:", result.solver.status)

print("Solver's termination condition:", result.solver.termination_condition)

print("\nOptimal Solution:")
for i in model.i:
    print(f"x{i} =", model.x[i]())

print()

for i in model.i:
    print(f"y{i} =", model.y[i]())

print()
for i in model.i:
    print(f"a{i} =", model.a[i]())
print()
for i in model.i:
    print(f"b{i} =", model.b[i]())
print()
for i in model.i:
    print(f"c{i} =", model.c[i]())
print()
for i in model.i:
    print(f"d{i} =", model.d[i]())
print()
print("Objective function's value (z) =", model.obj())
