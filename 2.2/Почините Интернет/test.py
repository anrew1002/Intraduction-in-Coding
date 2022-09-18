a= [4,4,3,2,1,5,6]
print(a.count(4))
for h in range(a.count(4)):
    a[a==4]=0
print(a)
