def longest_sequence(first, second):
    rows = len(first)
    cols = len(second)

    table = [[""] * cols for i in range(rows)]

    for i in range(rows):
        for j in range(cols):

            if first[i] == second[j]:
                if i == 0 or j == 0:
                    table[i][j] = first[i]
                else:
                    table[i][j] = table[i - 1][j - 1] + first[i]

            else:
                if i == 0:
                    table[i][j] = table[i][j - 1] if j > 0 else ""
                elif j == 0:
                    table[i][j] = table[i - 1][j]
                else:
                    table[i][j] = max(table[i - 1][j],
                                      table[i][j - 1], key=len)

    return table[rows - 1][cols - 1]


first = input("Enter first sequence: ")
second = input("Enter second sequence: ")

result = longest_sequence(first, second)

print("\nLongest Common Subsequence:", result)
print("Length of sequence:", len(result))