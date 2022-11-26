from numpy import array, fabs, linalg, zeros

'''
System Solution
x + y + z = 9
2x + 5y + 7z = 52
2x + y – z = 0
'''

coff = array([
    [2,-1,3],
    [1,1,1],
    [1,-1,1]
],float)
b = array([9,6,2], float)

n = len(b)
x = zeros(n, float)

print(linalg.solve(coff, b))

#Elimination
for k in range( n - 1):
    if(fabs(coff[k][k]) < 1.0e-12):
        for i in range(k+1, n):
            if(fabs(coff[i][k]) > fabs(coff[k][k])): 
                coff[[k,i]] = coff[[i,k]] # # A[k,:], A[k+1,:] = A[k+1,:], A[k,:]
                b[[k,i]] = b[[i,k]] # B[k],   B[k+1]   = B[k+1],   B[k]
                break
    
    for i in range(k+1, n):
        if(coff[i][k] == 0): continue
        factor = coff[k][k]/coff[i][k]
        #factor = coff[i][k] / coff[k][k]
        for j in range(k, n):
            coff[i][j] = coff[k][j] - coff[i][j] * factor
            #coff[i][j] = coff[i][j] - coff[k][j] * factor
        b[i] = b[k] - b[i] * factor
        #b[i] = b[i] - b[k] * factor

print(coff)
print(b)
# Back substitution
x[n - 1] = b[n - 1] / coff[n - 1][ n - 1]

for i in range(n - 2 ,-1, -1):
    sum_ax = 0
    for j in range(i+1, n):
        sum_ax += (coff[i][j]) * x[j]
    x[i] = (b[i] - sum_ax)/coff[i][i]

print(x)


