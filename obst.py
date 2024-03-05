def obst(key, freq):
    n = len(key)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = freq[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j + 1):
                cost = sum(freq[i:j + 1]) + (dp[i][k - 1] if k > i else 0) + (dp[k + 1][j] if k < j else 0)
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][n - 1]

key = [10, 12, 20]
freq = [34, 8, 50]

print("Cost of optimal BST:", obst(key, freq))
