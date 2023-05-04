print("\n\n\n\n")

# this code is for square matrix multiplication

s = int(input("Size of square matrix: ")) 

matrix_a = []
matrix_b = []
matrix_ans = []

print("\nEnter values for matrix_a")
for i in range(s):
    matrix_a.append([0]*s)
    for j in range(s):
        val = int(input(f"matrix_a [{i}][{j}]:"))
        matrix_a[i][j] = val

print("\nEnter values for matrix_b")
for i in range(s):
    matrix_b.append([0]*s)
    for j in range(s):
        val = int(input(f"matrix_b [{i}][{j}]:"))
        matrix_b[i][j] = val


print("\nMultiplied matrix")
for i in range(s):
    matrix_ans.append([0]*s)
    for j in range(s):
        for k in range(s):
            matrix_ans[i][j] += matrix_a[i][k] * matrix_b[k][j]

for i in matrix_ans:
    for j in i:
        print(j, end=" ")
    print()

print("\n\n\n\n\n")