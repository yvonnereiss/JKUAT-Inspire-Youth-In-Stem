first_name="yvonne"  #string
second_name="reiss"   #string
colour="blue"         #string
age=21                #integer
height=5.5            #float
weight=60             #integer
#print(first_name)
print(first_name, second_name, "likes the colour", colour, "and is", age, "years old. She is", height, "feet tall and weighs", weight, "kilograms.")

# operation in python 
#1.arithmatic operators
num1=20
num2=40
addition = num1 + num2
#print(addition)
print(addition)
subtraction = num1 - num2
#print(subtraction)
print(subtraction)
multiplication = num1 * num2
#2. comparison operators
print(num1 == num2)
print(num1!=num2) #true
print(num1<num2) #true
#3. logical operators
# and, or, not
print(num1<num2 and num1>num2) #false
print(num1<num2 or num1>num2) #true
print(not num1<num2) #false
#4. assignment operators
print(num1 -20)
#print(num1)
print(num1 *2)
#print(num1)
#5. identity operatorts
# is, is not
#print (num1 is not num2) #true
print(num1 is not num2) #true
#print(num1 is num2) #false
print(num1 is num2) #false
#6. conditional statements
# if, elif, else
if first_name=="yvonne":
    print("yes")
elif first_name=="reiss":
        print("no")
else:
            print("none")
if second_name=="reiss":
    print("yes")
elif second_name=="yvonne":
        print("no")
else:
            print("none")
#enter_name=(input("enter your name:"))
#enter_age=(input("enter your age:"))
if age>18:
    print("you are an adult")
if age<18:
    print("you are a child")
if age==18:
        print("you are a teenager")


    
