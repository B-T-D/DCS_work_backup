dt = 0.0001
iterations = 100000000

t = 0
for index in range(iterations):
    t = t + dt

correct = dt * iterations # Correct value of t from the carbon-14 decay model
print(correct, t)
error = (correct - t) / correct
print(f"off by {error}")
