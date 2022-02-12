#Во временной папке создайте 365 фалов по формату data_DDD_hh_mm.txt
#где DDD день года. hh и mm случайные час и время.
#Запишите внутрь файла время в секундах, означающее разницу между временем,
#определенным DDD и hh и mm (секунды возьмите за 0) и временем его создания.
import random
from datetime import datetime
for day in range(1, 365+1):
    hh=random.randint(0, 24)
    mm=random.randint(0, 60)
    naming=str(day)+'_'+str(hh)+'_'+str(mm)
    file_name = 'data_{}.txt' .format(i)
    PC_Time=datetime.now()
    #today=[PC_Time.day, PC_time.month, PC_Time.year]
    d, ms, y = PC_Time.day,PC_time.month,PC_Time.year
    #вычисляем сегодняшний порядковый день
    h=naming.hour
    m=naming.minute
    b=file_name.split('_')
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


    
      
  

       
  
