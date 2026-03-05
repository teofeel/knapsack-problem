## Genetic Algorithm for the 0/1 Knapsack Problem

This project implements a Genetic Algorithm (GA) to solve the classic 0/1 Knapsack Problem. The goal is to select a subset of items with given weights and values to maximize the total value without exceeding the knapsack's weight capacity

## Features
- Initial Population Generation: Creates a valid initial population where every individual (chromosome) respects the weight constraint
- Elitism Selection: The two best-performing individuals are automatically passed to the next generation
- Single-Point Crossover: Combines genetic material from parents to create offspring
- Mutation: Randomly flips bits (genes) in the offspring to maintain genetic diversity and prevent local optima
- Convergence Monitoring: Uses a deque to track scores over generations and stops early if the solution plateaus

## Genetic Algorithm Workflow
### 1. Fitness Function
The fitness is calculated as the sum of the valeus of all items included in the knapsack. If the total weight exceeds the capacity, the fitness is returned as 0 (invalid solution)
### 2. Selection
The algorithm uses an Elitism strategy. It identifies the two chromosomes with the highest fitness scores to act as parents for the next generation
### 3. Crossover
New offspring are created by picking a random split_index and swapping the bitstrings of the two parents
### 4. Mutation
A subset of the population is mutated based on the PROBABILITY_MUTATION. A random gene (bit) in a chromosome is flipped ($0 \to 1$ or $1 \to 0$)
