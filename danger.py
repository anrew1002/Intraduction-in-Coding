sum1=0
while True:
    while True:
        try:
            list1=list(map(int,input().split()))
            #print(list1)
            break
        except ValueError:
            print('Введены *не* числа')
    sum1+=sum(list1)
    if sum1!=0:
        print(sum1)
    else:
        print('END')
        break
