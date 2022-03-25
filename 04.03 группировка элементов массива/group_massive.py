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
        #print("влево",a[i][j-1],i,j-1)
        setA.update(detour(i,j-1,oX,oY))
        setA.add((a[i][j-1],i,j-1))
        a[i][j-1]=0
    if i-1>=0 and a[i-1][j]==reference:
        setA.update(detour(i-1,j,oX,oY))
        setA.add((a[i-1][j],i-1,j))
        a[i-1][j]=0
    if len(setA)==0:
        #print("end")
        a[i][j]=reference
    setA.add((reference,i,j))
  return setA
def printMatrix(mas,text=""):
  print(text)
  for line in mas:   
    print(line)
  print()

def FileReaderMatrix(name):
  f=open(name,"r").readlines()
  a=[]
  for line in f:
    line=list(map(int,line.split(" ")))
    a.append(line)
  return a
    
print("hello!")

a=[[1,1,3,2,0],
   [1,3,3,2,3],
   [1,6,3,2,3],
   [0,6,3,3,3]]

a=FileReaderMatrix("input1.txt")
oX=len(a[1])-1
oY=len(a)-1
#print("lens",oY,oX)
b=copy.deepcopy(a)
printMatrix(a)
outputDetour=[]
counter=0
for i in range(oY+1):
    for j in range(oX+1):
      output=detour(i,j,oX,oY)
      print(output)
      
      if output!=set():
        counter+=1
        outputDetour.append(output)
      #print("answer",outputDetour)
#printMatrix(a)
#for i in b:
    #print(i)
#print(outputDetour)
answer1=[[0]*(oX+1) for _ in range(oY+1)]
answer2=[[0]*(oX+1) for _ in range(oY+1)]
answer3=[[0]*(oX+1) for _ in range(oY+1)]
answer4=[[0]*(oX+1) for _ in range(oY+1)]
answer5=[[0]*(oX+1) for _ in range(oY+1)]
answer6=[[0]*(oX+1) for _ in range(oY+1)]
answer7=[[0]*(oX+1) for _ in range(oY+1)]
answer8=[[0]*(oX+1) for _ in range(oY+1)]
answer9=[[0]*(oX+1) for _ in range(oY+1)]

for elem in outputDetour:
  for coordinates in elem:
    if coordinates[0]!=0:
      
      if coordinates[0]==1:
        answer1[coordinates[1]][coordinates[2]]=coordinates[0]
      if coordinates[0]==2:
        answer2[coordinates[1]][coordinates[2]]=coordinates[0]
      if coordinates[0]==3:
        answer3[coordinates[1]][coordinates[2]]=coordinates[0]
      if coordinates[0]==4:
        answer4[coordinates[1]][coordinates[2]]=coordinates[0]
      if coordinates[0]==5:
        answer5[coordinates[1]][coordinates[2]]=coordinates[0]
      if coordinates[0]==6:
        answer6[coordinates[1]][coordinates[2]]=coordinates[0]
      if coordinates[0]==7:
        answer7[coordinates[1]][coordinates[2]]=coordinates[0]
      if coordinates[0]==8:
        answer8[coordinates[1]][coordinates[2]]=coordinates[0]
      if coordinates[0]==9:
        answer9[coordinates[1]][coordinates[2]]=coordinates[0]
printMatrix(answer1,"Группы 1")
printMatrix(answer2,"Группы 2")
printMatrix(answer3,"Группы 3")
printMatrix(answer4,"Группы 4")
printMatrix(answer5,"Группы 5")
printMatrix(answer6,"Группы 6")
printMatrix(answer7,"Группы 7")
printMatrix(answer8,"Группы 8")
printMatrix(answer9,"Группы 9")
print(counter)


 
      

    
  
  

