#Postfix expression into a Prefix 

def postfix_to_prefix(postfix):
    stack = []
    for char in postfix:
        if char.isalnum(): # helps us separate operands from operators
            stack.append(char) 
        else: 
            op1 = stack.pop()  
            op2 = stack.pop()  
            new_expr = char + op2 + op1
            stack.append(new_expr)
    return stack[-1]

postfix_expr = "AB+C*"
print("Prefix:", postfix_to_prefix(postfix_expr))
