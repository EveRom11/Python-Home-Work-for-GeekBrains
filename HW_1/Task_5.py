#Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве. 
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21



def two_D():
    import math
    xa=int(input("Введите координаты точки xА: "))
    xb=int(input("Введите координаты точки xB: "))
    ya=int(input("Введите координаты точки yА: "))
    yb=int(input("Введите координаты точки yB: "))
    S=math.sqrt(((xb-xa)**2)+((yb-ya)**2))
    print(round(S,2))

two_D()


#формула вроде правильная, но результаты не сходятся.