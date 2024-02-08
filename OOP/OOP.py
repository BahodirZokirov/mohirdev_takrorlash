# class Person():
#     def __init__(self, __name, surname, age, city, prof):
#         self.name = __name
#         self.surname = surname
#         self.age = age
#         self.city = city
#         self.prof = prof
#
#     def get_name (self):
#         return self.name
#     def get_surname (self):
#         return self.surname
#     def get_age (self):
#         return self.age
#     def get_city (self):
#         return self.city
#     def get_prof (self):
#         return self.prof
#     def get_info (self):
#         return f"My full name is {self.name} {self.surname}. I'm {self.age} years old. I was born in {self.city} my profession is {self.prof}"
#
#
#
# person1 = Person ("Bahodir", "Zokriov", 20, "Samarkand", "Programmer")
# person2 = Person ("Diyorbek", "Berkinov", 20, "Navoiy", "SMM manager")
# person3 = Person ("Zaynobiddin", "Hoshimov", 20, "Qo'qon", "Geolog")

# print (person1.name)


# print (person1.get_name())
# print (person3.prof)
# print (person1.get_info())


# name = "Bahodir"







# class Person:
#     def __init__(self, name, surname, age, city):
#         self.ism = name
#         self.familiya = surname
#         self.yosh = age
#         self.shahar = city
#
#     def get_info (self):
#         return f"My full name is {self.ism} {self.familiya}, yoshim {self.yosh} da {self.shahar}danman"
#
# person1 = Person ("Bahodir", "Zokirov", 20, "Samarkand")
# print (person1.get_info())




                    # 06.02.2024

# class User:
#     def __init__(self, name, username, password, email):
#         self.name = name
#         self.username = username
#         self.password = password
#         self.email = email
#
#     def get_name(self):
#         return self.name
#
#     def get_username (self):
#         return self.username
#
#     def get_password (self):
#         return self.password
#
#     def get_email (self):
#         return self.email
#
#     def get_info (self):
#         return f"Name: {self.name} \nUsername: {self.username} \nPassword: {self.password} \nEmail: {self.email}\n\n"
#
#
# user1 = User("Ramazon", "RamazonQudratov1114", "ramazon1114", "ramazonqudratov1114@gmail.com")
# user2 = User("Bahodir", "BahodirZokirov0530", "BahodirZokirov0530", "zokirovbahodir2003@gmail.com")
# user3 = User("Diyorbek", "DiyorbekSaparov", "Saparov0310", "saparovdiyorbek0310")
# print (user1.get_info())
# print (user2.get_info())
# print (user3.get_info())


                # 29-dars


# class Student ():
#     def __init__(self, name, surname, age, city):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.city = city
#         # self.course = course
#         self.course = 1
#         self.prof = 'programmer'
#
#
#     def get_fullname (self):
#         return f"{self.name} {self.surname}"
#
#     def get_info (self):
#         return (f"My full name is {self.name} {self.surname} \n\nI'm {self.age} years old I'm from {self.city}."
#                 f" \n\nI'm {self.course} year student, I'm feature {self.prof}")
#
#     def get_info_as_dict (self):
#         return self.__dict__
#
#     def set_course (self, new_course):
#         self.course = new_course
#
#     def update_course (self):
#         self.course = self.course + 1
#
# student1 = Student ("Bahodir", "Zokirov", 20, "Samarkand")
# student2 = Student ('Ramazon', "Qudratov", 20, "Kitob")
# student3 = Student ("Diyorbek", "Berkinov", 20, "Navoiy")
#
# # print (student1.get_info())
# student1.set_course(2)
# student1.update_course()
# student1.update_course()
# # student1.update_course()
# # student1.update_course()
#
# # print (student1.get_info())
# # print (student2.get_info_as_dict())
#
#
#
#                   ###
#
# class Fan ():
#     def __init__(self, name):
#         self.name = name
#         self.amount_of_students = 0
#         self.students = []
#
#     def add_student (self, student):
#         self.students.append(student)
#         self.amount_of_students += 1
#
#     def get_info (self):
#         return f"Fan nomi: {self.name}\nStudentlar soni: {self.amount_of_students}\nStudents: {self.students}"
#
#
#
#     def get_student (self):
#         return [student.get_info_as_dict() for student in self.students]
#
# fan1 = Fan ("Matematika")
#
# fan1.add_student(student1)
# fan1.add_student(student2)
# fan1.add_student(student3)
#
#
# # print (fan1.get_info())
#
# print (fan1.get_student())
# # print (fan1.name)
# k = (dir (Student))
#
# def see (klass):
#     return [i for i in k if "__" not in i]

# print (see(Student))





#                   29 - dars homework

# class Auto():
#     def __init__(self, model,make, color, carobka, price):
#         self.model = model
#         self.color = color
#         self.carobka = carobka
#         self.price = price
#         self.kilometre = 0
#         self.make = make
#         self.selled = 0
#
#
#
#     def car_info (self):
#         return f"Model: {self.model}\nColor: {self.color}\nCarobka: {self.carobka}\nPrice: {self.price}\nKilometre: {self.kilometre}\nSelled: {self.selled}"
#
#
#     def car_name (self):
#         return self.model
#     def update_km(self, km):
#         self.kilometre += km
#
#
#
# car1 = Auto("Gentra", "GM", "white", "Gas", 17200)
# car1.update_km(100000)
# car1.update_km(125000)
# car1.update_km(580000)
# car1.update_km(98500)
#
# # print (car1.car_info())
#
#
#                 # homework 2
#
# class Avtosalon ():
#     def __init__(self, name, location, cars):
#         self.name = name
#         self.location = location
#         self.cars = cars
#
#
#     def get_info (self):
#         return f"Salon name: {self.name}\nLocation: {self.location}\nCars: {self.cars}"
#
#
#     def new_car(self,name):
#         self.cars.append(name)
#
#     # def get_info (self):
#     #     return [car.name for car in self.cars]
#
#
# salon1 = Avtosalon("Hyundai AJ", "Sergeli tumani", ["Sanata", "Santa Fe", "Tucson"])
# salon1.new_car("Elantra N")
# salon1.new_car("Kona Hybrid")
# salon1.new_car("Hyundai Creta")
# salon1.new_car(car1)
#
# print (salon1.get_info())

# class Person ():
#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city
#
#     def get_info(self):
#         return f"My name is {self.name} I'm {self.age} years old. I'm from {self.city}"
#
#
#     def get_age (self):
#         return self.age
#
#
#
# person1 = Person ("Bahodir", 20, "Samarkand")
# print (person1.get_age())



# class Student (Person):
#     def __init__(self, name, age, city, student_id):
#         super().__init__(name, age, city)
#         self.student_id = student_id
#         self.course = 1
#
#     def get_student_info (self):
#         return f"Name: {self.name}\nAge: {self.age}\nCity: {self.city}\nStudent_id: {self.student_id}\nCourse: {self.course}"
#
#
# student1 = Student("Bahodir", 20, "Samarkand", "40321110014855")
# print (student1.get_student_info())



                # encapsulation


# from uuid import uuid4
#
# class Car():
#     def __init__(self, model, make, color, price):
#         self.model = model
#         self.make = make
#         self.color = color
#         self.price = price
#         self.__km = 0
#         self.__id = uuid4()
#
#
#     def get_id (self):
#         return self.__id
#
#     def get_km (self):
#         return self.__km
#
# car1 = Car ("Gentra", "GM", 'white', 17000)
#
# print (car1.get_km())
# print (car1.get_id())


                      # homework





# class Car ():
#     def __init__(self, model, make, color):
#         self.model = model
#         self.make = make
#         self.color = color
#         self.km = 0
#         self.price = 0
#
#     def get_info(self):
#         return f"Model: {self.model}\nMake: {self.make}\nColor: {self.color}\nKm: {self.km}\nPrice: {self.price}"
#
#     def add_km(self, km):
#         self.km = km
#
#     def add_price(self, price):
#         self.price = price
#
#
#
# car1 = Car("Gentra", "GM", "white")
# car2 = Car("Malibu", "GM", "black")
# car3 = Car("Traverse", "GM", "black")
# car4 = Car('Santa Fe', "Hyundai", "silver")
# car5 = Car("Sonata", "Hyundai", "golden")
#
# car1.add_km(105000)
# car1.add_price(15500)
#
# car2.add_km(150000)
# car2.add_price(32000)
#
# car3.add_km(150000)
# car3.add_price(50000)
#
# car4.add_km(720000)
# car4.add_price(45000)
#
# car5.add_km(0)
# car5.add_price(35000)
#
# # print (car1.get_info(), end="\n\n")
# # print (car2.get_info())
# # print (car3.get_info())
# # print (car4.get_info())
# # print (car5.get_info())
#
#
# class Avtosalon():
#     def __init__(self, name, location):
#         self.name = name
#         self.location = location
#         self.cars= []
#         self.amount_of_cars = 0
#
#
#     def get_car_info(self):
#         return [car.model for car in self.cars]
#
#
#     def get_salon_info(self):
#         """Ushbu funksiyada nameni object sifatida qaytarpati. Agar, for bilan kirib (get_car_info) ma'lumotlarni chiqarsam boshqa faqat name yoki boshqa bitta dona argumenti bor carlarda xatolik qaytaryapti
#         how can I fix it"""
#         return f"Salon name: {self.name}\nLocation: {self.location}\nCars: {self.cars}\nAmount of cars: {self.amount_of_cars}" if type (self.cars == list) else None
#
#         # f"Salon name: {self.name}\nLocation: {self.location}\nCars: {self.cars}\nAmount of cars: {self.amount_of_cars}
#
#
#
#     def add_car(self, car):
#         self.cars.append(car)
#         self.amount_of_cars += 1
#
#
#     # def get_car_full_info(self):
#     #     return [car.name for car in self.cars]
#
# #     # def get_info (self):
# #     #     return [car.name for car in self.cars]
#
# salon1 = Avtosalon("General", "Samarkand shahar, Olimlar ko'chasi")
# salon2 = Avtosalon("DiyrobekAgroTechnic", "Samarkand viloyati Qo'shrabot tumani")
# salon1.add_car(car1)
# salon1.add_car(car2)
# salon1.add_car(car3)
# salon1.add_car(car4)
# salon1.add_car(car5)
#
# salon2.add_car("Traktor")
# salon2.add_car("Excavator")
# salon2.add_car("Zil")
# salon2.add_car("Kombine")
# salon2.add_car("Prisofka")
#
#
# # print (salon1.get_salon_info())
# print (salon2.get_salon_info())



                           #07.02.2024  30-dars Inheritense va polimorphism


# class Student():
#     def __init__(self, name, surname, age, city):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.city = city
#         self.course = 1
#         self.subject = []
#         self.amount_of_subjects = 0
#
#
#
#     def join_to_subject(self, subject_name):
#         self.subject.append(subject_name)
#         self.amount_of_subjects += 1
#
#     def drop_lesson(self, subject_name):
#         if subject_name in self.subject:
#             self.subject.remove(subject_name)
#             self.amount_of_subjects -= 1
#         # else:
#         #     return "Siz bunday fanga qo'shilmagansiz"
#
#     def subject_name(self):
#         return [sbjt.name for sbjt in self.subject]
#
#     def student_info(self):
#         return f"Name: {self.name}\nSurname: {self.surname}\nAge: {self.surname}\nCity: {self.city} \nCourse: {self.course}\nSubjects: {self.subject_name()}\nAmount of subjects: {self.amount_of_subjects}"
#
#
# student1 = Student("Bahodir", "Zokirov", 20, "Samarkand")
# student2 = Student("Sunnatillo", "Kamolov", 20, "Qashqadaryo")
# student3 = Student("Ramazon", 'Qudratov', 20, "Qashqadaryo")
# student4 = Student("Sardorbek", "Ibrohimov", 20, "Navoiy")
# student5 = Student("Zaynobiddin", "Hoshimov", 20 ,"Farg'ona")
#
# class Subject():
#     def __init__(self, name, teacher_name, credit):
#         self.name = name
#         self.teacher_name = teacher_name
#         self.credit = credit
#         self.students = []
#         self.amount_of_students = 0
#
#
#     def subject_student_info(self):
#         return [student.student_info() for student in self.students]
#
#     def get_subject_info(self):
#         return f"Subject name: {self.name}\nTeacher: {self.teacher_name}\nCredit: {self.credit}\nStudents: {self.subject_student_info()}\nAmount of students: {self.amount_of_students}"
#
#     def add_student(self, student):
#         self.students.append(student)
#         self.amount_of_students += 1
#
#
#
#
# subject1 = Subject("Strukturaviy geologiya", "Davlatov", 3)
# subject2 = Subject("Xaritalash", "Moyliyev", 4)
# subject3 = Subject("Laboratoriya usullari", "Saidov", 5)
# subject4 = Subject("Sanoat turlari", "Abdimutalov", 4)
# subject5 = Subject("Petrografiya", "Qurbonov", 6)
#
#
# # subject1.add_student(student1)
# # subject1.add_student(student2)
# # subject1.add_student(student3)
# # subject1.add_student(student4)
# # subject1.add_student(student5)
# #
# # subject2.add_student(student1)
# # subject2.add_student(student3)
# # subject2.add_student(student5)
# #
# # subject3.add_student(student4)
# # subject3.add_student(student5)
# # subject3.add_student(student2)
# #
# # print (subject1.get_subject_info())
# # print (subject2.get_subject_info())
# # print (subject3.get_subject_info())
# student1.join_to_subject(subject2)
# student1.join_to_subject(subject1)
# student1.join_to_subject(subject3)
# student1.join_to_subject(subject4)
# student1.drop_lesson(subject5)
#
# student1.drop_lesson(subject1)
#
# print (student1.student_info())



                # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# class Person():
#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city
#
#
#     def get_age(self):
#         return self.age
#     def get_info(self):
#         return f"Name: {self.name}\nAge: {self.age}\nCity: {self.city}"
#
# person1 = Person ("Bahodir", 20, "Samarkand")
# # print (person1.get_info())
#
#
#
# class Student(Person):
#     def __init__(self, name, age, city, student_id, course):
#         super().__init__(name, age, city)
#         self.student_id = student_id
#         self.course = course
#
#
#     def get_info(self):
#         return f"{Person.get_info(self)}\nStudent_id: {self.student_id}\nCourse: {self.course}"
# student1 = Student("Sunnatillo", 20, "Qashqadaryo", "40320001528", 1)
# # print (student1.get_info())
#
#
# class Professor (Person):
#     def __init__(self, name, age, city, degree, speciality):
#         super().__init__(name, age, city)
#         self.degree = degree
#         self.speciality = speciality
#
#     def get_info(self):
#         return f"{Person.get_info(self)}\nDegree: {self.degree}\nSpeciality: {self.speciality}"
#
# professor1 = Professor ("Sunnatillo", 20, "Qashqadaryo", "phd", "Kartojnik")
# # print (professor1.get_info())
#
#
# print (person1.get_info(), end="\n\n")
# print (student1.get_info(), end="\n\n")
# print (professor1.get_info(), end="\n\n")


# class Avto():
#
#     __num_avto = 0
#     def __init__(self, name, make, color):
#         self.make = make
#         self.name = name
#         self.color = color
#         self.__km = 0
#         Avto.__num_avto += 1
#
#     @classmethod
#     def num_avtoo(cls):
#         return Avto.__num_avto
#
#
#     def get_info(self):
#         return f"Name: {self.name}\nMake: {self.make}\nColor: {self.color}\nKm : {self.__km}"
# avto1 = Avto("Malibu", "GM", "silver")
# avto2 = Avto("Malibu", "GM", "silver")
# avto3 = Avto("Malibu", "GM", "silver")

# print (avto1.get_info())
# print (avto1.__num_avto)
# print (avto1.num_avtoo())



# class Avto():
#     def __init__(self, name, make, color, price):
#         self.name = name
#         self.make = make
#         self.color = color
#         self.price = price
#
#     # def __str__(self):
#     #     return self.name
#
#     def __repr__(self):
#         return f"{self.make} {self.name}"
#
# avto1 = Avto("Malibu", "GM", "silver", 35000)
# # print (avto1)
# print (avto1)


# class Address():
#     def __init__(self, country, city, home):
#         self.country = country
#         self.city = city
#         self.home = home
#
#     # def __repr__(self):
#     #     return self.country
#     def get_address(self):
#         return f"Country: {self.country}\nCity: {self.city}\nHome: {self.home}"
#
# address1 = Address("Uzbekistan", "Samarkand vil", "Sho'rcha qq 35-uy")
# address2 = Address("USA", "Kaliforniya", "Silicon valley, 44-home")
#
#
# class Student ():
#     def __init__(self, name, surname, age, address):
#         self.name = name
#         self.surname = surname
#         self._age = age
#         # self.__city = city
#         self.address = Address
#
#
#
#     def get_info(self):
#         return f"Name: {self.name}\nSurname: {self.surname}\nAge: {self._age}\nAddress: {Address.get_address(address1)}"
# student1 = Student("Bahodir", "Zokirov", 20, Address)
# # print (student1.get_info)
# print (student1.get_info())



# class Car:
#     def __init__(self, name, make, price, km):
#         self.name = name
#         self.make = make
#         self.__price = price
#         self._km = km
#
#     def get_price(self):
#         return self.__price
#     def get_km(self):
#         return self._km

# car1 = Car("Malibu", "GM", 35000, 10000)
# print (car1.name)
# print (car1.get_km())
# print (car1.get_price())

#
# class Student:
#     def __init__(self, name, surname, age, address):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.address = address

# class Address:
#     def __init__(self, viloyat, tuman, MFY, uy):
#         self.viloyat = viloyat
#         self.tuman = tuman
#         self.MFY = MFY
#         self.uy = uy
#     # def get_address(self):
#     #     return self.tuman
#
# address1 = Address("Samarkand", "Qo'shrabot", "Qoratosh", 35)
# student1 = Student("Bahodir", "Zokirov", 20, address1)
#
# print (student1.address.uy)



# class Student:
#     def __init__(self, name, surname, age, address):
#         self.name = name
#         self.surname = surname
#         self.age = age



# class Fan:
#     amount_students = 0
#     def __init__(self, name, time, davomiylik):
#         self.name = name
#         self.time = time
#         self.davomiylik = davomiylik
#         self.students = []
#         self.amount_of_students = 0
#         # Fan.amount_students += 1
#
#     def add_student(self, student):
#         self.students.append(student)
#         self.amount_of_students += 1
#         with open (f"{self.name}.txt", 'a') as my_file:
#
#             my_file.write(f"{self.amount_of_students}. {student}\n")
#
# Python = Fan("Python", '18:30', "8 oy")
# C = Fan("C", "12:00", "11 oy")
# js = Fan("React", "09:00", "8 oy")
# Python.add_student("Bahodir")
# Python.add_student("Sardor")
# Python.add_student("Elbek")
# Python.add_student("Eldor")
# Python.add_student("Baxtiyor")
# Python.add_student("Fayzullo")
#
# # C.add_student("Samandar")
# # C.add_student("Ramazon")
# # C.add_student("Asilbek")
# # C.add_student("Shaxboz")
# # C.add_student("Diyorbek")
# #
# # js.add_student("Zaynobiddin")
# # js.add_student("Ahmadillo")
# # js.add_student("Fayzullo")
# js.add_student("Shohnazar")
#
# # print (Python.students)
# # print (Python.amount_of_students)
#
# # print (C.students)
# # print(C.amount_of_students)
#
# # print (js.students)
# # print (js.amount_of_students)
# # print (js.amount_students)


class Car:
    def __init__(self, name, make, price):
        self.name = name
        self.make = make
        self.price = price


    def __repr__(self):
        return f"Car: {self.make} {self.name}"

    def __lt__(self, other):
        return self.price < other.price

    def __eq__(self, other):
        return self.price == other.price

    def __ne__(self, other):
        return self.price != other.price

    def __len__(self):
        return len(self.name)

car1 = Car("Malibu", "GM", 35000)
car2 = Car("Traverse", "GM", 58000)
car3 = Car("Gentra", "GM", 18000)
car4 = Car("Epica", "GM", 35000)
car5 = Car("Onix", "GM", 21000)
car6 = Car("Monza", "GM", 21000)
# print (car1)
# print (car1 != car4)


class Salon:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.cars = []
        self.amount_cars = len(self.cars)



    def add_car(self, car):
            if isinstance(car, Car):
                self.cars.append(car)
                self.amount_cars += 1


    def __getitem__(self, item):
        return self.cars[item]

    def __setitem__(self, key, value):
        self.cars[key] = value

    def __len__(self):
        return len(self.cars)

    # def __call__(self, *args, **kwargs):
    #     return self.cars

    def __call__(self, *args, **kwargs):
        if args:
            for car in args:
                self.add_car(car)
        else:
            return [car for car in self.cars]

    def __add__(self, other):
        if isinstance(other, Salon):
            return self.cars + other.cars

    




salon1 = Salon("MaxGM", "Tashkent")

salon1.add_car(car1)
salon1.add_car(car2)
salon1.add_car(car3)
salon1.cars[1] = Car("Santa Fe", "Hyundai", 55000)

# print (salon1.cars)
# print (salon1.amount_cars)
#
# print (salon1.cars[2])
# print (salon1())

# print(salon1(car4, car5, car6))
# print (salon1())
salon2 = Salon("Golden Cars", "Samarkand")
salon2(car4, car6,car5)
print (salon1())
print (salon2())
print (salon1 + salon2)