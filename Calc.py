# Cделано Андреем Гороховым 14122
# Функция с входными данными типа число оператор число
# Выходное значение
def Calc(a,b,c):
    result=0
    try:
        a = float(a)
        b = str(b)
        c = float(c)
    except ValueError:
        print('Введено не число')
    else: 
        if b=='+':
            result=a+c
            return result
        elif b=='-':
            result=a-c
            return result
        elif b=='/':
            result=a/c
            return result
        elif b=='*':
            result=a*c
            return result
        elif b =="^" or b=="**":
            result=a**c
            return result
        else:
            print("Неизвестный оператор")
while True:
    a,b,c=input("Число_Оператор_Число ").split()
    print(Calc(a,b,c))
