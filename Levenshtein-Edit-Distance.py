# Take input strings s1 and s2 from the user
s1 = input("Enter string s1: ")
s2 = input("Enter string s2: ")

# Initialize a matrix of zeros with dimensions (len(s1)+1) x (len(s2)+1)
matrix = [[0]*(len(s2)+1) for i in range(len(s1)+1)]

# Fill the matrix with the minimum weighted edit distances
for i in range(len(s1)+1):
    for j in range(len(s2)+1):
        if i == 0:
            matrix[i][j] = j
        elif j == 0:
            matrix[i][j] = i
        elif s1[i-1] == s2[j-1]:
            matrix[i][j] = matrix[i-1][j-1]
        else:
            matrix[i][j] = min(matrix[i-1][j-1] + 2, matrix[i][j-1] + 1, matrix[i-1][j] + 1)

# Print the final matrix and the Levenshtein weighted edit distance
print("Matrix:")
for row in matrix:
    print(row)
print("Levenshtein Weighted Edit Distance:", matrix[-1][-1])
