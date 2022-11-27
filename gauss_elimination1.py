from numpy import array, fabs, linalg, zeros

coff = array([
    [2,-1,3],
    [1,1,1],
    [1,-1,1]
], float)

b = array([9,6,2], float)

n = len(b)
x = zeros(n , float)

for k in range(n - 1):
    for i in range(k + 1 , n):
        factor = coff[k][k] / coff[i][k]
        for j in range(k ,n):
            coff[i][j] = coff[k][j] - factor * coff[i][j]
        b[i] = b[k] - factor * b[i]


print(coff)
print(b)

x[ n - 1] = b[n - 1] / coff[n - 1] [n - 1]

for i in range(n - 2 , -1, -1):
    sum_ax = 0
    for j in range(i+ 1, n):
        sum_ax += (coff[i][j]) * x[j]
    x[i] = (b[i] - sum_ax)/coff[i][i]

print(x)