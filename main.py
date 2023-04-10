import random

# Define the parameters of the genetic algorithm
POPULATION_SIZE = 100000
GENE_LENGTH = 10
MUTATION_RATE = 0.1
GENERATIONS = 100

# Define the possible genes (A, T, C, G)
GENES = ['A', 'T', 'C', 'G']

# Define the fitness function
def calculate_fitness(chromosome):
    # Define the fitness criteria
    CRITERIA = ['A', 'AA', 'AAA', 'AAAA']

    # Initialize the fitness score
    fitness = 0

    # Evaluate the fitness based on the chromosome
    for i in range(len(chromosome)):
        gene = chromosome[:i+1]
        if gene in CRITERIA:
            fitness += 1

    return fitness

# Define the crossover function
def crossover(parent1, parent2):
    # TODO: Define the crossover function to produce offspring
    # Define the crossover point
    crossover_point = random.randint(0, len(parent1)-1)

    # Combine the chromosomes of the parents at the crossover point
    child = parent1[:crossover_point] + parent2[crossover_point:]

    return child

# Define the mutation function
def mutate(chromosome):
    # Convert the chromosome to a list to allow mutation
    chromosome = list(chromosome)

    # Mutate the genes
    for i in range(len(chromosome)):
        if random.random() < MUTATION_RATE:
            # Choose a random replacement gene
            new_gene = random.choice(['A', 'B', 'C'])
            # Replace the gene in the chromosome
            chromosome[i] = new_gene

    # Convert the chromosome back to a string
    chromosome = ''.join(chromosome)

    return chromosome


# Generate the initial population
population = []
for i in range(POPULATION_SIZE):
    chromosome = ''.join(random.choice(GENES) for _ in range(GENE_LENGTH))
    population.append(chromosome)

# Define the function to generate a new population
def generate_population(size):
    """
    Generates a new population of random chromosomes.
    """
    population = []
    for i in range(size):
        chromosome = ''.join(random.choice(GENES) for _ in range(GENE_LENGTH))
        population.append(chromosome)
    return population

# Define a function to evolve the population through generations
def evolve_population(population, fitness_fn, crossover_fn, mutation_fn, generations, watch_fn=None):
    for generation in range(generations):
        # Calculate the fitness of each individual
        fitness_scores = [fitness_fn(chromosome) for chromosome in population]

        # Select the parents for reproduction
        parents = []
        for _ in range(len(population) // 2):
            parent1 = random.choices(population, weights=fitness_scores)[0]
            parent2 = random.choices(population, weights=fitness_scores)[0]
            parents.append((parent1, parent2))

        # Generate the offspring through crossover and mutation
        offspring = []
        for parent1, parent2 in parents:
            child = crossover_fn(parent1, parent2)
            child = mutation_fn(child)
            offspring.append(child)

        # Replace the old population with the new offspring
        population = offspring

        # Call the watch function if provided
        if watch_fn:
            watch_fn(population, generation)

    return population

# Define a watch function to print the population after each generation
def print_population(population, generation):
    print("Generation:", generation)
    print("Population:", population)

# Generate the initial population
population = generate_population(POPULATION_SIZE)

# Evolve the population through generations using the new abstraction
evolve_population(population, calculate_fitness, crossover, mutate, GENERATIONS, watch_fn=print_population)

# Select the fittest individual from the final population
best_chromosome = max(population, key=calculate_fitness)
print("The fittest individual is:", best_chromosome)