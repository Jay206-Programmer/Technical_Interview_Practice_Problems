#* Asked in Amazon

#? You are given a 2D array of characters, and a target string. Return whether or not the word target word exists in the matrix. Unlike a standard word search, the word must be either going left-to-right, or top-to-bottom in the matrix.

#? Example:

#? [['F', 'A', 'C', 'I'],
#? ['O', 'B', 'Q', 'P'],
#? ['A', 'N', 'O', 'B'],
#? ['M', 'A', 'S', 'S']]

#? Given this matrix, and the target word FOAM, you should return true, as it can be found going up-to-down in the first column.

#! NOTE: I have implemented this code VERY poorly, try to make it Faster.

import numpy as np
import re
def word_search(matrix, word):
    
    #* creating a np array so that we can transpose
    matrix = np.array(matrix)
    for n,i in enumerate(zip(matrix.T)):
        
        #? Top to Bottem
        #* we can't get single elements from i(believe me I tried alot) so using RE to replace all not-needed chars with '' 
        string = re.sub('[^a-zA-Z]*','',str(*i))
        if word in string:
            return True
        
        #? Left to Right
        #* simply making string from list
        string = ''
        for j in matrix[n]:
            string+=str(j)
        if word in string:
            return True
        
    return False 
  
matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']]

print(word_search(matrix, 'BQP'))
# True
print(word_search(matrix, 'ASS'))
# True
print(word_search(matrix, 'FOAM'))
# True
print(word_search(matrix, 'Jay'))
# False
