import copy
def detour(i,j,oX,oY):
  global a
  setA=set()
  reference=a[i][j]
  #print("ref",reference)
  a[i][j]=0
  
  if reference!=0:
    #print("Нуль позиция",reference,i,j)
    
    
    if j+1<=oX and reference==a[i][j+1]:
        #print("whRight",reference,a[i][j+1])
        #print("вправо",a[i][j+1])
        setA.update(detour(i,j+1,oX,oY))
        setA.add((a[i][j+1],i,j+1))
        #print("setUpdate",setA)
        a[i][j+1]=0
    
    if i+1<=oY and a[i+1][j]==reference :
        #print("вниз",a[i+1][j],i+1,j)
        setA.update(detour(i+1,j,oX,oY))
        setA.add((a[i+1][j],i+1,j))
        #print("setUpdate",a[i+1][j],i+1,j)
        a[i+1][j]=0
    if j-1>=0 and a[i][j-1]==reference:
        print("влево",a[i][j-1])
        setA.update(detour(i,j-1,oX,oY))
        setA.add((a[i][j-1],i,j-1))
        a[i][j-1]=0
    if len(setA)==0:
        #print("end")
        a[i][j]=reference
    setA.add((a[i][j],i,j))
    
    
    
    
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


for i in range(oY+1):
    for j in range(oX+1):
        print("answer",detour(i,j,oX,oY))
        


for i in a:
    print(i)
print("")
for i in b:
    print(i)

