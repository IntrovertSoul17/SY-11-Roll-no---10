weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

def knapsack_top_down(n, capacity, memo):

    if n == 0 or capacity == 0:
        return 0

    if (n, capacity) in memo:
        return memo[(n, capacity)]

    if weights[n - 1] > capacity:
        memo[(n, capacity)] = knapsack_top_down(
            n - 1, capacity, memo
        )
    else:
        take = values[n - 1] + knapsack_top_down(
            n - 1,
            capacity - weights[n - 1],
            memo
        )

        skip = knapsack_top_down(
            n - 1, capacity, memo
        )

        memo[(n, capacity)] = max(take, skip)

    return memo[(n, capacity)]

def knapsack_bottom_up():

    n = len(weights)

    dp = [[0 for j in range(capacity + 1)]
          for i in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:

                take = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                skip = dp[i - 1][w]

                dp[i][w] = max(take, skip)

            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


memo = {}

top_result = knapsack_top_down(
    len(weights), capacity, memo
)

bottom_result = knapsack_bottom_up()

print("Weights:", weights)
print("Values:", values)
print("Capacity:", capacity)

print("\nTop-Down Result:", top_result)
print("Bottom-Up Result:", bottom_result)