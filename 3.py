#Обрученные
#Перебираем числа от 1 до н-1
#для каждого такого числа мы находим сумму его делителей
#Дальше обычная проверка на условия обрученных чисел
#48 75.0
#140 195.0
#1050 1925.0
#1575 1648.0
#2024 2295.0
#5775 6128.0
#8892 16587.0
#9504 20735.0
#
#
def OBRChis(n) :
    for num1 in range (1,n) :
        sum1 = 1
        i = 2
        while i * i <= num1 :
            if (num1 % i == 0) :
                sum1 = sum1 + i
                if (i * i != num1) :
                    sum1 += num1 / i
            i =i + 1
        if (sum1 > num1) :
            num2 = sum1 - 1
            sum2 = 1
            j=2
            while j * j <= num2 :
                if (num2 % j == 0) :
                    sum2 += j
                    if (j * j != num2) :
                        sum2 += num2 / j
                j = j + 1
            if (sum2 == num1+1) :
                print (num1, num2)


OBRChis(10000)
