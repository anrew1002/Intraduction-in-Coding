
def my_sort(a):
    for i in range(len(a)):
        min_ind=i
        for j in range(i,len(a)):
            if a[j] < a[min_ind]:
                min_ind=j    
        a[min_ind],a[i]=a[i],a[min_ind]
    return a

mas_to_sort=[]
            #чтение файла
f=open("input.txt","r").readlines()
#print(f)
for i in f:
    i=i.split()
    mas_to_sort.append(list(map(int,i)))
#cортировка внутреннего скучного массива
print(mas_to_sort,"\n")
mas_to_sort=list(map(my_sort,mas_to_sort))
#print(mas_to_sort)
    #сортировка внешнего массива
for i in range(len(mas_to_sort)-1):
    for j in range(len(mas_to_sort)-i-1):
        if mas_to_sort[j]==mas_to_sort[j+1]:
            continue #продолжить без изменения порядка
        k=0
        enough_elements=True
        while mas_to_sort[j][k]==mas_to_sort[j+1][k]: # весь while нужен для счетчика индексов элементов                                     
            try :                                       # которые будут сравнивать,(+1, если элементы текущего индекса равны )
                mas_to_sort[j][k+1]
            except IndexError:
                enough_elements=False
                #print("1")
                break #разрыв while
            try :                                       #try для определенния отстутствия элементов следующего индекса
                mas_to_sort[j+1][k+1]
            except IndexError:
                #print("2")
                enough_elements=False
                mas_to_sort[j],mas_to_sort[j+1]=mas_to_sort[j+1],mas_to_sort[j]
                break #разрыв while
            k+=1
        if mas_to_sort[j][k]>mas_to_sort[j+1][k] and enough_elements:
            mas_to_sort[j],mas_to_sort[j+1]=mas_to_sort[j+1],mas_to_sort[j]
print(mas_to_sort)
    
                    
             
