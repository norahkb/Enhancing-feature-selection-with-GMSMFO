import numpy as np
import matplotlib.pyplot as plt

# Define the objective function
def objective_Fun(x):
    dim = len(x)
    o = np.sum(100 * (x[1:dim] - x[0:dim-1])*2 + (x[0:dim-1] - 1)*2)
    return o

# Define the MFO optimization algorithm
def MFO(objective_function, swarm_size, dim, max_iterations):
    # Initialize the convergence curve array
    convergence_curve = np.zeros(max_iterations)

    # Initialize the population
    population = np.random.uniform(-30, 30, (swarm_size, dim))

    # Perform iterations
    for iteration in range(max_iterations):
        # Evaluate the fitness of each individual in the population
        fitness = [objective_function(x) for x in population]

        # Update the convergence curve
        convergence_curve[iteration] = np.min(fitness)

        # Find the best moth (individual) in the population
        best_moth_index = np.argmin(fitness)
        best_moth = population[best_moth_index]

        # Update the positions of moths
        for i in range(swarm_size):
            if i != best_moth_index:
                distance = np.linalg.norm(population[i] - best_moth)
                step_size = np.random.uniform(0, 1, dim)
                population[i] += step_size * (population[i] - best_moth) / distance

                # Apply boundary constraints
                population[i] = np.clip(population[i], -30, 30)

    return convergence_curve

# Set the optimization parameters
swarm_size = 30
dim = 50
max_iterations = 50
NoRuns = 10

# Run the MFO optimization algorithm
convergence_curves = []
for run in range(NoRuns):
    convergence_curve = MFO(objective_Fun, swarm_size, dim, max_iterations)
    convergence_curves.append(convergence_curve)

convergence_curves = np.array(convergence_curves)

# Plot the convergence curves of all runs
idx = range(max_iterations)
fig = plt.figure()

ax = fig.add_subplot(111)
for i in range(NoRuns):
    ax.plot(idx, convergence_curves[i])

plt.title('Convergence Curve of the MFO Optimizer', fontsize=12)
plt.ylabel('Fitness')
plt.xlabel('Iterations')
plt.show()
