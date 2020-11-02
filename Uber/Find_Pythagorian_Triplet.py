# * Asked in Uber

# ? Problem: Given a list of numbers, find if there exists a pythagorean triplet in that list. 
# ? A pythagorean triplet is 3 variables a, b, c where a^2 + b^2 = c^2

# * Example: Input: [3, 5, 12, 5, 13]
# * Output: True
# ? Here, 5^2 + 12^2 = 13^2.

#! Slow solution, O(n^3) time complexity
#todo: Find a faster solution O(n^2) or O(n)
def findPythagoreanTriplets(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)):
            for k in range(len(nums)):
                if k != i and k != j:
                    if (nums[i]**2+nums[j]**2)**0.5 == nums[k]:
                        #print(nums[i],nums[j],nums[k])
                        return True
                    
    return False

print(findPythagoreanTriplets([12, 13, 5, 3]))
# True
