import copy
def detour(i,j,oX,oY):
  global a
  setA=set()
  reference=a[i][j]
  if a[i][j]!=0:
    setA.add((a[i][j],i,j))
    print("Нуль позиция",a[i][j],i,j)
    
    
    if j+1<=oX and a[i][j]==a[i][j+1]:
        print("whRight",a[i],a[i][j+1])
        print("вправо",a[i][j+1])
        setA.update(detour(i,j+1,oX,oY))
        setA.add((a[i][j+1],i,j+1))
        print("setUpdate",setA)
        a[i][j+1]=0
    
    if i+1<=oY and a[i+1][j]==a[i][j] :
        print("вниз",a[i+1][j],i+1,j)
        setA.update(detour(i+1,j,oX,oY))
        setA.add((a[i+1][j],i+1,j))
        print("setUpdate",a[i+1][j],i+1,j)
        a[i+1][j]=0
    
        
        
        
    else:
        print("end")
    
    
    
  return setA
    

print("hello!")


a=[[1,1,3],
   [1,3,3],
   [1,6,7],
   [0,2,3]]

oX=len(a[1])-1
oY=len(a)-1
print("lens",oY,oX)


b=copy.deepcopy(a)
for i in a:
  print(i)
#print(a[0+1][0+1])
print("")


for i in range(oY):
    for j in range(oX):
        detour(i,j,oX,oY)


for i in a:
    print(i)
print("")
for i in b:
    print(i)

