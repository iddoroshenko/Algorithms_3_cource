import genetic.knapsack as knapsack
import genetic.salesman as salesman
import math


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

    test_num = 0
    w = int(p_c[test_num].read())
    items_c = []
    for line in p_p[test_num]:
        items_c.append(int(line))

    items_w = []
    for line in p_w[test_num]:
        items_w.append(int(line))

    items_true = []
    w_true = 0
    c_true = 0
    for line in p_s[test_num]:
        items_true.append(int(line))
    for j in range(len(items_true)):
        if items_true[j] == 1:
            w_true += items_w[j]
            c_true += items_c[j]

    # for i in range(100):
    # print(knapsack.get_ans(w, items_c, items_w))

    file = open('benchmarks/a280.tsp', 'r')
    coord = []
    for line in file:
        coord.append((int(line.split()[1]), int(line.split()[2])))
    w = []
    for i in range(len(coord)):
        w.append([])
        for j in range(len(coord)):
            w[i].append(euclidean_distance(coord[i], coord[j]))
    for i in range(100):
        print(salesman.get_ans(w))
