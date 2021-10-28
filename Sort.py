
def sort(a=[1,2,7,8,9,10],b=[3,6]):
    c=[]
    a_num=0
    b_num=0
    length_a=len(a)
    length_b=len(b)
    if a[0] < b[0]:
        c.append(a[0])
        a_num=1
        length_a-=1
        print(length_a)
    else:
        b_num=1
        c.append(b[0])
        length_b-=1
    print('first Iter',c,length_a,length_b)
    
    for i in range(a_num,length_a):
        flag_of_appending=False
        print('a[i]',a[i])
        for j in range(b_num,length_b):
            print('b[j]=',b[j])
            if a[i] < b[j]:
                flag_of_appending=True
                c.append(a[i])
                print('*',c)
                break
            else:
                c.append(b[j])
                print('-',c)
    tail=0
    if flag_of_appending==False:
        c.append(a[i])
        i+=1
        print('a=',a[i])
        tail=length_a-length_b
        while not tail ==0:
            print('tail_a',tail)
            c.append(a[i])
            i+=1
            tail-=1
    else:
        tail=length_b-length_a
        while not tail ==0:
            print('tail_b',tail)
            c.append(a[j])
            j+=1
            tail-=1
    print('tail',tail)
    print(c)
sort()


        

    
