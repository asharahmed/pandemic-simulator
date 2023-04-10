import random
import matplotlib.pyplot as plt

# Define simulation parameters
POPULATION_SIZE = 1000
INFECTION_RATE = 0.3
MUTATION_RATE = 0.01
GENERATIONS = 50

# Define colors for visualization
COLORS = {
    'not_infected': 'blue',
    'infected': 'red',
}

# Create initial population
population = [{'infected': False, 'genotype': random.uniform(0, 1)} for i in range(POPULATION_SIZE)]

# Infect one individual
population[0]['infected'] = True


# Run simulation for specified number of generations
for generation in range(GENERATIONS):
    # Calculate number of infected individuals in population
    num_infected = sum([1 for ind in population if ind['infected']])

    # Display current generation and number of infected individuals
    print(f"Generation {generation + 1}: {num_infected} infected")

    # Display % of population infected
    print(f"{num_infected / POPULATION_SIZE * 100}% of population infected")


    # Visualize population
    plt.clf()
    for ind in population:
        color = COLORS['infected'] if ind['infected'] else COLORS['not_infected']
        plt.scatter(ind['genotype'], random.uniform(0, 1), color=color)
    # Display % of population infected at the top right of the plot
    plt.title(f"Generation {generation + 1} || " + f"{num_infected / POPULATION_SIZE * 100}% of population infected")
    plt.xlabel("Genotype")
    plt.ylabel("Y-coordinate")
    plt.pause(0.05)

    # Apply genetic algorithm to create next generation
    new_population = []
    for i in range(POPULATION_SIZE):
        # Select parents randomly
        parent1 = random.choice(population)
        parent2 = random.choice(population)

        # Determine infection status of child based on parents' infection status
        if parent1['infected'] and parent2['infected']:
            child_infected = True if random.random() < INFECTION_RATE else False
        elif parent1['infected'] or parent2['infected']:
            child_infected = True
        else:
            child_infected = False
        
        child_genotype = (parent1['genotype'] + parent2['genotype']) / 2

         # Apply mutation rate to child genotype
        if random.random() < MUTATION_RATE:
            child_genotype += random.uniform(-0.1, 0.1)

        # Add child to new population
        new_population.append({'infected': child_infected, 'genotype': child_genotype})

    # Replace old population with new population
    population = new_population


# Display final generation and number of infected individuals
num_infected = sum([1 for ind in population if ind['infected']])

# Display % of population infected
print(f"{num_infected / POPULATION_SIZE * 100}% of population infected")



# Visualize final population
plt.clf()
for ind in population:
    color = COLORS['infected'] if ind['infected'] else COLORS['not_infected']
    plt.scatter(ind['genotype'], random.uniform(0, 1), color=color)
plt.title(f"Generation {GENERATIONS + 1}")
plt.xlabel("Genotype")
plt.ylabel("Y-coordinate")
plt.pause(0.1)

# Display plot
plt.show()
