# Format speciifiers = {value:flags} format a value based on what flag are inseted

# :.(number)f = round to that many decimal places (fixed point)
# :(number) = aloocate that many spaces
# :03 = allocated and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma seprator

'''
:.(number)f
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is {price1:.2f}")
print(f"Price 1 is {price2:.2f}")
print(f"Price 2 is {price3:.2f}")
'''

'''
:(number) 
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is {price1:.2f}")
print(f"Price 1 is {price2:.2f}")
print(f"Price 2 is {price3:.2f}")
'''
