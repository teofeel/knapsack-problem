import random
import math
from constants import POPULATION_SIZE, PROBABILITY_MUTATION
# generate population
def generate_population(capacity, data, population):
    # 3. if not select new parents
    parent1_tuple, parent2_tuple = select_parents(capacity, data, population)
    parent1 = population[parent1_tuple[0]]
    parent2 = population[parent2_tuple[0]]

    new_population = [parent1, parent2]
    # 4. crossover
    new_population.extend(crossover(POPULATION_SIZE, parent1, parent2))
    # 5. mutate genes
    new_population = mutate_population(new_population,PROBABILITY_MUTATION)

    return new_population
    

# fitness function
def fitness(capacity, data, chromosome):
    weight = 0
    value = 0
    for i in range(len(chromosome)):
        if chromosome[i] == "1":
            weight += data[i][0]
            value += data[i][1]
    print(chromosome)
    print(weight)
    print(value)
    print("\n")
    if weight > capacity:
        return 0
    return int(value)


# select parents function
# pick two best if elitism choosen
def select_parents(capacity, data, population):
    max1 = (0, 0)
    max2 = (0, 0)
    for i in range(len(population)):
        score = fitness(capacity, data, population[i])
        if max1[1] < score:
            tmp = max1
            max1 = (i, score)
            max2 = tmp
        elif max2[1] < score:
            max2 = (i, score) 
    return max1, max2

# crossover function
# choose a random value which is less that lenght of dataset
# add parent1's genes up to that point to the new chromosome
# add parent2's genes from that point to the new chromosome
# offspring is created
def crossover(population_size, parent1, parent2):
    children = []

    for _ in range(population_size-2):
        split_index = random.randint(1, len(parent1)-2)
        coin = random.randint(0,1)

        print(split_index, coin)

        if coin==0:
            child = parent1[split_index:]
            child += (parent2[:split_index])
        else:
            child = parent2[split_index:]
            child += (parent1[:split_index])
        

        children.append(child)


    return children


# mutation function
# mutate only offsprings
# theres two ways to choose how many genes to mutate:
    # choose 1-2 genes of offspring and then move to next one
    # assign a random probability to every gene that determines if the gene will be mutated. Roll a dice for every gene and mutate it if lands within the probability
def mutate_chromosome(chromosome):
    index = random.randint(0, len(chromosome) - 1)
    if chromosome[index] == "0":
        chromosome = chromosome[:index]+"1"+chromosome[index+1:]
    else:
        chromosome = chromosome[:index]+"0"+chromosome[index+1:]
    return chromosome


def mutate_population(population, probability):
    n = math.ceil(len(population) * probability)
    for i in range(n):
        index = random.randint(2, len(population) - 1)
        population[index] = mutate_chromosome(population[index])

    return population


# criteria satisfied function
# criteria is satisfied when:
    # if new population score is simillar to the last ones after x number of repetitions
    # if the number of generation is reached
    # if has optained optimal  
def criteria(last_scores, gen_num, max_num_gen, optimal, population):
    pass

