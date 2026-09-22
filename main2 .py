# numbers= []
# for number in range(2,11):
#     numbers.append(number)
# print(numbers)
# numbers = []
# for number in range(1, 6):
#     numbers.append(number)
# print(number)
# numbers = [number for number in range(1, 6)]
# print(numbers)


# numbers=[number for number in range(3,7)]
# print(numbers)


numbers=[]
for number in range(1,21):
    if number % 2 == 0:
        numbers.append(number)
print(numbers)


numbers=[number for number in range(20,40)if number %2 == 0 ]
print(numbers)


numbers= [number* number for number in range(2,13) if number%2 ==0]
print(numbers)

numbers=[number * number for number  in range(1,11)if number %2 != 0]
print(numbers)


numbers=["even"if number%2==0 else "odd" for number in range(1,11)]
print(numbers)



add = lambda a,b: a + b
print(add(10,20))

multiply=lambda  a,b: a * b
print(multiply(10, 10))

square= lambda number: number* number
print(square(17))

numbers = [1, 2, 3, 4] 
square= []
for number in numbers:
    square.append(number * number)
print(square)

numbers=[1,2,3,4]
square=map(lambda number: number * number, numbers)  
print(list(square))

numbers= [ 2 ,7,9,11]
square=map(lambda number:number* number, numbers)
print(list(square))

numbers = [5, 10, 15, 20] 
square=map(lambda number: number* 2,numbers)
print(list(square))


numbers=[1,2,3,2,4,5,1] 
unique= []
duplicates=[]
for number in numbers:
    if number in unique:
        if number not in duplicates:
            duplicates.append(number)
    else:
        unique.append(number)
print(duplicates)


numbers = [3, 8, 11, 14, 17, 20]
Result=filter(lambda number:number %2 ==0, numbers)
print(list(Result))

from functools import reduce
number= [1,2,3,4]
Result=reduce(lambda a,b:a+b,number)
print(Result)

# numbers=[22,33,6]
# result=reduce(lambda a,b:a+b,numbers)
# print(result)
# list=[12,24,36]
# result=reduce(lambda a,b: a+b,list)
# print(result)


numbers=[22,6]
result=reduce(lambda a,b:a*b,numbers)
print(result)
number=[78,3]
result=reduce(lambda a,b:a*b,number)
print(result)

from functools import reduce

numbers = [15, 42, 8, 31, 27]
result =reduce(lambda a,b: a if  a< b  else b ,numbers)
print(result)


number=[ 34,56,90,7]
result=reduce(lambda a,b:a if  a > b else b,number)
print(result)

number=[ 8,9,10,-1 ,-7,-22]
result=reduce(lambda a,b:a if a >b else b ,number)
print(result)

name=[ "Azan","Ali","Ahmad"]
marks=[90,80,87]
result=zip(name,marks)
print(list(result))


product=["iphone","samsung","google","ipad"]
sales= [225000,180000,100000,50000]
result=zip(product,sales)
print(list(result))


name=[ "Azan","Ali","Ahmad"]
marks=[99,89,67] 
for name,marks in zip(name,marks):
    print(name,marks)


product=["iphone","samsung","google","ipad"]
sales= [225000,180000,100000,50000] 
for product,sales in zip(product,sales):
    print(product,sales)

class student:
    def __init__(self,name,age, marks):
        self.name= name 
        self.age= age 
        self.marks= marks 

    def check_result(self):
        if self.marks>=50:
            print("pass")
        else:
            print("failed as a son ")

student1=student("Azan Malik", 18, 90)
print(student1.name,marks)
student2=student("Ali",22,75)
print(student2.name,marks)
student1.check_result()
student2.check_result()

class student:
    def __init__(self, name,age,marks):
        self.name=name 
        self.marks=marks
        self.age=age 
    def check_result(self):
        if self.marks>=60:
            print("pass")
        else:
            print("failed")
student1=student("Azan",18,90)
student1.check_result()


# class Animal:
#     def eat(self):
#         print("Animal is Eating")
# class dog(Animal):
#     def bark(self):
#         print("The Dog is barking ")
# animal1=dog()
# animal1.eat()
# animal1.bark()

# class Animal:
#     def __init__(self,name):
#         self.name= name
#     def eat(self):
#         print(self.name, "is eating food")
# class dog(Animal):
#     pass
# dog1=dog("beela")
# dog1.eat()


# class vehicle:
#     def __init__(self,brand):
#         self.brand =brand
#     def show_brand(self):
#         print(self.brand)
# class car(vehicle):
#     pass
# car1=car("Toyoto supra")
# car1.show_brand


# class vehicle:
#     def __init__(self,brand):
#         self.brand =brand
#     def show_brand(self):
#         print(self.brand)
# class car(vehicle):
#     def __init__(self,brand,model):
#         super().__init__(brand)
#         self.model= model
# car1=car("Toyoto ","supra")
# car1.show_brand()
# # print(car1.model)
# car1.model


class Vehicle:
    def show(self):
        print("Vehicle is running")


class Car(Vehicle):
    def show(self):
        print("Car is running")


car1 = Car()
car1.show()



# class Animal:
#     def sound(self):
#         print("Animal make sounds")
# class dog(Animal):
#     def sound(self):
#         super().sound()
#         print("dog is barking")
# animal1=dog()
# animal1.sound()


# class Animal:
#     def eat(self):
#         print("Animal is Eating")
# class Dog(Animal):
#     def sound(self):
#         print("Animal is barking")
# class puppy(Dog):
#     def play(self):
#        print("Puppy is playing ")
# puppy1=puppy()
# puppy1.eat()
# puppy1.sound()
# puppy1.play()




# class person:
#     def walk(self):
#         print("person can walk")
# class student(person):
#     def study(self):
#         print("students are studying")
# class collage_student(student):
#     def attend(self):
#         print("student attend the class")

# collge_student1=collage_student()
# collge_student1.walk()
# collge_student1.study()
# collge_student1.attend()



class person:
    def __init__(self,name ):
        self.name=name 
class student(person):
    def __init__(self, name,marks):
        super().__init__(name)
        self.marks= marks
student1=student("azan" ,90)
print(student1.name)
print(student1.marks)



class person:
    def __init__(self,name ):
        self.name=name 
class student(person):
    def __init__(self, name,marks):
        super().__init__(name)
        self.marks= marks
student1=student("azan" ,90)
print(student1.name)
print(student1.marks)

class vehicle:
    def __init__(self,name):
        self.name=name
class car(vehicle):
    def __init__(self, name ,model):
        super().__init__(name)
        self.model=model
car1= car("garande",2007)
print(car1.name)
print(car1.model)

class father:
    def car(self):
        print("father has a car")
class mother:
    def house(self):
        print("Mother has an house")
class child(father,mother):
    pass
child1=child()
child1.car()
child1.house()   



class teacher:
    def teach(self):
        print("teacher is teaching ")
class coach:
    def train(self):
        print("coach is traning")
class student(teacher, coach):
    pass 
student1=student()
student1.teach()
student1.train()

# this is a herichical inheritance
class Animal:
    def Eat(self):
        print("Animal is eating ")
class cat(Animal):
    def meow(self):
        print("The cat is meowing ")
class dog(Animal):
    def bark(self):
        print("The dog is barking ")
dog1=dog()
cat1=cat()

cat1.Eat()
cat1.meow()


class human:
    def drink(self):
        print("we drink water")
class man(human):
    def good(self):
        print(" mens are good ")
class women(human):
    def hard(self):
        print(" womens are strong")
man1 =man()
women1=women()
man1.drink()
man1.good()


class dog:
    def sound(self):
        print("dog bark ")
class cat:
    def sound(self):
        print("cat meow")
class cow:
    def sound(self):
        print("cow bow bow")
animals=[cat(),dog(),cow()]
for animal in animals:
    animal.sound()

class solider:
    def attack(self):
        print( "solider attack with weapon")
class archer:
    def attack(self):
        print("archer attack with bow ")
class player:
    def attack(self):
        print("player attack")
def start_attack(charater):
        charater.attack()


solider1= solider()
archer1=archer()
player1=player()

start_attack(solider1)
start_attack(archer1)
start_attack(player1)


class number:
    def __init__(self,value):
        self.value= value
    def __add__(self, other):
        return self.value + other.value
a=number(10)
b= number(30)
print(a+b)

class product:
    def __init__(self,price):
        self.price=price
    def __add__(self,other):
        return self.price + other.price 
p1=product(900)
p2=product(100)
print(p1 + p2)
number= [ 2,3,4,7]
count= 0
for number in number:
    if number %2 ==0:
        count=count + 1 
print(count)



class product:
    def __init__(self,price):
        self.price=price
    def __sub__(self,other):
        return self.price - other.price 
p1=product(900)
p2=product(800)
print(p1-p2)


class product:
    def __init__(self,price):
        self.price=price
    def __mul__(self,other):
        return self.price * other.price 
p3=product(900)
p4=product(2)
print(p3 * p4)


class product:
    def __init__(self,price):
        self.price=price
    def __eq__(self,other):
        return self.price==other.price 
p1=product(900)
p2=product(900)
p3=product(300)
print(p1==p2)
print(p2==p3)


class product:
    def __init__(self,price):
        self.price=price 
    def __mul__(self,other):
        return self.price * other.price
p1=product(90)
p2=product(10)
p3=product(9)

print(p1 * p2 )
print(p2 * p3)
print(p1 * p3)


class Product:
    def __init__(self, price):
        self.price = price

    def __gt__(self, other):
        return self.price > other.price


p1 = Product(900)
p2 = Product(810)
print(p1 > p2)

class student:
    def __init__(self,name ,marks):
        self.name=name 
        self.marks= marks
    def __str__(self):
        return f"{self.name} -Marks.{self.marks}"

s1=student("Azan",90)
print(s1)


class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks=marks
    def __str__(self):
        return f"{self.name} -Marks.{self.marks}"
    def __repr__(self):
        return f"{self.name} -Marks.{self.marks}"
s1=student("Malik",825)
print(s1)
print(repr(s1))

class bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
class student:
    def __init__(self,marks):
        self.__marks=marks
    def get_marks(self):
        return self.__marks
    def set_marks(self,marks):
        self.__marks=marks
s1 = student(90)
print(s1.get_marks())

s1.set_marks(95)

print(s1.get_marks())

class bank:
    def __init__(self,balance):
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def set_balance(self,balance):
        if balance>=0:
           self.__balance=balance
        else:
            print("balance cannot be negative")

account=bank(9000)

print(account.get_balance())
account.set_balance(-8000)
print(account.get_balance())

class bank:
    def __init__(self,balance):
        self.__balance= balance 
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,value):
        if value >=0:
            self.__balance=value
        else:
            print("balance cannot be negative")
a1=bank(1000)
print(a1.balance)
a1.balance= 2500
print(a1.balance)


class dog:
    def sound(self):
        print( "Dog is barking ")
class cat:
    def sound(self):
        print("Cat is meowing")
dog1=dog()
cat1=cat()

dog1.sound()
cat1.sound()

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog barks")

dog1 = Dog()
dog1.sound()

class Engine:
    def started(self):
        print("Engine started")
class car:
    def __init__(self):
        self.engine=Engine()
car1=car()
car1.engine.started()

class cpu:
    def run(self):
        print("CPU is running")


class computer:
    def __init__(self):
        self.cpu = cpu()


c1 = computer()
c1.cpu.run()

class pertrolengine:
    def start(self):
        print("petrol engine is strated ")
class electricengine:
    def start(self):
        print("electric engine is started")
class car:
    def __init__(self,engine):
        self.engine=engine
    def start(self):
       self.engine.start()
car1=car(pertrolengine())
car2=car(electricengine())

car1.start()
car2.start()

class student:
    course="python"
    @classmethod
    def show_course(cls):
        print(cls.course)

student.show_course()

class car:
    brand= "toyota"
    @classmethod
    def show_brand(cls):
        print(cls.brand)
car.show_brand()


class student:
    school= " Azan public school"
    @classmethod
    def change_school(cls,new_school):
        cls.school=new_school
student.change_school("Malik school")
print(student.school)

class employee:
    company= "Azan ffc"
    @classmethod
    def change_company(cls,new_company):
        cls.company=new_company

employee.change_company("Code with Malik")
print(employee.company)

word= input("enter the word: ")
reversed=""
for letter in word:
     reversed= letter + reversed
if word== reversed:
    print("pelidrome")
else:
    print("not pelidrome")

class student:
    total_student=0
    def __init__(self):
        student.total_student+=1
    @classmethod
    def show_total(cls):
        print(cls.total_student)
s1=student()
s2=student()
s3=student()
student.show_total() 


number=[1,33,5,6,88,98,45,67]
even=[]
odd=[]
for number in number:
    if number %2 ==0:
        even.append(number)
    else:
        odd.append(number)
print("even",even)
print("odd",odd)


numbers = [2, 5, 2, 8, 2, 10, 5]
search = int(input(" enter  the number "))
count= 0 
for number in numbers:
    if number == search:
        count= count+ 1
print(count)
