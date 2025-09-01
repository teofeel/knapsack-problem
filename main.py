import random 
import math
import ga.genetic_algorithm as ga
from collections import deque

# from constants import POPULATION_SIZE, NUM_GENERATIONS, LAST_SCORES_LEN
from constants import POPULATION_SIZE, NUM_GENERATIONS, LAST_SCORES_LEN, PROBABILITY_MUTATION

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
    while len(population) < population_size:
        chromosome = ""
        chromosome_weight = 0
        for j in range(len(data)):
            bit = random.randint(0,1)
            if bit == 1:
                chromosome_weight += data[j][0]
            chromosome += str(bit)
        if chromosome_weight <= capacity and chromosome not in population:
            population.append(chromosome)      
    return population

def calc_weight(chromosome, data, capacity):
    weight = 0
    for i in range(len(chromosome)):
        if chromosome[i] == '1':
        #   print('Item:',data[i])
            weight += data[i][0]
    weight_perc = weight / capacity * 100

    return weight_perc

    
def print_items(chromosome, data, score):
    weight = 0
    for i in range(len(chromosome)):
        if chromosome[i] == '1':
            print('Item:',data[i])
            weight += data[i][0]

    print('Total score:', score)
    print('Total weight:', weight)



def call_main(POPULATION_SIZE, NUM_GENERATIONS, LAST_SCORES_LEN, MUTATION_PROBABILITY):
    capacity, data = load_data("data/data_knapsack01.txt")
    population = generate_initial_population(capacity, data, POPULATION_SIZE)
    pop = 0

    last_scores = deque()
    optimal = 0
    for i in range(NUM_GENERATIONS):
        # 1. check criterium
        parent1, parent2 = ga.select_parents(capacity, data, population)

        #print(i)
        # if parent score > optimal
        if parent1[1] >= optimal:
            optimal = parent1[1]

        # add scores to the list
        last_scores.append((parent1[1], parent2[1]))
        if(len(last_scores)>LAST_SCORES_LEN):
            last_scores.popleft()
        
        # 2. if satisfied exit
        if ga.criteria(last_scores, LAST_SCORES_LEN) or i==NUM_GENERATIONS -1 :
            pop = i
            break

        # 3. if not, move to new population
        parent1 = population[parent1[0]]
        parent2 = population[parent2[0]]
        population = ga.generate_population(parent1, parent2, POPULATION_SIZE, MUTATION_PROBABILITY)

    chromosome1 = population[parent1[0]]
    
    weight_perc = calc_weight(chromosome1, data, capacity)

    print_items(chromosome1, data, parent1[1])
    return parent1[1], weight_perc, pop


if __name__ == '__main__':
   call_main(POPULATION_SIZE, NUM_GENERATIONS, LAST_SCORES_LEN, PROBABILITY_MUTATION)
   