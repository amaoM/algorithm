def main():
    N = int(input())
    W = int(input())
    weight = []
    value = []
    dp = [[0 for w in range(W + 1)] for _ in range(N + 1)]
    for i in range(N):
        w, v = map(int, input().split())
        weight.append(w)
        value.append(v)
    for i in range(N):
        for w in range(W + 1):
            if w >= weight[i]:
                dp[i + 1][w] = max(dp[i][w - weight[i]] + value[i], dp[i][w])
            else:
                dp[i + 1][w] = dp[i][w]
    print(dp)
    print(dp[N][W])

if __name__ == '__main__':
    main()