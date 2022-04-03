import copy
import graphviz
class graph_Matrix():
    def __init__(self,list1):
        self.matrix=[]
        self.naming=list(map(lambda x: x.strip() , list1[0][1:]))
        for i in range(1,len(list1)):
            self.matrix.append(list(map(int,a[i][1:])))
            
        self.set_path()
        
    def __str__(self):
        return self.output_Matrix(self.matrix)
    def __repr__(self):
        return self.output_Matrix(self.matrix)
    
    def set_path(self):
        self.path=[]
        self.path=copy.deepcopy(self.matrix)
        counter=0
        while counter < len(self.path):
            for i in range(len(self.path)):
                for j in range(len(self.path[0])):
                    if (self.path[i][counter]!=0) and (self.path[counter][j]!=0):
                        if self.path[i][j] > self.path[i][counter]+self.path[counter][j] or self.path[i][j]==0 :
                            self.path[i][j] = self.path[i][counter]+self.path[counter][j]
            counter+=1
        return self.output_Matrix(self.path)
    
    def output_Matrix(self,list1):
        output="  "
        output+=", ".join(self.naming) +" \n"
        for i in range(len(list1)):
            output+= str(self.naming[i])+" "+str(list1[i])[1:-1] + " \n"
        return output
    def edit_Matrix(self, param, i,j):
        self.matrix[i][j]=param
        self.set_path()
    def get_path(self, start,finish):
        counter=0
        for i in range(len(self.naming)):
            if start==self.naming[i]:
                lineStart=i
                counter+=1
                continue
            elif finish == self.naming[i]:
                columnFinish=i
                counter+=1
                continue
        if counter!=2:
            print("Ошибка")
            return
        output=self.path[lineStart][columnFinish]
        if output==0:
            output=min(filter(lambda x: (x!=0),self.path[columnFinish]))
        return output
    
#основан на алгоритме Флойда + парочка функций для интереса
def FileReaderMatrix(name):
  a=[]
  f=open(name,"r").readlines()
  for line in f:
    a.append(list(line.split(" ")))
  return a

a=[[0, "A","B","C","D"],
   ["A",0,  1,  6,  0],
   ["B",0,  0,  4,  1],
   ["C",0,  0,  0,  0],
   ["D",0 , 0,  1,  0]]
a=FileReaderMatrix("input.txt")
print("\n")
graph=graph_Matrix(a)
#graph.edit_Matrix(3,1,0)
print(graph)
print(graph.set_path())






