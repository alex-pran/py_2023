message = "I am variable value and can be changed"

print(message)
print('Second' + message)

num1 = 25
num2 = 30.45 #float
status = True

print('data type ', type(message))  #you can concatenate (join multiple text)
print('data type ', type(num1))
print('data type ',type(num2))
print('data type ',type(status))

print('data type ' + str(num1))  #here str() function converts int to string, then cancatenate strings

# fstring - format-string
print(f"Value of the num1 variable: {num1} .")
print(f"num1 multiplied by 50: '{num1 * 50}' .")

num3 = f"num1 multiplied by 50: '{num1 * 50}' ."  #text
num4 = "num1 multiplied by 50:", num1, 45, True
print(num3)
print(num4)

print("###########################\n\n\n")

###### Working with String values ###########
# tittle()
# lower()
# upper()

print(message.title())
print(message.upper())
print(message.lower())


print("#####################\n\n\n")

msg2 = '     python     '

print(msg2.rstrip())
print(msg2.lstrip())
print(msg2.strip())

num5 = '25'
num6 = '25.65'
print(num5 + ' 10')
print(int(num5) + 10) #convert integer, int()
print(float(num6) + 10) #convert float, float()

print(f"Result: {num5} + 10\n\n")


# Addition of number
num1 = 36
num2 = 21
print(f"Number we have: \nNum1 = {num1} and num2 = {num2} \n")
print(f"Addition of number: {num1 + num2}")
print({num1 - num2})
print({num1 * num2})
print({num1 / num2})
print(f" Roundede value: {round(num1 / num2, 5)}")

print("********* # in Python: // (floor division, % (modulo) **************")
print(f"Floor division of number: {num1 // num2}")
print(f"Floor division of number: {num1 % num2}")
