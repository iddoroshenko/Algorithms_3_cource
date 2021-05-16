import genetic.knapsack as knapsack
import genetic.salesman as salesman
import math
import time


def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


if __name__ == '__main__':
    file = open('the_most_important_file_do_not_remove.txt')
    print(file.read())
    p_c = []
    p_p = []
    p_s = []
    p_w = []
    for i in range(1, 8):
        p_c.append(open("../lab-2/benchmarks/p0" + str(i) + "_c.txt", "r"))
        p_p.append(open("../lab-2/benchmarks/p0" + str(i) + "_p.txt", "r"))
        p_s.append(open("../lab-2/benchmarks/p0" + str(i) + "_s.txt", "r"))
        p_w.append(open("../lab-2/benchmarks/p0" + str(i) + "_w.txt", "r"))

    # for test_num in range(7):
    #     print(f"BENCHMARK p0{test_num+1}")
    #     w = int(p_c[test_num].read())
    #     items_c = []
    #     for line in p_p[test_num]:
    #         items_c.append(int(line))
    #
    #     items_w = []
    #     for line in p_w[test_num]:
    #         items_w.append(int(line))
    #
    #     items_true = []
    #     w_true = 0
    #     c_true = 0
    #     for line in p_s[test_num]:
    #         items_true.append(int(line))
    #     for j in range(len(items_true)):
    #         if items_true[j] == 1:
    #             w_true += items_w[j]
    #             c_true += items_c[j]
    #
    #     answers = []
    #     timeExecuted = 0
    #     for i in range(100):
    #         start = time.time()
    #         answers.append(knapsack.get_ans(w, items_c, items_w))
    #         timeExecuted += time.time() - start
    #     print(f"TIME: {timeExecuted/100}")
    #     bestResult = max(list(map(lambda x: x[1], answers)))
    #     print(f'COST: {bestResult}')
    #     for i in answers:
    #         if i[1] == bestResult:
    #             print(f'ITEMS: {i[0]}')
    #             break

    salesman_benchmarks = {'a280': open('benchmarks/a280.tsp', 'r').readlines(),
                           'att48': open('benchmarks/att48.tsp', 'r').readlines()[6:-1],
                           'bays29': open('benchmarks/bays29.tsp', 'r').readlines()[38:-1],
                           'ch150': open('benchmarks/ch150.tsp', 'r').readlines()[6:-1],
                           'fl417': open('benchmarks/fl417.tsp', 'r').readlines()[6:-1],
                           }

    for benchmark in salesman_benchmarks:
        coord = []
        for line in salesman_benchmarks[benchmark]:
            coord.append((float(line.split()[1]), float(line.split()[2])))
        w = []
        for i in range(len(coord)):
            w.append([])
            for j in range(len(coord)):
                w[i].append(euclidean_distance(coord[i], coord[j]))
        answers = []
        timeExecuted = 0
        for i in range(100):
            start = time.time()
            answer = salesman.get_ans(w)
            timeExecuted += time.time() - start
            answers.append(answer)

        print(f"BENCHMARK {benchmark}")
        print(f"TIME {timeExecuted/100}")
        bestResult = min(list(map(lambda x: x[1], answers)))
        print(f'BEST RESULT: {bestResult}')
        for i in answers:
            if i[1] == bestResult:
                print(f'PATH: {i[0]}')
                break
