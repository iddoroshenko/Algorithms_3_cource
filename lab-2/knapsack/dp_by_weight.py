def get_ans(w, items_c, items_w):
    n = len(items_c)
    dp = []
    for i in range(n + 1):
        dp.append([0] * (w + 1))
    for i in range(1, n + 1):
        for k in range(1, w + 1):
            if k < items_w[i - 1]:
                dp[i][k] = dp[i - 1][k]
            else:
                dp[i][k] = max(dp[i - 1][k], dp[i - 1][k - items_w[i - 1]] + items_c[i - 1])
    items = [0 for i in range(n)]
    final_weight = [0]

    def get_items(k, s):
        if dp[k][s] == 0:
            return
        if dp[k - 1][s] == dp[k][s]:
            get_items(k - 1, s)
        else:
            get_items(k - 1, s - items_w[k - 1])
            items[k - 1] = 1
            final_weight[0] += items_w[k - 1]

    get_items(n, w)
    return dp[n][w], final_weight[0], items
