numbers=list(map(int,input().split(" ")))
print(numbers)
counter=0
for i in numbers:
  if i%2==0:
    counter+=1
print(counter)