
# load data
def load_data(name):
    with open(name) as data:
        capacity_s = data.readline().strip()
        capacity = int(capacity_s.replace("capacity: ", ""))
        items = data.readlines()
        for i in range(len(items)):
            line = items[i].strip().split(",")
            line = [int(line[0]), int(line[1])]
            items[i] = line
        
    return capacity, items
        

# generate initial population
# population is consisted of 2+ chromosomes
# number of genes in chromosome is equal to length of dataset
# chromosome is consisted of randomly selected items from dataset whose total weight can fit in backpack
# max population size is 2^n (where n is length of dataset)
def generate_initial_population(data, population_size, capcity):
    pass

if __name__ == '__main__':
    print(load_data("data/data_knapsack01.txt"))