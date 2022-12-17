class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ('+','-','*','/')
        evaluate = 0
        num_stack = []
        def operation(num1,num2): 
            if tokens[i] == '+': 
                return num1 + num2
            elif tokens[i] == '-': 
                return num1 - num2
            elif tokens[i] == '/': 
                if num1 / num2 < 0 : 
                    return ceil(num1 / num2)
                else:
                    return num1 // num2
            else: 
                return num1 * num2
        
        for i in range(0,len(tokens)):
            if tokens[i] in operators: 
                evaluate = operation(num_stack[-2],num_stack[-1]) 
                num_stack.pop() 
                num_stack.pop()
                num_stack.append(evaluate) 
            else:
                num_stack.append(int(tokens[i])) 
            
        return num_stack[-1] 
