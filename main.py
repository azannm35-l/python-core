# n= int(input(" enter the value:"))
# if n % 2 !=0:
#     print("weird")
# elif 2 <= n <= 5:
#     print ( " not weird ")
# elif 6<= n <=20:
#     print("weird")
# else:
#     print( " invalid value enter ")



# a=int(input ("enter  the value" ))
# b=int(input("enter the value "))

# n1=  a + b
# print (n1)

# n2= a - b
# print( n2)


# n3 =a * b
# print(n3)





# n = 5

# for i in range(0, 5):
#     square = i * i
#     print(square)

# def is_leap(year):
#     if year % 400 == 0:
#         return True

#     elif year % 100 == 0:
#         return False

#     elif year % 4 == 0:
#         return True

#     else:
#         return False

# for i in range (1,6):
#     print(i, end="7")
# numbers = [2,3,5,6,6]
# numbers.sort()

# numbers= list(set(numbers))

# if len(numbers) >= 2:
#         print(numbers[-2])


# num= int(input("enter your number: "))
# if num % 2==0:
#     print("positive")
# elif num < 0:
#     print ("negative")
# else:
#     (" the number is zero ")

# a= int(input("enter first number "))
# b= int(input("enter second number "))
# c=int(input("enter third number "))

# if a> b and a>c:
#     print ("max",a)
# elif b>a and b>  c:
#     print("max",b)
# elif c>b and c> a:
#     print("max",c)
# print( " the largest number is ",  )


# for i in range(10,0,-1):
#     print(i)

# n= int(input("enter  number "))
# total= 0

# for i in range(1, n +1):
    
#     total= total + i 
# print( total)


# numbers = [2, 7, 4, 9, 10, 13, 16, 21,34,22]  
# count= 0
# for  number in numbers:
#     if number % 2 == 0:
#         count= count +1 
# print(count)





# numbers = [2, 7, 4, 9, 10, 13, 16, 21,34,22,77]  
# count= 0
# for  number in numbers:
#     if number % 2 != 0:
#         count= count +1 
# print(count)



# numbers = [12, 45, 7, 89, 34, 23]
# largest=numbers[0]
# for number in numbers:
#     if number > largest:
#         largest = number
# print("largest=", largest)

# numbers = [12, 45, 7, 89, 34, 23]

# smallest = numbers[0]

# for number in numbers:
#     if number < smallest:
#         smallest = number

# print("smallest =", smallest)


# numbers = [12, 7, 5, 18, 21, 30, 9, 14]
# even= [ ]
# odd=[ ]
# for number in numbers:
#     if number % 2 == 0:
#         even.append(number)
#     else:
#         odd.append(number)
# print("even",even)
# print("odd",odd)



# numbers = [2, 5, 2, 8, 2, 10, 5]
# search = int(input(" enter  the number "))
# count= 0 
# for number in numbers:
#     if number == search:
#         count= count+ 1
# print(count)


# numbers = [2, 5, 8, 11, 14, 17, 20]
# total = 0

# for number in numbers:
#     if number % 2 ==0:
#         total = total + number
# print(total)
    
# numbers = [10, 20, 30, 40, 50]
# total= 0
# for number in numbers:
#     total = total + number 
# average=total/len(numbers)
# print(average)

# sentence= input("enter word = ")
# count= 0 
# for letter in sentence:
#     if letter in "a,e,i,o,u":
#         count= count + 1 
# print(count)



# word = input("enter word")
# reversed= ""
# for letter in word:
#     reversed= letter + reversed 
# print(reversed)




# word = input("Enter word: ")
# reversed= ""
# for letter in word:
#     reversed= letter + reversed
# if word== reversed:
#     print("palindrome")
# else: 
#     print( " not palindrome")



# students = {
#     "Ali": 85,
#     "Ahmed": 72,
#     "Usman": 91,
#     "Hamza": 68
# }

# # for name, marks in students.items():
# #     if marks>=80:
# #         print(name)
# highest= 0
# top_student= "" 
# for name, marks in students.items():
#     if marks> highest:
#         highest= marks 
#         top_student= name
# print("highest_mark=",highest)
# print("Top_student=",top_student)

# import calculator
# print(calculator.addition(11,4))
# # print(calculator.subtract(11,4))
# import calculator

# print(calculator)
# print(calculator.__file__)

# import calculator 

# print(calculator.addition(11, 4))
# print(calculator.subtract(11, 4))
# print(calculator.multiply(11, 4))

# from calculator import addition
# print(addition(22,2))

# from calculator import multiply
# print(multiply(44,2))


# import math
# user= int(input("enter your number="))
# result= math.sqrt(user)
# print(result)

numbers = [5, -2, 8, -7, 0, 12, -3, 9]
count= 0
for number in numbers:
    if number > 0:
        count= count + 1
print(count)

numbers = [5, -2, 8, -7, 0, 12, -3, 9]
count= 0
for number in numbers:
    if number < 0:
        count= count + 1
print(count)

numbers = [5, -2, 8, -7, 0, 12, -3, 9] 
total= 0
for  number in numbers:
    if number > 0:
        total = total + number 
print(total)


numbers = [10, 5, 20, 8, 15]
largest= numbers[0]
second  = numbers[0]
for number in numbers:
    if number > largest:
        second= largest 
        largest= number
print(largest)
print(second)


numbers = [10, 5, 20, 8, 15]

largest = numbers[0]
second = numbers[0]

for number in numbers:

    if number > largest:
        second = largest
        largest = number

    elif number < largest and number > second:
        second = number

print(second)

numbers = [2, 5, 2, 8, 5, 9, 8, 10]
unique= []
for number in numbers:
    if number not in unique:
        unique.append(number) 
print(unique)



numbers = [2, 7, 4, 9, 3, 8, 1, 6]
count = 0
for number in numbers:
    if number > 5:
        count= count + 1 
print(count)



numbers = [2, 7, 4, 9, 3, 8, 1, 6]
total = 0
for number in numbers:
    if number % 2== 0:
        total = total + number 
print(total)



numbers = [-4, 7, -2, 10, 0, -8, 5]
count=0
for number in numbers:
    if number> 0:
        count= count + 1 
print (count)

numbers = [4, 12, 7, 19, 3, 15] 
largest= numbers[0]
for number in numbers:
    if number > largest:
        largest= number
print(largest)


numbers = [14, 6, 22, 3, 18, 9]
smallest= numbers[0]
for number  in numbers:
    if number < smallest:
        smallest = number
print( smallest )


numbers = [5, -3, 8, -7, 2, -4, 10]
total= 0
for number in numbers:
    if number <0:
        total = total + number 
print(total)


numbers = [5, 0, 8, 0, -3, 7, 0, 2] 
count = 0
for number in numbers:
    if number == 0:
        count= count + 1 
print( count )

numbers = [10, 20, 30, 40, 50]
total = 0
for number in numbers:
    total= total+ number
    average= total/ len(numbers)
print(average)
for number in numbers:
    if number > average:
        print(number)

numbers = [3, 8, 11, 14, 17, 20, 25]

for number in numbers:
    if number % 2 != 0:
        print(number)


numbers = [2 ,4,5,6,8,3,44,66,77]
count= 0
for number in numbers:
    if number  % 2 == 0:
        count= count+ 1 
print( count)



numbers = [3, 8, 5, 11, 4, 7, 10] 
total= 0
for number in numbers:
    if number % 2 !=0:
        total= total + number 
print(total)


numbers = [5, 12, 18, 7, 15, 22, 10, 25] 
total= 0
for number in numbers:
    if number> 10 and number < 20:
        total= total + number 
print(total)


numbers = [5, 12, 18, 7, 15, 22, 10, 25] 
count =0
for number in numbers:
    if number> 10 and number < 20:
        count= count + 1 
print(count)


numbers = [5, 12, 18, 7, 15, 22, 10, 25] 
total = 0
for number in numbers:
    if number> 10 :
        total = total + number 
print(total)


word = "banana"
count = 0
for letter in word:
    if letter== "a":
        count = count + 1 
print (count)

word= "banana"
frequency={}

for letter in word:
    if letter in frequency:
        frequency[letter]= frequency[letter] + 1
    else:
        frequency[letter]= 1
print(frequency)


word = "programming"
frequency={}
for letter in word:
    if letter in frequency:
        frequency[letter]=frequency[letter]+1 
    else:
        frequency[letter]= 1
print(frequency)

students = {
    "Ali": 78,
    "Ahmed": 45,
    "Usman": 91,
    "Hamza": 32,
    "Bilal": 67
}
highest= 0
for name, marks in students.items():

    if marks >= 50:
        print(name, "Pass")
    else:
        print(name, "Fail")
    if marks > highest:
        highest = marks
print(highest)




# accounts = {
#     "Ali": 50000,
#     "Ahmed": 25000,
#     "Usman": 80000,
#     "Hamza": 15000
# }

# name= input( "enter the name: ")
# if name in accounts:
#     print( " existed ")
# else:
#     print( "not existed ")

# if name in accounts:
#     amount = int(input("Enter amount: "))
#     accounts[name] = accounts[name] + amount
#     print("newbalance", accounts[name])
# else:
#     print("account not found ")

# name= input( "enter the  account name : ")
# if name in accounts:
#     amount=int(input( " enter withdrawal   amount: "))
# if amount <= accounts[name]:
#     accounts[name]=accounts[name]- amount 
#     print("new balance",accounts[name] )
# else:
#     print( "insufficient balance ")



numbers = [12, -5, 8, 0, 15, -3, 8, 20, 0, 7]
total= 0
for number in numbers:
    if number > 0 :
        total = total + number
print(total)


numbers = [12, -5, 8, 0, 15, -3, 8, 20, 0, 7]
total= 0
for number in numbers:
    if number < 0 :
        total = total + number
print(total)

 

numbers = [12, -5, 8, 0, 15, -3, 8, 20, 0, 7]
count = 0
for number in numbers:
    if number == 0 :
        count = count + 1
print(count)



numbers = [12, -5, 8, 0, 15, -3, 8, 20, 0, 7]
largest= numbers[0]
for number in numbers:
    if number> largest: 
        laregst= number 
print(largest)

numbers = [12, -5, 8, 0, 15, -3, 8, 20, 0, 7]
smallest = numbers[0]
for number in numbers:
    if number <smallest: 
        smallest= number 
print(smallest)


numbers = [12, -5, 8, 0, 15, -3, 8, 20, 0, 7]
unique= []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)


numbers = [12, -5, 8, 0, 15, -3, 8, 20, 0, 7]
duplicates=[]
unique=[]
for number in numbers:
    if number in unique:
        duplicates.append(number)
    else:
        unique.append(number)

print(duplicates)

numbers = [8, 8, 8, 0, 0]
duplicates=[]
unique=[]
for number in numbers:
    if number in unique:
        if number not in duplicates:
            duplicates.append(number)
    else:
        unique.append(number)
print(duplicates) 

def add(a,b):
     return a + b

result = add(10,20)
print(result)


def calculate_grade(marks):
    if marks>= 90:
        return marks, "A"
    elif marks>= 80:
        return marks,"B"
    elif marks>= 70:
        return marks,"C"
    elif marks>= 60:
        return marks,"D"
    else:
        return marks,"fail"

result= calculate_grade(85)
print(result)

result= calculate_grade(50)
print(result)

def withdraw(balance, amount):
    if amount <= balance:
        return "withdraw allowed", balance - amount
    else:
        return " insufficient balance "

result= withdraw(8000, 9000)
print(result)



students = {
    "Ali": 78,
    "Ahmed": 45,
    "Usman": 91,
    "Hamza": 32
}
def check_student(students):

    for name, marks in students.items():

        if marks >= 80:
            return marks, name, "B"
        if marks >= 70:
            return marks, name, "C"
result= check_student(students)
print(result)


students = {
    "Ali": 78,
    "Ahmed": 45,
    "Usman": 91,
    "Hamza": 32
}
def get_grade(student):

    results={}
    for name, marks in student.items():
        if marks >= 90:
            grade= "A"
        if marks >= 80:
            grade= "B"
        if marks >= 70:
            grade= "C"
        if marks >= 60:
            grade= "D"
        else:
            grade= "f"
        results[name] =grade 
    return results
results= get_grade(students)
print(results)

numbers=[2,8]
total=0
for number in numbers:
    total = total + number
print(total)

def find_largest(number):
    largest= number[0]
    for number in numbers:
        if number > largest:
            largest = number
        
    return largest

numbers= [20,30,40,50]
result= find_largest(numbers)
print(result)

numbers=[0,1,22,22,4,4,7,9,8,9]
 
unique=[]
duplicates=[]
for number in numbers:
    if number in unique:
        duplicates.append(number)
    else:
        unique.append(number)
print(duplicates)



numbers=[0,1,22,22,4,4,7,9,8,9]
 
unique=[]
duplicates=[]
for number in numbers:
    if number not in duplicates:
        duplicates.append(number)
    else:
        unique.append(number)
print(duplicates)



numbers = [2, 5, 2, 8, 5, 2, 9]  
frequency= {}
for number in numbers:
    if number in frequency:
        frequency[number]=frequency[number]+ 1 
    else:
        frequency[number]= 1
print(frequency)

try:
    age=int(input("enter your age "))
    print(age) 
except:
    print("invalid statemnt")


try:
    numbers=int(input("enter your number"))
    print(numbers)
except ValueError:
    print("invalid number  ")

try:
    result = 10 / 0
    print(result)

except ZeroDivisionError:
    print("0 se divide nahi kar sakte")
finally:
    print("project finished")


try:
    age= int(input(" enter your age"))
    number= int(input(" enter your number "))
    print( age,number )
    result= number/age 
except ValueError:
    print( "invalid number")
except ZeroDivisionError:
    print( "cannot duvde by zero")

def add(*args):
    print(args)
add(10,20,30,40)

def user_info(**kwargs):
    print(kwargs)
user_info(name="Malik azan", age = 19, city="Ahmad pur east")

def test(*args, **kwargs):
    print(args)
    print(kwargs)

test(10, 20, name="Ali", age=20)



def student_info(*subjects,**details):
    print(subjects)
    print(details)
student_info(
    "python"
     "sql",
     "jengo",
name = "Azan",
age= 19
)

def class_info(*roommate, **classnumber):
    print(roommate)
    print(classnumber)
class_info(
    "room 1 ",
    "room 2 ",
    "room 3",
name= " saad",
age= 20,
)

name=["ahmad" "Mubeen" "awais"]
marks=[ 90,50,45]
result=zip(name,marks)
print(list(result))