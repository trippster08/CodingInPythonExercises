#This program will act as a calculator. It will ask the user for 2 # integers, and an operation to perform

operation = input ("Choose whether you want to add, subtract, multiply or divide:")
first_number = input ("Please enter the first number you wish to" + operation + ":")
second_number = input ("Please enter the second numberyou wish to" + operation + ":")
 
 if first_number.isnumeric() and second_number.isnumeric():
 	first_number = int(first_number)
 	second_number = int(second_number)

 	if operation == "add":
 		answer = first_number + second_number

 	elif operation == "multiply":
 		answer = first_number * second_number

 	elif operation == "subtract":
 		answer = first_number - second_number

 	else operation == "divide":
 		answer = first_number // second_number

else answer = print ("Your input was not valid.")

print answer
