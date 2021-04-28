import scipy
def get_ans(w, items_c, items_w):
    n = len(items_c)
    C = sum(items_c)
    dp = []
    for i in range(n + 1):
        dp.append([w+1] * (C + 1))
    dp[0][0] = 0
    for j in range(1, n + 1):
        for k in range(1, C + 1):
            if k < items_c[j - 1]:
                dp[j][k] = dp[j - 1][k]
            else:
                dp[j][k] = min(dp[j - 1][k], dp[j - 1][k - items_c[j - 1]] + items_w[j - 1])


    items = [0 for i in range(n)]
    final_weight = [0]

    def get_items(k, s):
        if dp[k][s] == 0:
            return
        if dp[k - 1][s] == dp[k][s]:
            get_items(k - 1, s)
        else:
            get_items(k - 1, s - items_c[k - 1])
            items[k - 1] = 1
            final_weight[0] += items_w[k - 1]

    best_c = -1
    for i in range(C, -1, -1):
        if dp[n][i] < w + 1:
            best_c = i
            break
    get_items(n, best_c)

    return best_c, final_weight[0], items
