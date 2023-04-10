# 🦠 Simple Pandemic Simulation using Genetic Algorithms

> **Note** 
>
> **This program is for educational purposes only. It is not intended to be used for medical or scientific research.**

![alttxt](https://github.com/asharahmed/pandemic-simulator/blob/main/newsrc.gif?raw=true)


This program simulates the spread of a pandemic using a genetic algorithm. The simulation represents a population of individuals, each with a genotype and an infection status. The genotype is a real number between 0 and 1, and determines the individual's susceptibility to infection. The infection status is a Boolean value, where `True` represents an infected individual and `False` represents a healthy individual.

## Simulation Parameters
The following parameters can be modified to customize the simulation:

`POPULATION_SIZE`: The number of individuals in the population.
`INFECTION_RATE`: The probability that an individual will become infected if exposed to the virus.
`MUTATION_RATE`: The probability that an individual's genotype will mutate during reproduction.
`GENERATIONS`: The number of generations to simulate.

## Visualization
The simulation includes a simple visualization of the population, where healthy individuals are represented by blue dots and infected individuals are represented by red dots. The size of the dot represents the individual's genotype, with larger dots indicating individuals that are more susceptible to infection.

## Running the Simulation
To run the simulation, simply run the `pandemic_simulation.py` file. The simulation will run for the specified number of generations and display the population visualization for each generation.

## Requirements
This program requires Python 3 and the following packages: matplotlib, and random.