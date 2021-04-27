import knapsack.dp as dp

if __name__ == '__main__':
    print('H', 'i', ' ', 'S', 'a', 's', 'h', 'a', ' ', 'a', 'n', 'd', ' ', 'A', 'n', 'y', 'a', sep='')
    p_c = []
    p_p = []
    p_s = []
    p_w = []
    for i in range(1, 8):
        p_c.append(open("benchmarks/p0" + str(i) + "_c.txt", "r"))
        p_p.append(open("benchmarks/p0" + str(i) + "_p.txt", "r"))
        p_s.append(open("benchmarks/p0" + str(i) + "_s.txt", "r"))
        p_w.append(open("benchmarks/p0" + str(i) + "_w.txt", "r"))
    w = int(p_c[0].read())
    items_c = []
    for line in p_p[0]:
        items_c.append(int(line))

    items_w = []
    for line in p_w[0]:
        items_w.append(int(line))

    print(dp.get_ans(w, items_c, items_w))
