from itertools import chain, combinations


def greedy_search(n, c, p, w, M, cnt_cmp):
    z_g = 0
    sum_w = 0
    for x in M:
        sum_w += w[x]
    c_new = c - sum_w
    X = set()
    for j in range(n):
        cnt_cmp += 1
        if j not in M and w[j] <= c_new:
            z_g = z_g + p[j]
            c_new = c_new - w[j]
            X.add(j)
    return z_g, X, cnt_cmp


def powerset(iterable, k):
    lst = list(iterable)
    return list(chain.from_iterable(combinations(lst, r) for r in range(1, min(len(lst) + 1, k + 1))))


def s(n, c, p, w, k):
    cnt_cmp = 0
    z_h = 0
    X_h = set()
    items = [x for x in range(n)]
    subsets = powerset(items, k)
    for M in subsets:
        sum_w = 0
        for x in M:
            sum_w += w[x]
        cnt_cmp += 1
        if sum_w > c:
            continue
        z_g, X, cnt_cmp = greedy_search(n, c, p, w, M, cnt_cmp)
        sum_p = 0
        for x in M:
            sum_p += p[x]
        cnt_cmp += 1
        if z_g + sum_p > z_h:
            z_h = z_g + sum_p
            X_h = X | set(M)
    return z_h, X_h, cnt_cmp


def get_ans(w, items_c, items_w):
    z_h, X_h, cnt_cmp = s(len(items_c), w, items_c, items_w, len(items_c)//4)
    items_to_take = [1 if i in X_h else 0 for i in range(len(items_c))]
    items_weight = 0
    for x in X_h:
        items_weight += items_w[x]
    return z_h, items_weight, items_to_take, cnt_cmp
