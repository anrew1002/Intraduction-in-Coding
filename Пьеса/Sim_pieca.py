#Выполненно Гороховым Андреем
def help():
    print("Что вы хотите сделать?")
    time.sleep(0.5)
    print("Cписок команд:")
    print(".......................................................")
    print("begin- начать работу")
    print(".......................................................")
def main():
    help()
    while True:
        offer=input("//помошник---> ")
        #offer="begin"
        if offer=="begin":
            roles_to_par()
            break
        else:
            print("Извините, команда не расспознана")
def roles_to_par():
    File = open('pyesa.txt', 'r')
    myDict ={}
    i = 1
    for line in File:
        x = line.split()
        myDict[x[0].strip('. ')] = myDict.get(x[0].strip('. '), '') + str(i) + ') ' + ' '.join(x[1:]) + '\n'
        i += 1
    for k,v in myDict.items(): print(k, ':\n', v, sep='')

    File.close()
    
    
        
import time

print("Приветствую вас, Я - *не* умный помошник для артистов театра")
for i in range(3):
    print("...")
    time.sleep(0.5)

main()
for i in range(3):
    print("...")
    time.sleep(0.5)
print("Да")
time.sleep(1)
print("Это всё")
time.sleep(1)
print("На то я и 'не умный' помощник")
time.sleep(1)
print("Это немного, но это честная работа~")
    
