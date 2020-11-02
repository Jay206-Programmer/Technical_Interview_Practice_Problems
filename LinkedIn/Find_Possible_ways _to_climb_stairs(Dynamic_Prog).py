# Asked In LinkedIn

# Problem: You are given a positive integer N which represents the number of steps in a staircase. 
# You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.

# Example: for 5 stairs Number of possible ways -> 8
#          How: 11111
#               1112
#               1121
#               1211
#               2111
#               221
#               212
#               122

#Try Solving in O(n) complexity.

# ! I have tried commenting using comment highlighting extension of vs code, download it to see comments in different colours.

# * Lets GO For the Good Old Recursive Way, Slow as hell but good for a start
def staircase(n):
    # Fill this in.
    
    # ? Base Cases
    if n == 0:
        return 1
    elif n ==1:
        return 1
    elif n == 2: 
        return 2
    
    # ? all the possible solutions for one stair at a time
    one_Stair_a_Time = staircase(n-1)
    # ? all the possible solutions for two stair at a time
    two_Stair_a_Time = staircase(n-2)
    
    return one_Stair_a_Time + two_Stair_a_Time

#print('For 4 staris, possible ways: ',staircase(4))
# ? Answer you should get 5
#print('For 5 staris, possible ways: ',staircase(5))
# ? Answer you should get 8

# * AHA recursion one works, lets make it a bit faster using Memory Stack.
def FasterStaircase():
        
    # ? Lets make a list that will remember steps,
    n = int(input('\nEnter the Number of Steps:'))

    Memory = [-1]*(n+1)
    Memory[0:3] = [1,1,2] # ? We Know it
    def Fsc(n):
        # ? Base Cases
        if n == 0:
            return 1
        elif n == 1:
            return 1
        elif n == 2: 
            return 2
        
        if Memory[n] == -1:
        # * We haven't already found the solution, lets do it    
        
            # ? all the possible solutions for one stair at a time
            one_Stair_a_Time = Fsc(n-1)
            # ? all the possible solutions for two stair at a time
            two_Stair_a_Time = Fsc(n-2)
            
            Memory[n] = one_Stair_a_Time + two_Stair_a_Time
            #print(Memory) # ? for Dynamic programming purpos
            return Memory[n]
        
        else:
        # * We have found the solution, lets take it directly from memory
            return Memory[n]    
        
    print('\nNumber of Possible Ways:', Fsc(n))

# Todo: Uncomment bellow functions
# FasterStaircase()
# FasterStaircase()

# * Still Not Satisfied?, lets summon the all mighty Dynamic Programming...

# Todo: Try printing the memory stack from the previous function and try finding some pattern in it.
# * For 5 -> [1, 1, 2, 3, 5, 8]
# * For 7 -> [1, 1, 2, 3, 5, 8, 13, 21]

# ? Found anything? sum of previous 2 numbers is next Number... BINGO!! Now you can solve this problem without any recursion.

# * Implementing Dynamic Algo:
def DynamicStaircase(n):
    
    Memory = [1,1]
    
    for i in range(2,(n+1)):
        Memory.append(Memory[i-2]+Memory[i-1])
        
    return Memory[n]

print('For 5 staris, possible ways: ',DynamicStaircase(5))
print('For 10 staris, possible ways: ',DynamicStaircase(10))

# * Okay! so we solved this problem in O(n) time complexity using Dynamic Programming.

# * Have a happy coding time!
