import matplotlib.pyplot as plt

from die import Die

# Create a D6 and a D10.
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(50_000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

# Visualize the results.

x_values = range(2, max_result+1)
y_values = frequencies

fig, ax = plt.subplots()

ax.bar(x_values, y_values)

plt.show()

