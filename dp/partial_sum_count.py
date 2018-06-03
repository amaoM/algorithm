def main():
    N = int(input())
    A = int(input())
    V = list(map(int, input().split()))
    dp = [[0 for _ in range(A + 1)] for _ in range(N + 1)]
    dp[0][0] = 1

    for n in range(N):
        for a in range(A + 1):
            dp[n + 1][a] += dp[n][a]
            if a >= V[n]: dp[n + 1][a] += dp[n][a-V[n]]

    print(dp)
    print(dp[N][A])

if __name__ == '__main__':
    main()