#* Asked in Microsoft

#? You 2 integers n and m representing an n by m grid, determine the number of ways you can get 
#? from the top-left to the bottom-right of the matrix y going only right or down.

#? Example:
#? n = 2, m = 2 

#? This should return 2, since the only possible routes are:
#? Right, down
#? Down, right.


#* Good Old Recursive way, slow but good for start
def num_ways(n, m):
    if n == 1 or m == 1:
        return 1
    
    else:
        count = 0
        count += num_ways(n-1,m)
        count += num_ways(n,m-1)
        
        return count

#* Using memory stack for faster execution
#* First create a function that creates hash and passes it to the function
def num_ways_hm(n,m):
    
    # Hash = [[0*m]*n] #! wrong 
    
    #!Note: We can create 2D array like [[0]*m]*n, 
    #! but under the hood python creates shallow arrays(Go on geeks for geeks for deep understanding)
    #! in which every multiplied value points to one single value which is fast & memory eff. but it will work weirdly in some situations
    #! Copy below 4 lines and Uncomment & execute them somewhere to see this weird phenomena(data structures) called shallow arrays in action
    #! Geeks for Geeks article link (https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/)

    #A = [[0]*3]*3
    #print(*A,sep='\n')
    #A[0][2] = 1
    #print(*A,sep='\n')

    #Creating arrays the right way, pretty slow, but we are using python so anyways... XD
    hash = [[0 for i in range(m+1)] for j in range(n+1)]
    return nw(n,m,hash)

def nw(n,m,hash):
    if not hash[n][m] == 0:
        return hash[n][m]
    else:
        if n == 1 or m == 1:
            hash[n][m] = 1
            #* print(*hash, sep='\n', end='\n\n') For Dynamic prog purpose
            return hash[n][m]
        
        else:
            hash[n][m] += nw(n-1,m,hash)
            hash[n][m] += nw(n,m-1,hash)
            #* Hmmm, Got any hints for dynamic programming from these 2 steps ???
            
            #* print(*hash, sep='\n', end='\n\n') For Dynamic Prog Purpose
            return hash[n][m]

#* Summoning the all mighty dynamic programing
#? From looking at the stack from above implementation, we can see that first row and first column will be initialized as 1 and every other-
#? element will be a sum of left and top element, lets implement that
def num_ways_dy(n,m):
    hash = [[1 for i in range(m)] for j in range(n)] #creating a 2D array of 1s
    
    for i in range(1,n):
        for j in range(1,m):
            hash[i][j] = hash[i-1][j] + hash[i][j-1]
            #? hash[i-1][j] = 0 The above element will not be needed again, so if you want to save some memory than uncomment this step 
    
    #* print(*hash, sep='\n', end='\n\n') Dynamicly created array, which will look similar to Recursively created stack  
    return hash[n-1][m-1]
    #* Through Dynamic programing we were able to solve this problem in O(nm) time complexity which will be lowest achievable among all the logics (I guess!!!)

# print(num_ways(2,2))
# #2

# print(num_ways(3,3))
# #6 => get a pen & paper and manually solve how it has 6 ways 

# print(num_ways(3, 4))
# # 10

#print(num_ways_hm(2,2))
#2

#print(num_ways_hm(3,3))
#6 

#print(num_ways_hm(3, 4))
# 10

print(num_ways_dy(3,3))
# 6

print(num_ways_dy(5,10))
#715

#* We Have implemented dynamic solution so lets go for some absurd grid ;)
#print(num_ways_dy(687,959))
#OUTPUT: 2376990657380170053335691334607333533984188811812145631345039134790343911332428159642142725013610144831574663950650791844562303940291288943131712399908785320572180121301527964878686469921472563748160377794556248126136438009091645386901302323125285511796001262231197322291699018878239824629596965126202851549969922822893518436959566965967970997767013243911713063425734204847252348410514703595845536361680009281489202826487766379681533036147234992632179195481815907027828023578917041920
#* Now try solving this grid using the first simple recursive function.. XDXD Kidding!!!