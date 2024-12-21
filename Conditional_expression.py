'''Conditional expression = A one-line shortcut for th rif-else statement (ternary operator)
                            print or assign one or two values based on a condition 
                            x if condition else y '''

num = -6 
#print("Positive" if num > 0 else "Negative")

a = 6 
#print("Even" if a % 2 == 0 else "Odd")

b=7
max_num = a if a > b else b
min_num = a if a < b else b
print(max_num )
print(min_num )