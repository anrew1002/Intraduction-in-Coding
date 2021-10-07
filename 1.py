#ГОРОХОВ АНДРЕЙ ЕВГЕНЬЕВИЧ 14122
#Ищет числа Армстронга
#Обычнй перебор с проверкой на условия
#из оптимизации только проверка на повторяющиеся цифры
#например если 153 уже в массиве 513 проверяться не будет
#
#1
#2
#3
#4
#5
#6
#7
#8
#9
#153
#370
#371
#407
#1634
#8208
#9474
#54748
#92727
#93084
#548834
#1741725



def colch(n):
    n=str(n)
    return len(n)
def namin(n):
    n=str(n)
    mas=[]
    for l in n:
        mas+=[l]
        mas.sort()
    return mas
masISKL=[]
for i in range(1,10**40):
    razriad= colch(i)
    ver=namin(i)
    otv=0
    if ver!=masISKL:
        for j in range(razriad):
            otv+=int(ver[j])**razriad
        if i==otv:
            print(i)
            masISKL+=ver
print(masISKL)
    
    
