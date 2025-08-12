import random 
import math
import ga.genetic_algorithm as ga
from constants import POPULATION_SIZE, NUM_GENERATIONS
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
    for i in range(population_size):
        while True:
            chromosome = ""
            chromosome_weight = 0
            for j in range(len(data)):
                bit = random.randint(0,1)
                if bit == 1:
                    chromosome_weight += data[j][0]
                chromosome += str(bit)
            if chromosome_weight <= capacity:
                break
        population.append(chromosome)
        
    return population

def print_items(chromosome, score, data):
    pass

if __name__ == '__main__':
    capacity, data = load_data("data/data_knapsack01.txt")
    population = generate_initial_population(capacity, data, POPULATION_SIZE)
    #p1, p2 = ga.select_parents(capacity, data, population)
    #print(p1,p2)
    #print(ga.crossover(5, population[p1[0]], population[p2[0]] ))

    for i in range(NUM_GENERATIONS):
        # 1. check criterium
        # 2. if satisfied exit
        # 3. if not, move to new population
        population = ga.generate_population(capacity, data, population)

    print(population)
