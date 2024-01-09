# class Amadin:
#     name= ""
#     age = 0

# Amadin1=Amadin()
# Amadin1.name="Vi"
# Amadin1.age=30

# Amadin2=Amadin()
# Amadin2.name="Serge"
# Amadin2.age=55

# print (f"{Amadin1.name} is {Amadin1.age} yeards old")
# print (f"{Amadin2.name} is {Amadin2.age} yeards old")

# class Anketa:
#     name=""
#     age=0
#     street=""
#     housenun=0

# anketa1=Anketa()
# anketa1.name= input('Ваше имя ')
# anketa1.age=input('Ваш возрост ')
# anketa1.street=input("ВВедите улицу ")
# anketa1.housenun=input('Ведите номер  дома ') 
# print (anketa1.age, anketa1.name)

# class Erik:
#     lenght=0
#     width=0
#     def calc(self):
#         print ("Erik=", self.lenght * self.width)
               
# Erik1=Erik()
# Erik1.lenght=14
# Erik1.width=14
# Erik1.calc()      

# class Erik:
#     def __init__(self,name=" ", age=""):
#         self.name=name
#         self.age=age
#         print(name, age)

# Erik1=Erik("Erik_D")        
# Erik1=Erik("Serge2") 
# Erik2=Erik("Serge3",20)        

# class book:
#     def __init__(self, title,author):
#         self.title=title
#         self.author=author
#     def get_info (self):
#         return f" Книга{ self.title}, Автор {self.author}"
# book1= book( "Война и Мир", "Л.Толстой") 
# print(book1.get_info())

# Домашенне задание №1
#Написать программу с классом One и создать два атрибута a и b . 
#Написать 4 метода (умножение, сложение, деление и вычитание). 
#Необходимо выполнить эти действия при передаче в методы параметров a и b.

# class One:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     def summ (self):
#         return (self.a+self.b)
    
#     def minus (self):
#         return (self.a-self.b)
    
#     def mul (self):
#         return (self.a*self.b)
    
#     def div (self):
#         return (self.a/self.b)
# Onetotal=One(2,5)
# print(Onetotal.summ())
# print(Onetotal.minus())
# print(Onetotal.mul())
# print(Onetotal.div())

# Домашнее задание №2
# Написать программу с классом Студент, у которого будет 3 атрибута: имя, номер и возраст. Необходимо создать пять методов:
# для получения данных об имени студента;
# для получения данных о возрасте;
# для номера студента;
# для изменения данных возраста;
# для изменения данных группы.

class student:
    def __init__(self, name, num_group,age):
        self.name=name
        self.num_group=num_group
        self.age=age
    def names(self):
        return(self.name)
    def ages (self):
        return(self.age)
    def numbers (self):
        return(self.num_group)
    def change_age(self, new_age):
        self.age = new_age
    def change_num_number(self, new_num_number):
        self.num_group = new_num_number
student1=student("Serge", 12, 24)
print (f"Возрост студента :", (student1.ages()))
print ("Имя студента :", (student1.names()))
print ("Группа :",(student1.numbers()))

student1.change_age(33)
print ("Изменнения данных возроста студента на - ",(student1.ages()))

student1.change_num_number(15)
print ("Изменнения данных группы  студента на - " ,(student1.numbers()))