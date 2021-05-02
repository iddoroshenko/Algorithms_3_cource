from scipy.optimize import linprog
from pulp import *
cnt_cmp = 0


def f(c, A_ub, b_ub, A_eq, b_eq, best_opt):
    global best_items
    global cnt_cmp
    res = linprog(c, A_ub, b_ub, A_eq, b_eq, bounds=(0, 1))
    opt = -res['fun']
    items = [round(x, 3) for x in res['x']]
    cnt_cmp += 1
    if opt < best_opt[0]:
        return
    for i in range(len(items)):
        cnt_cmp += 1
        if not round(items[i], 3).is_integer():
            A_eq_tmp = A_eq.copy()
            b_eq_tmp = b_eq.copy()
            A_eq_tmp.append([0 for x in range(len(items))])
            A_eq_tmp[-1][i] = 1
            b_eq_tmp.append(1)
            f(c, A_ub, b_ub, A_eq_tmp, b_eq_tmp, best_opt)
            b_eq_tmp[-1] = 0
            f(c, A_ub, b_ub,A_eq_tmp, b_eq_tmp, best_opt)
            return
    cnt_cmp += 1
    if opt > best_opt[0]:
        best_opt[0] = opt
        best_items = items
    return


def get_ans(w, items_c, items_w):
    # items_w[0] * x[0] + ... + items_w[n] * x[n] <= w
    # items_c[0] * x[0] + ... + items_c[n] * x[n] -> max
    # x[0] = 0
    # x[1] = 1
    # 0 * x1 + 0 * x2 + 1 * x3 ... = 1
    cnt_cmp = 0
    c = [-x for x in items_c]
    A_ub = [items_w]
    b_ub = [w]
    A_eq = [[0 for x in range(len(items_w))]]
    b_eq = [0]
    best_opt = [-1]
    f(c, A_ub, b_ub, A_eq, b_eq, best_opt)
    z = 0
    weight = 0
    items = [int(best_items[i]) for i in range(len(best_items))]
    for i in range(len(items)):
        cnt_cmp += 1
        if items[i] == 1:
            z += items_c[i]
            weight += items_w[i]
    return z, weight, items, cnt_cmp
