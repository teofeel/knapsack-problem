import random 
import math
import copy
import ga.genetic_algorithm as ga
from collections import deque

from models.chromosome import Chromosome
from models.gene import Gene

from constants import POPULATION_SIZE, NUM_GENERATIONS, LAST_SCORES_LEN

# load data
def load_data(name):
    with open(name) as file:
        capacity_s = file.readline().strip()
        capacity = int(capacity_s.replace("capacity: ", ""))
        data = file.readlines()
        for i in range(len(data)):
            line = data[i].strip().split(",")
            line = [int(line[0]), int(line[1])]
            data[i] = line
        
    return capacity, data
        

# generate initial population
# population is consisted of 2+ chromosomes
# number of genes in chromosome is equal to length of dataset
# chromosome is consisted of randomly selected items from dataset whose total weight can fit in backpack
# max population size is 2^n (where n is length of dataset)
def generate_initial_population(capacity, data, population_size):
    population = []
    for _ in range(population_size):
        while True:
            genes = []
            chromosome_weight = 0
            for j in range(len(data)):
                bit = random.randint(0,1)

                if bit == 1:
                    chromosome_weight += data[j][0]

                gene = Gene(data[j][0], data[j][1], bit)
                genes.append(gene)

            if chromosome_weight <= capacity:
                break

        chromosome = Chromosome(genes)
        population.append(chromosome)
        
    return population

def print_items(chromosome, data, score):
    weight = 0
    for i in range(len(chromosome.genes)):
        if chromosome.genes[i].added == 1:
            print('Item:',data[i])
            weight += data[i][0]

    print('Total score:', score)
    print('Total weight:', weight)

if __name__ == '__main__':
    capacity, data = load_data("data/data_knapsack01.txt")
    population = generate_initial_population(capacity, data, POPULATION_SIZE)

    last_scores = deque()
    optimal = 0
    for i in range(NUM_GENERATIONS):
        # 1. check criterium
        parent1, parent2 = ga.select_parents(capacity, data, population)
        #print(parent1, parent2)


        # if parent score > optimal
        if parent1[1] >= optimal:
            optimal = parent1[1]

        # add scores to the list
        last_scores.append((parent1[1], parent2[1]))
        if(len(last_scores)>LAST_SCORES_LEN):
          last_scores.popleft()
      
        # 2. if satisfied exit
        if ga.criteria(last_scores, LAST_SCORES_LEN) or i==NUM_GENERATIONS:
            break

        # 3. if not, move to new population
        chromosome1 = copy.deepcopy(population[parent1[0]])
        chromosome2 = copy.deepcopy(population[parent2[0]])
        del population
        population = ga.generate_population(chromosome1, chromosome2)

    if not isinstance(parent1, Chromosome) or not isinstance(parent2, Chromosome):
        chromosome1 = population[parent1[0]]
        chromosome2 = population[parent2[0]]

    print_items(chromosome1, data, parent1[1])
