
#print(int(3.5))
def mas_division(Base):
    if len(Base)<2:
        return Base
    else:
        i=int(len(Base)/2)
        left=mas_division(Base[:i])
       # print(left)
        right=mas_division(Base[i:])
        #print(right)
        return compare(left,right)
def compare(left,right):
    sortedMAS=[]
    i=0
    j=0
    #print(left,right,"----")
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sortedMAS.append(left[i])
            #print("left:",sortedMAS)
            i+=1
            #print(i)
        #if right[i]<left[i]:
        else:
            sortedMAS.append(right[j])
            #print("right",sortedMAS)
            j+=1
    while i<len(left):
        sortedMAS.append(left[i])
        i+=1
    while j<len(right):
        sortedMAS.append(right[j])
        j+=1
    #print("sort:",sortedMAS)
    return sortedMAS
def CreateNums():
    import random
    file=open("nums.txt","w")
    a=[x for x in range(300)]
    random.shuffle(a)
    for l in a:
        file.write(str(l))
        file.write("\n") 
    
#base=[1,4,3,5,2,8,7]
#print(base)
#print(mas_division(base))


while True:
        offer=input("Создать файл nums.txt с рандомно перемешанами числами от 0 до 300? \nРекомендуется если нет заготовленного файла. [yes/no] ")
        if offer=="yes":
            CreateNums()
            break
        elif offer=="no":
            break
        print("\n")
UserInput=input("\nИмя файла с данными: ")
Good=False
while not Good:
    try:
        f=open(UserInput)
    except FileNotFoundError:
        print("Файл не найден")
        UserInput=input("Имя файла с данными: ")
    else:
        Good=True
        

f=f.readlines()
massive=[]
for line in f:
    massive.append(int(line))
result=mas_division(massive)
#print(result)
try:
    file=open("results.txt")
except FileNotFoundError:
    file=open("results.txt","w")
    for num in result:
        file.write(str(num))
        file.write("\n")
    file.close()
else:
    while True:
        offer2=input("\nФайл с результатами уже существует. Заменить? [yes/no] ")
        if offer2=="yes":
            file=open("results.txt","w+")
            for num in result:
                file.write(str(num))
                file.write("\n")
            print("Успешно!")
            break
        elif offer2=="no":
            print("Перезапустите программу когда надумаете")
            break
    file.close()
    
            
    
