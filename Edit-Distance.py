# Take input strings from the user
s1 = input('Enter first string: ')
s2 = input('Enter second string: ')

# Initialize a matrix to store the edit distances
dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

# Fill the first row and column of the matrix
for i in range(len(s1) + 1):
    dp[i][0] = i
for j in range(len(s2) + 1):
    dp[0][j] = j

# Compute the edit distances using dynamic programming
for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

# Print the edit distance between s1 and s2
print('Edit distance:', dp[-1][-1])
