
def determine(mat):
    result = mat[0][0] * (mat[1][1] * mat[2][2] - mat[2][1]* mat[1][2]) - mat[0][1]*(mat[1][0] * mat[2][2] - mat[2][0] * mat[1][2]) + mat[0][2] * (mat[1][0] * mat[2][1] - mat[1][1]*mat[2][0])

    return result

def crammer_matrix(mat):

    determine_of_matrix = determine(mat)

    dx = [
        [mat[0][3],mat[0][1],mat[0][2]],
        [mat[1][3],mat[1][1], mat[1][2]], 
        [mat[2][3],mat[2][1],mat[2][2]]
    ]

    dy = [
        [mat[0][0],mat[0][3],mat[0][2]],
        [mat[1][0],mat[1][3], mat[1][2]], 
        [mat[2][0],mat[2][3],mat[2][2]]
    ]

    dz = [
        [mat[0][0],mat[0][1],mat[0][3]],
        [mat[1][0],mat[1][1], mat[1][3]], 
        [mat[2][0],mat[2][1],mat[2][3]]
    ]

    print("DX :", dx)
    print("DY :", dy)
    print("DZ :", dz)

    det_dx = determine(dx)
    det_dy = determine(dy)
    det_dz = determine(dz)

    x = det_dx / determine_of_matrix
    y = det_dy / determine_of_matrix
    z = det_dz / determine_of_matrix

    return [x, y , z]
   


def main():
    coff = []
    row = 3 
    col = 4
    for i in range(row):
        arr = []
        print("i : ", i)
        for j in range(col):
            n = float(input())
            arr.append(n)
        coff.append(arr)
    print(coff)
    print(crammer_matrix(coff))

   

if __name__=="__main__":
    main()
    
'''
 row 3 
 col 
 [
  [1, 2 , 3 , 4], 
  [5, 6 , 7 , 8],
  [9, 10, 11, 12]
  ]
'''