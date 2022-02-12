# Сделано Андреем Гороховым
# Функция перевода числа в заданую систему счисления
def CCnumbers():
    Errors=True
    while Errors:
        try:
            a,b=map(int,input('Введите число и СС ').split())
        except ValueError:
            print("Critical Error,try again")
            continue
        else:
            Errors=False
        
    s=0
    st=''
    x=['A', 'B', 'C', 'D', 'E', 'F']
    while a>0:
        s=a%b
        if s>=10:
           s=x[s-10]
        else:
            s=str(s)
        st+=s
        a=a//b
    #print(st[::-1])
    return st[::-1]
hr=CCnumbers()
print(hr)

