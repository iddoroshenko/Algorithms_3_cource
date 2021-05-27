import random


def fit(dist, flows, ans):
    res = 0
    n = len(dist)
    for i in range(n):
        for j in range(n):
            res += dist[i][j] * flows[ans[i]][ans[j]]
    return res


def change_fit(dist, flows, ans, i, j, current_ans):
    n = len(flows)
    for x in range(n):
        current_ans -= dist[i][x] * flows[ans[i]][ans[x]]
        current_ans -= dist[j][x] * flows[ans[j]][ans[x]]
    ans[i], ans[j] = ans[j], ans[i]
    for x in range(n):
        current_ans += dist[i][x] * flows[ans[i]][ans[x]]
        current_ans += dist[j][x] * flows[ans[j]][ans[x]]
    return ans, current_ans


def init_base(n):
    ans = [x for x in range(n)]
    random.shuffle(ans)
    return ans


def local_search(dist, flows, base_ans):
    n = len(dist)
    ans = base_ans
    current_ans = fit(dist, flows, ans)

    dont_look = [0 for x in range(n)]
    i = 0
    while i < n:
        if dont_look[i] == 1:
            i += 1
            continue
        founded = False
        for j in range(i + 1, n):
            new_ans, new_current_ans = change_fit(dist, flows, ans.copy(), i, j, current_ans)
            if new_current_ans < current_ans:
                ans = new_ans
                current_ans = new_current_ans
                founded = True
                i = 0
                break
        if not founded:
            dont_look[i] = 1
        i += 1
    return ans, current_ans


def get_ans(dist, flows):
    ans = init_base(len(dist))
    return local_search(dist, flows, ans)
