#* Asked in Twitter

#* Given a string with the initial condition of dominoes, where:

#? . represents that the domino is standing still
#? L represents that the domino is falling to the left side
#? R represents that the domino is falling to the right side

#* Figure out the final position of the dominoes. 
#? If there are dominoes that get pushed on both ends, the force cancels out and that domino remains upright.

#? Example:
#? Input:  ..R...L..R.
#? Output: ..RR.LL..RR

class Solution(object):
    def pushDominoes(self, dominoes):
        dominoes = list(dominoes)
        flag = True
        while flag:
            i = 0
            flag = False
            while i < len(dominoes)-1:
                if dominoes[i] == "R":
                    if dominoes[i+1] == '.' and i+2 < len(dominoes) and dominoes[i+2] == 'L':
                        if i+3<len(dominoes): 
                            i+=3
                        else: break
                    elif dominoes[i+1] == '.':
                        flag = True
                        dominoes[i+1] = 'R'
                        if i+3 < len(dominoes):
                            i+=3
                        else: break
                    else: i+=1
                    
                elif dominoes[i] == '.':
                    if dominoes[i+1] == 'L':
                        flag = True
                        dominoes[i] = 'L'
                        if i+2< len(dominoes): i+=2
                        else: break
                    else: i+=1
                else: i+=1
                
        return ''.join(dominoes)

print(Solution().pushDominoes('..R...L..R.'))
# ..RR.LL..RR
print(Solution().pushDominoes('...LR..L..R..L'))
# LLLLRR.L..RR.L
print(Solution().pushDominoes('R...LL..RR....L'))
# RR.LLL..RRRR.LL

