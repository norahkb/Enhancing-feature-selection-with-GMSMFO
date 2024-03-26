import random # import random module which provides functions to generate random num
import numpy as np #for num computing in python
import math # provides math function and constant
import matplotlib.pyplot as plt #for the dataframwork and final figure


def objective_Fun(x):
    dim = len(x) #assign the length of the x in dim
    o = np.sum(100 * (x[1:dim] - x[0:dim-1])**2 + (x[0:dim-1] - 1)**2) #based on X compute o
    return o

#set parameter
Max_iterations = 50  #max num of iteration
swarm_size = 30  #size of practical swarm
LB = -30  #lower bound of search space
UB = 30  #upper bound of search space
Dim = 50   # Dimensionality of the problem
NoRuns = 10 # Number of independent runs


# Initialize the convergence curve array
ConvergenceCurve = np.zeros((Max_iterations, NoRuns))

# Perform the optimization runs
for r in range(NoRuns):
    result = []
    for _ in range(Max_iterations):
        x = np.random.uniform(LB, UB, Dim)  # Generate a random solution
        fitness = objective_Fun(x)  #calculate the fittness value
        result.append(fitness)
    ConvergenceCurve[:, r] = result

#generates a plot to visualize the convergence of the optimization algorithm over iterations
idx = range(Max_iterations)
fig = plt.figure()

ax = fig.add_subplot(111)
for i in range(NoRuns):
    ax.plot(idx, ConvergenceCurve[:, i])

plt.title('Convergence Curve of without Optimizer', fontsize=12)
plt.ylabel('Fitness')
plt.xlabel('Iterations')
plt.show()
