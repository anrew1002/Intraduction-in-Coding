def ziper(a):
    end=[]
    k=0
    for i in a:
        
        if k==0:
            end.append(i)
            k+=1
        elif k==1:
            end.append(end.pop()+i)
            k=0
    return end
plant=input()
#plant="{{g}<g>}"
opened=["{","[","<","("]
closed=["}","]",">",")"]
#print(plant)
hooks=[]
open_hook=False
#print(len(plant))
for i in range(len(plant)):
    if plant[i] in opened+closed:
        #print("OK")
        if plant[i] in opened:
            hooks.append(plant[i])
            counter=1
            miss=0
            while counter < (len(plant)-i):
                #print("Bingo",plant[i+counter])
                if plant[i+counter] in opened:
                    miss+=1
                elif plant[i+counter] in closed and miss==0:
                    hooks.append(plant[i+counter])
                    #print("MMM:",plant[i+counter])
                    break
                elif plant[i+counter] in closed and miss!=0:
                    miss-=1
                counter+=1

for k in ziper(hooks):
    if k==opened[0]+closed[0] or k==opened[1]+closed[1] or k==opened[2]+closed[2] or k==opened[3]+closed[3]:
        print("ok")
    else:
        print("Есть проблема")
