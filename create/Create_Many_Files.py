#Во временной папке создайте 365 фалов по формату data_DDD_hh_mm.txt
#где DDD день года. hh и mm случайные час и время.
#Запишите внутрь файла время в секундах, означающее разницу между временем,
#определенным DDD и hh и mm (секунды возьмите за 0) и временем его создания.
import random
from datetime import datetime
for i in range(1, 365+1):
    hh=random.randint(0, 24)
    mm=random.randint(0, 60)
    i=str(i)+'_'+str(hh)+'_'+str(mm)
    file_name = 'data_{}.txt' .format(i)
    #вычисляем сегодняшний порядковый день
    a=datetime.now()
    today=[a.day, a.month, a.year]
    d, ms, y = today
    #вычисляем сегодняшний порядковый день
    h=a.hour
    m=a.minute
    b=i.split('_')
    #print('часы ', h)
    #print('часы рандомные ',hh)
    #print('минуты ', m)
    #print('минуты рандомные ',mm)
    if m-mm<0:
        h=h-1
        m=m-mm+60
        #print('часы ', h,'минуты  ' , m)
    else:
         m=m-mm
         #print('часы ', h,'минуты  ' , m)
    if h-hh<0:
        d=d-1
        h=h-hh+60
    else:
         h=h-hh
    today=(datetime(y, ms, d) - datetime(y, 1, 1)).days + 1
    #print('сегодня ',today)
    c=(today-int(b[0]))*24*60*60+h*60*60+m*60
    f=open(file_name,'w+')
    f.write(str(c))
    f.close()


    
      
  

       
  
