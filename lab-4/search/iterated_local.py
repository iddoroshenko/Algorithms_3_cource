import random
from .two_opt import local_search, init_base

def stochastic_two_opt(ans, i, j):
    new_ans = ans[:i] + ans[j:i-1:-1] + ans[j+1:]
    return new_ans


def get_ans(dists, flows):
    ans, current_ans = local_search(dists, flows, init_base(len(dists)))
    count = 0
    n = len(dists)
    k = n // 2
    i = random.randint(0, n-2)
    j = max(i + random.randint(1, k), n-1)
    while count < 100:
        count += 1
        tmp_ans = stochastic_two_opt(ans, i, j)
        tmp_ans, new_ans = local_search(dists, flows, tmp_ans)
        if new_ans < current_ans:
            current_ans = new_ans
            ans = tmp_ans
            count = 0
    return ans, current_ans

