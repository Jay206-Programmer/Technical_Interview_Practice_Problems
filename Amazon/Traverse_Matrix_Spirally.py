
#* Asked in Amazon

#? You are given a 2D array of integers. Print out the clockwise spiral traversal of the matrix.

#! Example:

#? grid = [[1,  2,  3,  4,  5],
#?         [6,  7,  8,  9,  10],
#?         [11, 12, 13, 14, 15],
#?         [16, 17, 18, 19, 20]]

#! The clockwise spiral traversal of this array is:

#? 1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12

def matrix_spiral_print(M):

    #? EndCases(Cases where our Function acts different) => No value, Row Of Elements , Single Value , Columns of Elements
    
    #? No value    
    if len(M) == 0: return
    
    #? Single Value
    elif len(M) == 1 and len(M[0]) == 1:
      print(M[0][0])
      return
    
    #? Row of Values
    elif len(M) == 1:
      for i in M:
        print(i)
        return
    
    #? Columns of values
    elif len(M[0]) == 1:
      for i in M:
        print(i[0])
        return
    
    #? Traversing
    
    #? Lft to Rght
    i = 0
    j = 0
    while i < len(M[0]):
      print(M[j][i])
      i+=1
    else: i-=1
    
    #? Top to Btm
    j += 1
    while j < len(M):
      print(M[j][i])
      j+=1
    else: j-=1
    
    #? Rght to Lft
    i -= 1
    while i >= 0:
      print(M[j][i])
      i-=1
    else: i+=1
    
    #? Btm to Top
    j -= 1
    while j > 0:
      print(M[j][i])
      j-=1
    else: j+=1
    
    #? Recursion: Giving inner array
    
    M = M[1:-1]
    for i in range(len(M)):
      M[i] = M[i][1:-1]
    
    matrix_spiral_print(M)
    
    return 

grid = [[1, 2, 3, 4, 5],
        [16,17,18,19,6],
        [15,24,25,20,7],
        [14,23,22,21,8],
        [13,12,11,10,9]
        ]
        
matrix_spiral_print(grid)
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25