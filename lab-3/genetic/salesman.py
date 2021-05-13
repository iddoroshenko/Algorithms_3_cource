import random


def fitness_function(chromosome, edges_weight):
    ans = 0
    for i in range(len(chromosome)-1):
        ans += edges_weight[chromosome[i]][chromosome[i+1]]
    return ans


def get_ans(edges_weight):
    num_of_edges = len(edges_weight)
    num_of_chromosomes = 4000
    k = num_of_chromosomes // 4
    k = k // 4
    k *= 4
    chromosomes = []
    for i in range(num_of_chromosomes):
        chromosomes.append([])
        for j in range(num_of_edges):
            chromosomes[i].append(j)
        random.shuffle(chromosomes[i])

    fitness_results = []
    for i in range(num_of_chromosomes):
        tmp = fitness_function(chromosomes[i], edges_weight)
        fitness_results.append((i, tmp))
    fitness_results.sort(key=lambda x: x[1])

    random_list = [0 for i in range(num_of_chromosomes)]
    for i in range(k):
        random_list[i] = 1
    random.shuffle(random_list)

    chromosomes_selected = []
    for i in range(num_of_chromosomes):
        if random_list[i] == 1:
            chromosomes_selected.append((i, fitness_results[i]))

    chromosomes_selected.sort(key=lambda x: x[1])
    chromosomes_selected = chromosomes_selected[:len(chromosomes_selected)//2]

    for i in range(0, len(chromosomes_selected), 2):

        crossover_point1 = random.randint(0, num_of_edges - 2)

        crossover_point2 = random.randint(crossover_point1+1, num_of_edges)

        child1 = [-1 for i in range(num_of_edges)]

        child2 = [-1 for i in range(num_of_edges)]

        tmp1 = chromosomes[chromosomes_selected[i+1][0]][crossover_point2:] + chromosomes[chromosomes_selected[i+1][0]][:crossover_point1]
        tmp2 = chromosomes[chromosomes_selected[i][0]][crossover_point2:] + chromosomes[chromosomes_selected[i][0]][:crossover_point1]

        for j in range(crossover_point1, crossover_point2):
            child1[j] = chromosomes[chromosomes_selected[i][0]][j]
            child2[j] = chromosomes[chromosomes_selected[i+1][0]][j]
            if chromosomes[chromosomes_selected[i+1][0]][j] in tmp1:
                tmp1.remove(chromosomes[chromosomes_selected[i+1][0]][j])
            if chromosomes[chromosomes_selected[i][0]][j] in tmp2:
                tmp2.remove(chromosomes[chromosomes_selected[i][0]][j])

        child1[crossover_point2:] = tmp1[:num_of_edges - crossover_point2]
        child1[:crossover_point1] = tmp1[num_of_edges - crossover_point2:]

        child2[crossover_point2:] = tmp2[:num_of_edges - crossover_point2]
        child2[:crossover_point1] = tmp2[num_of_edges - crossover_point2:]

        if random.randint(1, 100) == 42:
            pointer1 = random.randint(0, num_of_edges - 1)
            pointer2 = random.randint(0, num_of_edges - 1)
            child1[pointer1], child1[pointer2] = child1[pointer2], child1[pointer1]

        if random.randint(1, 100) == 42:
            pointer1 = random.randint(0, num_of_edges - 1)
            pointer2 = random.randint(0, num_of_edges - 1)
            child2[pointer1], child2[pointer2] = child2[pointer2], child2[pointer1]

        chromosomes.append(child1)
        chromosomes.append(child2)

    for i in range(num_of_chromosomes, len(chromosomes)):
        tmp = fitness_function(chromosomes[i], edges_weight)
        fitness_results.append((i, tmp))
    fitness_results.sort(key=lambda x: x[1])

    return fitness_results[0][1], chromosomes[fitness_results[0][0]]

