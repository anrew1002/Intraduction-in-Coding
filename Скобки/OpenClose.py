plant=input()
#plant="{{g}<g>}"
opened=["{","[","<","("]
closed=["}","]",">",")"]
print(plant)
hooks=[]
open_hook=False
print(len(plant))
for i in range(len(plant)):
    if plant[i] in opened+closed:
        print("OK")
        if plant[i] in opened:
            hooks.append(plant[i])
            counter=1
            miss=0
            while counter < (len(plant)-i):
                print("Bingo",plant[i+counter])
                if plant[i+counter] in opened:
                    miss+=1
                elif plant[i+counter] in closed and miss==0:
                    hooks.append(plant[i+counter])
                    print("MMM:",plant[i+counter])
                    break
                elif plant[i+counter] in closed and miss!=0:
                    miss-=1
                counter+=1
                
                    
print(hooks)
