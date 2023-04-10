import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# Define parameters for the simulation
num_people = 1000
initial_infected = 5
mutation_rate = 0.01
num_iterations = 100
num_generations = 50
population_size = 100

# Initialize the population

# Global variables
population = np.zeros(num_people)
virus = {'infectivity': 0.5, 'lethality': 0.1, 'duration': 14}
evolved_virus = []
virus_generation = 0


population[:initial_infected] = 1

# Define the initial virus characteristics
virus = {
    'infection_rate': 0.3,
    'recovery_rate': 0.1,
    'death_rate': 0.01
}

# Define a function to simulate the spread of the virus
def simulate_step(population, virus):
    # Calculate the number of infected individuals in the population
    num_infected = np.sum(population == 1)

    # Calculate the number of susceptible individuals in the population
    num_susceptible = np.sum(population == 0)

    # Calculate the number of recovered individuals in the population
    num_recovered = np.sum(population == 2)

    # Calculate the probability of infection for each susceptible individual
    p_infection = virus['infection_rate'] * num_infected / num_susceptible

    # Calculate the probability of recovery for each infected individual
    p_recovery = virus['recovery_rate']

    # Calculate the probability of death for each infected individual
    p_death = virus['death_rate']

    # Create a new population array
    new_population = np.zeros_like(population)

    # Simulate each individual in the population
    for i, state in enumerate(population):
        if state == 0: # Susceptible
            if random.random() < p_infection:
                new_population[i] = 1 # Infected
            else:
                new_population[i] = 0 # Still susceptible
        elif state == 1: # Infected
            if random.random() < p_death:
                new_population[i] = 2 # Recovered (with immunity)
            elif random.random() < p_recovery:
                new_population[i] = 0 # Recovered (still susceptible)
            else:
                new_population[i] = 1 # Still infected
        else: # Recovered (with immunity)
            new_population[i] = 2 # Still recovered

    return new_population

# Define a function to evolve the virus
def evolve_virus(virus, num_generations, population_size, mutation_rate):
    # Initialize a population of viruses
    evolved_virus = [virus]
    viruses = [virus] * population_size

    # Iterate over each generation
    for i in range(num_generations):
        # Create a list to store the fitness of each virus
        fitness = []

        # Evaluate the fitness of each virus
        for v in viruses:
            # Simulate the spread of the virus with the current characteristics
            population = np.zeros(num_people)
            population[:initial_infected] = 1
            for j in range(num_iterations):
                population = simulate_step(population, v)

            # Calculate the fitness of the virus based on the number of infected individuals
            num_infected = np.sum(population == 1)
            fitness.append(num_infected)

        # Select the fittest viruses to mate and produce offspring
        fittest_viruses = [viruses[i] for i in np.argsort(fitness)[-population_size//2:]]

        # Create a list to store the offspring
        offspring = []

        # Generate offspring by mating the fittest viruses
        for j in range(population_size - len(fittest_viruses)):
            # Select two parent viruses
            parent1 = random.choice(fittest_viruses)
            parent2 = random.choice(fittest_viruses)

            # Combine the virus characteristics of the parents
            child_virus = {
                'infection_rate': (parent1['infection_rate'] + parent2['infection_rate'])/2,
                'recovery_rate': (parent1['recovery_rate'] + parent2['recovery_rate'])/2,
                'death_rate': (parent1['death_rate'] + parent2['death_rate'])/2
            }

            # Mutate the child virus
            if random.random() < mutation_rate:
                child_virus['infection_rate'] += np.random.normal(scale=0.01)
            if random.random() < mutation_rate:
                child_virus['recovery_rate'] += np.random.normal(scale=0.01)
            if random.random() < mutation_rate:
                child_virus['death_rate'] += np.random.normal(scale=0.01)

            # Add the child virus to the list of offspring
            offspring.append(child_virus)

        # Replace the old viruses with the offspring
        viruses = fittest_viruses + offspring

    # Return the final population of viruses
    return viruses

# Simulate the evolution of the virus
viruses = evolve_virus(virus, num_generations, population_size, mutation_rate)

# Define a function to update the plot with each iteration of the simulation
def update_plot(frame):
    global population, virus, evolved_virus, virus_generation

    # Update the population with one iteration of the simulation
    population = simulate_step(population, virus)

    # Update the plot with the new population
    healthy = np.sum(population == 0)
    infected = np.sum(population == 1)
    recovered = np.sum(population == 2)
    dead = np.sum(population == 3)
    ax.clear()
    ax.bar(['Healthy', 'Infected', 'Recovered', 'Dead'], [healthy, infected, recovered, dead])
    ax.set_ylim([0, num_people])

    # Check if the virus has evolved
    if frame > 0 and frame % num_iterations == 0:
        # Evolve the virus
        evolved_virus = evolve_virus(virus, num_generations, population_size, mutation_rate)
        virus_generation = num_generations
        virus = evolved_virus[0]
        print(f'Virus evolved to generation {len(evolved_virus)}')

    # Update the virus characteristics if it has evolved
    if virus_generation > 0:
        virus = evolved_virus[virus_generation-1]
        virus_generation -= 1

    # Stop the animation if everyone is healthy or everyone is dead
    if infected == 0 or (infected + recovered + dead) == num_people:
        return


# create an animation using funcanimation

fig, ax = plt.subplots()
anima = FuncAnimation(fig, update_plot, frames=num_iterations*num_generations, interval=100, repeat=False)
plt.show()
