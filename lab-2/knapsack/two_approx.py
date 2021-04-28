def max_greed(w, items_c, items_w):
    items = []
    n = len(items_c)
    for i in range(n):
        items.append((i, items_c[i], items_w[i]))
    items.sort(key=lambda x: x[1], reverse=True)
    ans = [0 for x in range(n)]
    z = 0
    w_ost = w
    for item in items:
        if w_ost > item[2]:
            w_ost -= item[2]
            ans[item[0]] = 1
            z += item[1]
    return z, w - w_ost, ans


def greedy(w, items_c, items_w):
    n = len(items_c)
    items = [(i, items_c[i] / items_w[i]) for i in range(n)]
    items.sort(key=lambda x: x[1], reverse=True)
    ans = [0 for x in range(n)]
    z = 0
    w_ost = w
    for item in items:
        if w_ost > items_w[item[0]]:
            w_ost -= items_w[item[0]]
            ans[item[0]] = 1
            z += items_c[item[0]]
    return z, w - w_ost, ans


def get_ans(w, items_c, items_w):
    z_1, w_1, ans_1 = max_greed(w, items_c, items_w)
    z_2, w_2, ans_2 = greedy(w, items_c, items_w)
    if z_1 > z_2:
        return z_1, w_1, ans_1
    else:
        return z_2, w_2, ans_2
