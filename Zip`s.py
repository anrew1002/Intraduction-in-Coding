def multiplication (a):
    ret=1
    for i in a:
        
        ret*=i
    return ret
print(type(3))      

a=[1,2,3,4]
print("1)\nМассив на входе: ", a)
print("Вывод:",list(zip(a,a)))

b=[1,3,0,5]
c=[2,4,3,5]
worked=list(zip(a,b,c))
worked2=list(map(multiplication,worked))
print("2)\nМассив на входе: ", a,b,c)
print("Вывод:",worked2)

dem=[1,1,"КУ-КУ",[3,4,5,7],345]
for i in range(len(dem)):
    if isinstance(dem[i],int):
        dem[i]=str(dem[i])
    
print("3)\nМассив на входе: ", dem)
print("Вывод:",list(map(len,dem)))

print("4)\nМассив на входе: ", c)
print("Вывод:", list(filter(lambda x: x % 2 == 0,a)))

pim=[[],[1,2,3,4],[],[34],[5,6]]
print("5)\nМассив на входе: ", pim)
print("Вывод:", list(filter(lambda x: x != [],pim)))

print("6)\nМассив на входе: ", a,b,c)
print("Вывод:",list(zip(a,b,c)))

print("1)\nМассив на входе: ", b,a)

print("Вывод:", list (zip(b,list(zip(a,a)))))






