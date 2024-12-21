# While loop = execute some code WHILE some condition remains true
#              if we just give the condition as true we have to add the 'Break' at the end of the loop we can use if else statement there 
'''
name = input("Enter your name: ")

while name == "":
    print("You did not enter your name") 
    name = input("Enter your nmae: ")

print(f"Hello {name}")
'''

# For loop = executes a block of codea fixed number of times.
#            You can iterate over a range, string,  sequence, etc.

'''
for x in range(1, 21):    # (lower range , upper range , step)
    if x == 13:
        continue
    else:
        print(x)
'''

# Nested loop = A loop withiin another loop (outer, inner)
#               outer loop:
#                   inner loop:
rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use:")

for y in range(rows):
    for x in range(columns):
        if y == 0 or y == rows-1 or x == 0 or x == columns-1:
            print(symbol , end="")
        else:
            print(" " , end="")
    print()              