def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp_path = [[''] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
        dp_path[i][0] = 'u'

    for j in range(n + 1):
        dp[0][j] = j
        dp_path[0][j] = 'l'

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
                dp_path[i][j] = 'd'
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                if dp[i][j] == dp[i - 1][j] + 1:
                    dp_path[i][j] = 'u'
                elif dp[i][j] == dp[i][j - 1] + 1:
                    dp_path[i][j] = 'l'
                else:
                    dp_path[i][j] = 'c'

    print("Edit distance matrix:")
    for row in dp:
        print(row)

    print("Alignment:")
    alignment = get_alignment(dp_path, word1, word2, m, n)
    print(alignment)

def get_alignment(dp_path, word1, word2, i, j):
    if i == 0 and j == 0:
        return ""
    elif dp_path[i][j] == 'd':
        return get_alignment(dp_path, word1, word2, i - 1, j - 1) + word1[i - 1] + word2[j - 1]
    elif dp_path[i][j] == 'u':
        return get_alignment(dp_path, word1, word2, i - 1, j) + word1[i - 1] + ' '
    elif dp_path[i][j] == 'l':
        return get_alignment(dp_path, word1, word2, i, j - 1) + ' ' + word2[j - 1]
    else:
        return ""

# Example usage
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")
edit_distance(word1, word2)
