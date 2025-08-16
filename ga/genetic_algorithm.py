import random
import math
import copy

from constants import POPULATION_SIZE, PROBABILITY_MUTATION
from models.chromosome import Chromosome

# generate population
def generate_population(parent1, parent2):
    new_population = [parent1, parent2]
    # 4. crossover
    new_population.extend(crossover(POPULATION_SIZE, parent1, parent2))
    # 5. mutate genes
    new_population = mutate_population(new_population, PROBABILITY_MUTATION)

    return new_population
    

# fitness function
def fitness(capacity, data, chromosome):
    weight = 0
    value = 0
    for i in range(len(chromosome.genes)):
        if chromosome.genes[i].added == 1:
            weight += chromosome.genes[i].weight
            value += chromosome.genes[i].value
    #print(chromosome)
    #print('weight',weight)
    #print('value',value)
    #print("\n")
    if weight > capacity:
        return 0
    return int(value)


# select parents function
# pick two best if elitism choosen
# parent[0] - index in population
# parent[1] - score of chromosome
def select_parents(capacity, data, population):
    max1 = (0, 0)
    max2 = (0, 0)
    for i in range(len(population)):
        score = fitness(capacity, data, population[i])
        print(score)
        if max1[1] < score:
            tmp = max1
            max1 = (i, score)
            max2 = tmp
        elif max2[1] < score:
            max2 = (i, score) 

    print(max1, max2)
    return max1, max2

# crossover function
# choose a random value which is less that lenght of dataset
# add parent1's genes up to that point to the new chromosome
# add parent2's genes from that point to the new chromosome
# offspring is created
def crossover(population_size, parent1, parent2):
    children = []

    for _ in range(population_size-2):
        split_index = random.randint(1, len(parent1.genes)-2)
        coin = random.randint(0,1)

        if coin==0:
            child_genes = parent1.genes[split_index:].copy()
            child_genes += parent2.genes[:split_index].copy()
        else:
            child_genes = parent2.genes[split_index:].copy()
            child_genes += parent1.genes[:split_index].copy()
        
        child = Chromosome(child_genes)

        children.append(child)

    return children


# mutation function
# mutate only offsprings
# theres two ways to choose how many genes to mutate:
    # choose 1-2 genes of offspring and then move to next one
    # assign a random probability to every gene that determines if the gene will be mutated. Roll a dice for every gene and mutate it if lands within the probability
def mutate_chromosome(chromosome):
    index = random.randint(0, len(chromosome.genes) - 1)
    gene = chromosome.genes[index]
    gene.added = 1 - gene.added 



def mutate_population(population, probability):
    n = math.ceil(len(population) * probability)
    for i in range(n):
        index = random.randint(2, len(population) - 1)
        mutate_chromosome(population[index])

    return population


# criteria satisfied function
# criteria is satisfied when:
    # if new population score is simillar to the last ones after x number of repetitions
    # if the number of generation is reached
    # if has optained optimal  
def check_last_scores(last_scores, expected_len, tolerance=0.000001):
    if len(last_scores) < expected_len:
        return False
   
    scores_percentage1 = []
    scores_percentage2 = []

    for i in range(len(last_scores)-1):
        scores_percentage1.append(last_scores[i+1][0]/last_scores[i][0])
        scores_percentage2.append(last_scores[i+1][1]/last_scores[i][1])

        #print('optimal1', scores_percentage1, 'optimal2', scores_percentage2)

    scores1_same = 0
    scores2_same=0

    for i in range(len(scores_percentage1)-1):
        if abs(scores_percentage1[i] - scores_percentage1[i+1]) < tolerance:
            scores1_same+=1

        if abs(scores_percentage2[i] - scores_percentage2[i+1]) < tolerance:
            scores2_same+=1
    
    if scores1_same == scores2_same:
        return True
    

def criteria(last_scores, expected_len):
    if check_last_scores(last_scores, expected_len):
        return True
    
    return False

