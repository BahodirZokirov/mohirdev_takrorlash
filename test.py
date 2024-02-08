# lt = ['malibu', 'nexia', 'gentra']
# lt.pop(0)
# lt.remove('nexia')
# print (lt)


# lt = ['olma', 'anor', 'anjir', 'uzum', 'shaftoli']
# print (f'bozordan {lt.pop(0), lt.pop(1)} oldim.\n{lt} larni olish kk')


# names = ['Sardor', 'Ramazon', 'Samandar', 'Akbar']
# print(names.pop(0))
# print(names.pop(0))
# print(names.pop(0))
# print(names.pop(0))
# print(names.pop(1))
# print(names.pop(2))
# print(names.pop(3))

# print (names[0])
# print (names[1])
# print (names[2])
# print (names[3])

# names.sort(key=lambda x: len(x))
# print (names)



# sonlar = list(range(0, 10, 2))
# print(sonlar)

# name = "Bahodir"
# my_name = name
# name = 'Sardor'
# print (name)
# print (my_name)



# name = input ("Ismingizni kiriting: ")
# print (f"Assalomu alaykum {name} sahifamizga xush kelibsiz")

# for i in range (1000000000000000):
#     print(i)


# names = ['Samandar', 'Sunnatillo', "Bahodir"]
# names.reverse()
# print (names)

# names.sort(reverse=True)
# print (names)

#
# lt = list(range(120, 1201, 2))
# print (lt)
# print (sum(lt))
# print (max(lt) - min (lt))
# print (len(lt))
# print (lt[:20])
# print (lt[260:280])
# print (lt[-20:])


# for i in range (11, 101, 2):
#     print (i ** 3)


# kinolar = []
# for i in range(5):
#     kino = input ("sevimli kinongizni kiriting: ")
#     kinolar.append(kino)
# print (kinolar)


# lt = []
# soni = int(input ("Bugun nechta odam bilan suhbatlashdingiz: "))
# for odam in range(1, soni + 1):
#     lt.append((input(f"{odam} - suhbatdoshingiz ismini kiriting: ")))
# print (lt)
# raqam = list(range(1, 101))
# while True:
#     yosh=int(input("yoshingizni kiriting: "))
#     # talaba=input("siz talabamisiz? \n1-ha,2-yo'q\n>>>")
#
#
#     if yosh > 18 and yosh < 22:
#         talaba = int(input ("Siz talabamisiz? \n1-ha,2-yo'q\n>>>"))
#         if talaba == 1:
#             id = int (input ("ID iningizni kiriting:"))
#             if id in raqam:
#                 print("50% chegirma")
    #     else:
    #         print ("")
    # if yosh > 60 or yosh < 4:
    #     print("chipta siz uchun tekin")
    # elif yosh >18 and yosh <22:
    #     print("talabalar uchun 50% CHEGIRMADAN foydalaning")
    # elif talaba=="1":
    #     id = input ("talaba ID sini kiriting: ")7r

    #     if id in raqam:
    #         print ("tasdiqlandi")
    #     else:
    #         print ("Mavjud bo'lmagan talaba")
    # elif yosh < 18:
    #     print("chipta siz uchun 10 ming ")
    # else :
    #     print ("chipta siz uchun 30 ming ")


# for i in range (111111111111111111111):
#     print (i)

# a = 0
# while True:
#     a += 1
#     print (f"Sardor {a}")

# def bahodir (request):
#     print (request)
#
#
# def daraja (asos, daraja):
#     return asos ** daraja
#
# bahodir (daraja(2, 5))
# range.
#
# for i in range (25):
#
#     print (i + 1)
#     print (i)

# son = float(input("Juft son kiriting: ")
# if son%2==0:
#     print("Bu son juft emas.')
# else:
#     print("Rahmat!"))

# son = int(input("Istalgan butun son kiriting: "))
#
# for n in range(2,11):
#     if son % n:
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")

# users = ['alisher1983','aziza','yasina', 'umar']
#
# login = input("Yangi login tanlang:")
#
# if login in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print("Xush kelibsiz!")


# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz', 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
#
# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else:
#     print("Savatingiz bo'sh")



# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz','kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#
#
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
#
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(f"{mahsulot}")
#     else:
#         mavjud_emas.append(mahsulot)
#
# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
# for mahsulot in mavjud_emas:
#   print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")



# talabe = {}
# print (type (talabe))

# soz = 'mexanizatsiyalashtirilmaganligidandirda'
# dt = {}
# for harf in soz:
#     dt[harf] = soz.count(harf)
# dtt = sorted (dt.items(), key=lambda x: x[1], reverse=True)
#
# print (dtt)



# en_uz = {
#     "apple": "olma",
#     "phone" : "telefon",
#     "laptop" : "kompyuter",
#     "table" : "stol",
# }
# soz = input ("Inglizcha so'z kiriting: ")
# # print (en_uz[soz])
# # print (en_uz.get(soz))
#
# print (en_uz.get(soz))
# # print (en_uz.get(soz, "Bunday so'z bizning lug'atda mavjud emas"))

# print ("Bahodir "
#        "ZOkirov")





# print ("dasturn tugashi uchun 'exit'ni kiriring.")
# sikl = 1
# mahsulot = input(f"{sikl} - mahsulot nomini kriting: ")
# lt = []
# while mahsulot != 'exit':
#     lt.append(mahsulot)
#     mahsulot = input (f"{sikl + 1} - mahsulot nomini kiriting: ")
#     sikl += 1
# print (mahsulot)


# for son in range(7):
#     if son == 5:
#         break
#     print (son)

# print (print.__doc__)


# def ism (ism):
#     "vali akaning kalishi"
#     print ( f"Assalomu alaykum {ism}")
#
# print (ism.__doc__)


# lt = []
# def rencho (start=0, finish=100, step=None):
#     if step:
#         while start < finish:
#             start += step
#             lt.append (start)
#     else:
#         while start < finish:
#             start += 1
#             lt.append(start)
#     return lt
#
#
# print (rencho(25, 30))


# def avtolar (make, model, color, price):
#
#     print ("salonimizda quyidagi mashinalar bor: ")
#
#     return f"{make} {model}, {color}, {price}"
#
# print ("Avtomobil uchun quyidagim ma'lumotlarni kiriting: ")
#
# print (avtolar( make = input ("Nomini kiriting: "),
#     model = input ("Modelni kiriting: "),
#     color = input ("Rangini kiriting: "),
#     price = input ("Narxini kiriting: ")))

# ismlar = ['Bahodir', "Diyorbek", "Botir", "Qodir", "Ali"]
# def bahola (ismlar):
#     natija = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input (f"{ism.title()}ning bahosini kiriting: ")
#         natija[ism] = baho
#     return natija
#
# print (bahola(ismlar))

# def sonlar (*son):
#     return son
# print (sonlar('fadsf', "afadadfadf", 'adfadf'))



# def new_function (x, y, *sonlar):
#     return x + y + sum (sonlar)
# print (new_function(5, 5,9))


# def kwargs (*args, **kwargs):
#     return f"{args} {kwargs}"
#
# print (kwargs("GM", model="Malibu", price=32000))


# def name(ism):
#     return (f"Assalomu alaykum {ism} aka")

from math import pi
# import math
# from math import pow
# number = 4852
# print (pow(number, 0.5))


# print (math.pi)
# print (pi)

import random as r
# sonlar = list (range (11))
# print (r.randint(0, 60))
# son = r.randint (sonlar)

# sonlar = list (range (15))
# r.shuffle (sonlar)
# print (sonlar)


# uzunlik = lambda pi, r: pi * 2 * r
# print (uzunlik(pi, 4))


# def daraja (x):
#     return lambda n: n ** x
#
# kvadrat = daraja (2)
# kub = daraja (3)
# print (kub(5))


# def kvadrat (x):
#     return x ** 2

# lt = list (map (kvadrat, list (range (11))))
# print (lt)



# def ildiz (x):
#     return x ** (1 / 2)
# lt = list (map (ildiz, list (range (10))))
# print(lt)

# print (list (map (lambda x: x ** 2, list (range (11)))))
#
# import random as r
# lt = r.sample ([25, 51, 85, 63, 621, 7, 0, 2, 4, 6, 8, 44, 2586, 85236974], 5)
# print (lt)



# def juftmi (number):
#     return number%2==0
# print (juftmi(10))


# print (list (filter(lambda x: x%2==0, lt)))





lt = list (range (101))
print (list (filter (lambda x: x % 2 == 0, lt)))