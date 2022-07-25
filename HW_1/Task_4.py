#Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

def show_range_points(number):
    if number==1:
        print("Диапазон координат точек первой четверти: \nХ= от 0 до 10, Y= от 0 до 10")
    elif number==2:
        print("Диапазон координат точек второй четверти: \nХ= от -10 до 0, Y= от 0 до 10")
    elif number==3:
        print("Диапазон координат точек третьей четверти: \nХ= от 0 до 10, Y= от -10 до 0")
    elif number==4:
        print("Диапазон координат точек четвертой четверти: \nХ= от -10 до 0, Y= от -10 до 0")
    else:
        print("Что-то пошло не так.\nПопробуйте еще раз.")


show_range_points(3)