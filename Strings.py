# String methods
'''
name = input("Enter your full name: ")

result = len(name)             # length of the string
result = name.find("o")        # Index on which the letter in the "" avilable (first occurance)
result = name.rfind("o")       # Index on which the letter in the "" availableat the end (last occurance)
#name = name.capitalize()      # makes the first letter capital 
name = name.upper()            # makes the entire word upper case
name = name.lower()            # makes the entire word lower case
nmae = name.isdigits()         # accepts only digits
result = name.isalpha()        # accepts only alphabets
phone_number = input("Enter the phone number: ")     
result = phone_number.count("-")    #counts the elemnts from the ""
phone_number = phone_number.replace("-"," ")   # replaces the elements from the two "" , ""

print(name) 
'''
#print(help(str))

'''
validate user input exercise
1. username is no more than 12 characters
2. username must not contain spaces
3. usernmae must not contain digits
'''

'''
username = input("Enter a usernmae: ")

if len(username) >12:
    print("Usernmae cannot be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username cannot contain spaces")    
elif not username.isalpha():
    print("Your usernmae can only contain alphabets")    
else:
    print(f"Welcome {username}")   
'''

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#String Indexing = accesing elements of a sequence using [] (indexing operator)
#                  [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0])   #string start
print(credit_number[0:4]) #string start : end
print(credit_number[::3]) #every 3rd number from the string 
                          #bland space represents that we have considured a complete string 
                          #we can reverse the string with [::-1] we just have to give -1 to step 

                          