from math import *

my_num=-5
character_name="Sarwar"
character_age = 22
is_male=True


print("Hello World")
print("      /|")
print("     / |")
print("    /  |")
print("   /   |")
print("  /____|")

print("My name is: "+ character_name.upper()+",")
#print(str(character_name.index("a")))
#print(str(character_name.replace("Sar","An")))
#print("My name is: "+ character_name[0]+",")
#print("Age: "+str(character_age)+ ".")
print("Age: "+repr(character_age)+ ".")
#print(-2.44+3.5)
#print(3*(4+5))
#print(10%3)

#print(abs(my_num))
#print(pow(3,2))
#print(min(3,2))
print(round(3.4))
print(floor(3.4))
print(ceil(3.4))
print(sqrt(36))


name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello "+name+"! and You are: "+age)


#tuples
#coordinates= ( 4,5 )
#coordinates= [( 4,5 ), (6,7), (50,40)]
#coordinates[0]=10
# Not Changeable #
#print(coordinates[1])


#conditions:



# def say_hi(name, age):
#     print("Hello "+name+"! You are "+age)
#
#
# say_hi("Mike", "24")
# say_hi("Steve","30")

#
# def cube(num):
#     return num*num*num
#
# result=cube(3)
# print(result)


# is_male = False
# is_tall = False
# if is_male and is_tall:
#     print("You are a male and tall")
# elif is_male and not(is_tall):
#     print("You are male but not tall ")
# elif is_tall and not(is_male):
#     print("You are not male but tall ")
# else:
#     print("You are not a male nor tall")

#Comparision:
#def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
#
# num1 = 3;
# num2 = 1;
# num3 = 5;
# print(max_num(num1,num2,num3))



#Calcultor:

#
# num1=float(input("Enter first number: "))
# op= input("Enter Operator: ")
# num2 = float(input("Enter Second number: "))
#
# if op == "+":
#     print(num1+num2)
# elif op== "-":
#     print(num1 - num2)
# elif op== "*":
#     print(num1 * num2)
# elif op== "/":
#     print(num1 / num2)
# else:
#     print("Invalid Operater")




#Dictionary: "Key": "Value"
#
# monthConversions = {
#     "Jan" : "January",
#     "Feb" : "February",
#     "Mar" : "March",
#     "Apr" : "April",
#     "May" : "May",
#     "Jun" : "June",
#     "Jul" : "July",
#     "Aug" : "August",
#     "Sep" : "September",
#     "Oct" : "October",
#     "Nov" : "November",
#     "Dec" : "December"
# }
#
# print(monthConversions.get("Jan","Not a Valid key"))



# #While Loop
#
# i=1
# while i <=10 :
#     print(i)
#     i+=1
#
#
# print("Done with loop")



#For Loop
#
# friends = ["Aminul" , "Taha", "Aspia"]

# for index in range(3,10) :
#     print(index)
# for index in range(len(friends)) :
#      print(friends[index])

# for index in range(5):
#     if index == 0:
#         print("Sarwar")
#     if index == 4:
#         print("Aminul")

# def raise_to_power(base_num, pow_num):
#     result =1
#     for i in range(pow_num):
#         result*=base_num
#     return result
#
#
# print(raise_to_power(3,4))

#Nested, 2D array

# number_grid= [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ]
#
# print(number_grid[1][2])

# for row in number_grid:
#     for column in row:
#         print(column)



#
# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter in "AEIOUaeiou":
#             translation= translation+ "g"
#         else:
#             translation = translation +letter
#     return translation
#
# print(translate(input("Enter a Phrase: ")))



# #Try/Except
#
# try:
#     number = int(input("Enter a number: "))
#     value = 10 / 0
#     print(number)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError:
#     print("Invalid Input.")


