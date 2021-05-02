import knapsack.dp_by_weight as dp_by_weight
import knapsack.dp_by_cost as dp_by_cost
import knapsack.ptas as ptas
import knapsack.two_approx as two_approx
import knapsack.fptas as fptas
import knapsack.branch_and_bound as branch_and_bound
import time
TRY = 10

def test(test_num):
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

    print("true result:", (c_true, w_true, items_true))

    time_ = 0
    for tries in range(TRY):
        start = time.time()
        res = dp_by_weight.get_ans(w, items_c, items_w)
        stop = time.time()
        time_ += stop - start
    print("dp_by_weight\nans:", res[:3], "number of comparisons:", res[3])
    print('Time:', time_/TRY)

    time_ = 0
    for tries in range(TRY):
        start = time.time()
        res = dp_by_cost.get_ans(w, items_c, items_w)
        stop = time.time()
        time_ += stop - start
    print("dp_by_cost\nans:", res[:3], "number of comparisons:", res[3])
    print('Time:', time_/TRY)


    time_ = 0
    for tries in range(TRY):
        start = time.time()
        res = ptas.get_ans(w, items_c, items_w)
        stop = time.time()
        time_ += stop - start
    print("ptas\nans:", res[:3], "number of comparisons:", res[3])
    print('Time:', time_/TRY)

    time_ = 0
    for tries in range(TRY):
        start = time.time()
        res = two_approx.get_ans(w, items_c, items_w)
        stop = time.time()
        time_ += stop - start
    print("2_approx\nans:", res[:3], "number of comparisons:", res[3])
    print('Time:', time_/TRY)

    time_ = 0
    for tries in range(TRY):
        start = time.time()
        res = fptas.get_ans(w, items_c, items_w)
        stop = time.time()
        time_ += stop - start
    print("fptas\nans:", res[:3], "number of comparisons:", res[3])
    print('Time:', time_/TRY)

    time_ = 0
    for tries in range(TRY):
        start = time.time()
        res = branch_and_bound.get_ans(w, items_c, items_w)
        stop = time.time()
        time_ += stop - start
    print("branch_and_bound\nans:", res[:3], "number of comparisons:", res[3])
    print('Time:', time_/TRY)


if __name__ == '__main__':
    p_c = []
    p_p = []
    p_s = []
    p_w = []
    for i in range(1, 8):
        p_c.append(open("benchmarks/p0" + str(i) + "_c.txt", "r"))
        p_p.append(open("benchmarks/p0" + str(i) + "_p.txt", "r"))
        p_s.append(open("benchmarks/p0" + str(i) + "_s.txt", "r"))
        p_w.append(open("benchmarks/p0" + str(i) + "_w.txt", "r"))

    for i in range(7):
        test(i)
        print()
