import main
import math

def average(pop_size, num_gens, mutation_prob):
    # print("Population size: ", pop_size)
    # print("Max Generations: ", num_gens)
    # print("Mutation probability", mutation_prob)
    max_score = 0
    # total_gens = 0
    for i in range(50):
        score, weight_perc, gens = main.call_main(pop_size, num_gens, 30, mutation_prob)
        if score > max_score:
            max_score = score
        # total_gens += gens
    # average_score = total_score / 1
    # average_gens = total_gens / 1
    
    # print("Average score = ", average_score)
    # print("Average weight = ", average_weight, " \n")
    return max_score, gens

def best():
    sizes = [200]
    generations = [150]
    mutations = [0.05]
    best = [0, 0, 0, 0]
    for i in range(1):
        for j in range(1):
            for k in range(1):
                score, gens = average(sizes[i], generations[j], mutations[k])
                if score > best[0]:
                    best[0] = score
                    best[1] = sizes[i]
                    best[2] = generations[j]
                    best[3] = mutations[k]
    print("BEST SCORE = ", best[0])
    # print("POPULATION SIZE = ", best[1])
    # print("NUMBER OF GENERATIONS = ", best[2])
    # print("MUTATION PROBABILITY = ", best[3])
    print("GENERATIONS: ", gens)
    print("===========================")
    return best

if __name__ == "__main__":
    idk = [0,0,0,0]
    for i in range(1):
        bst = best()
        if bst[0] > idk[0]:
            idk = bst
    print("---------FINAL RESULTS----------\n")
    print("BEST SCORE = ", idk[0])
    print("POPULATION SIZE = ", idk[1])
    print("NUMBER OF GENERATIONS = ", idk[2])
    print("MUTATION PROBABILITY = ", idk[3])    
