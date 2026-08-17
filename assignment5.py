def find_lcs(a, b):
    m = len(a)
    n = len(b)

    dp = [[""] * (n + 1) for i in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + a[i - 1]

            else:
                if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]

    return dp[m][n]


x = input("Enter first sequence: ")
y = input("Enter second sequence: ")

answer = find_lcs(x, y)

print("Longest Common Subsequence:", answer)
print("Length:", len(answer))