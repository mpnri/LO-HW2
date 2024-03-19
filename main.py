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

model.obj = pyo.Objective(expr=200 * sum((model.x[i] + model.y[i]) for i in model.i), sense = pyo.minimize)

