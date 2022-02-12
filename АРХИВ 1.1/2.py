#ГОРОХОВ АНДРЕЙ ЕВГЕНЬЕВИЧ 14122
#
#Ищет дружественные числа
#перебирает все числа  и смотрит получится ли
#из суммы их делителей число сумма делителей которой будет равна первому числу
#220 284
#284 220
#1184 1210
#1210 1184
#2620 2924
#2924 2620
#5020 5564
#5564 5020
#6232 6368
#6368 6232
#10744 10856
#10856 10744
#12285 14595
#14595 12285
#17296 18416
#18416 17296
# и далее....
from math import sqrt

def delit(n):
    list1=[1]
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            list1.append(i)
            list1.append(n//i)
    #if n%sq==0:
         #list1.append(sq)
    return sum(list1)
#print(int(sqrt(8)))
#print(delit(1568)
#print (delit(410))
##for i in range(220,10000):
    ##delFirst=delit(i)
    ##for j in range(i+1,10000):
        ##delSecond=delit(j)
        ##if delFirst==j and delSecond==i :
            ##print(i,j)
#print(delit(496))
#print('2',delit(1184),delit(1210))
for i in range(1,100000):
    delFirst=delit(i)
    if delit(delFirst)==i and not(i>=delFirst) :
        print(i,delFirst)


