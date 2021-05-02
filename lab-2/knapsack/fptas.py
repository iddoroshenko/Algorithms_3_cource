from .dp_by_cost import get_ans as dp_get_ans
from .two_approx import get_ans as two_approx_get_ans
from math import floor


def get_ans(w, items_c, items_w, E = 0.01):
    c_a2 = two_approx_get_ans(w, items_c, items_w)
    n = len(items_c)
    alpha = c_a2[0] * E / n
    new_items_c = [floor(items_c[i]/alpha) for i in range(n)]
    z, weight, ans, cnt_cmp = dp_get_ans(w, new_items_c, items_w)
    z_true = 0
    cnt_cmp += c_a2[3]
    for i in range(n):
        cnt_cmp += 1
        if ans[i] == 1:
            z_true += items_c[i]
    return z_true, weight, ans, cnt_cmp
