# * Asked by Google

#* Given a mathematical expression with just single digits, plus signs, negative signs, and brackets, evaluate the expression. 
#* Assume the expression is properly formed.

# ? Example:
# ? Input: - ( 3 + ( 2 - 1 ) )
# ? Output: -4

def eval(expression, verbos = False):
    Num_stack = list()
    exp_stack = list()
    i = 0
    while i < len(expression):
        
        #? Maintaining Digits
        if expression[i].isdigit():
            count = i+1
            while count < len(expression) and expression[count].isdigit():
                count+=1
            Num_stack.append(int(expression[i:count]))
            i = count
        
        #? Maintaining expressions
        elif expression[i] == '+' or expression[i] == '-':
            exp_stack.append(expression[i])
            i+=1
        
        #? Traversing through brackets using recursion (Every equation in bracket will be considered as a new equation and will be solved saperately.)    
        elif expression[i] == '(':
            count = 1
            count_index = i+1
            while count>0:
                if expression[count_index] == '(': count+=1
                elif expression[count_index] == ')': 
                    count-=1
                count_index+=1
                
            #? Recursion function returns the resultant number of given equation(bracket) 
            Num_stack.append(eval(expression[i+1:count_index-1]))
            i = count_index
        
        else:
            i+=1
    
    #Todo: Give verbos true in function call to see how Recursion works
    if verbos: print(f'Before: Expression ( {expression} ) Number_stack is {Num_stack} and Expression_stack is {exp_stack} .')

    #? As told in the problem defintion, we assume that the given equation is Properly formatted.
    #? So the two cases in which 'number of expression' == 'number of Decimals' will be when there will be,
    
    #? 1) an expression in front of the first Value,example: [-(10) - (-2)] here there are 2 expressions ['-','-'] and 2 values (10,-2) 
    #! NOTE: we don't consider 2's "-" as an expression because the whole '-2' value will  be in Number_stack as an intiger  
    #? so in this case we have to multiply first element with the expression BEFORE SOLVING THE EQUATION
    
    #? 2) expression outside the brackets, example: - (10), here Num. of exp == Num. of values
    
    #? so below if statement takes care of that 
    if len(Num_stack) == len(exp_stack):
        exp = exp_stack.pop(0)
        if exp == '-':
            Num_stack[0] *= -1
    
    #? Simple Calculation step
    while len(Num_stack) > 1:
        Num2 = Num_stack.pop()
        Num1 = Num_stack.pop()
        
        exp = exp_stack.pop()
        if exp == '+':
            Num_stack.append(Num1+Num2)
        else:
            Num_stack.append(Num1-Num2)
    
    if verbos: print(f'After: Expression ( {expression} ) Number_stack is {Num_stack} and Expression_stack is {exp_stack} .')
    
    return Num_stack[0]


print('For expression:  - (3 + ( 2 - 1 ) ) \n')
print('Ans:',eval('- (3 + ( 2 - 1 ) )'),'\n')
# -4

print('For expression:  - (3-3) + ( 2 +24 ) - 10) \n')
print('Ans:',eval('- (3 - 3) + ( 2 + 24 ) - 10'),'\n')
# -16

print('For expression:  +(-(+(-(10+2000)-(-300))+100)) \n')
print('Ans:',eval('+(-(+(-(10+2000)-(-300))+100))'),'\n')
#1610 