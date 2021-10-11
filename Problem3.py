lower = int(input("Enter start Value:"))
upper = int(input("Enter end Value:"))

o1 =[]
o2=[]
o3=[]
o4=[]
for i in range(lower, upper+1):
    if((i%3==0) or (i%5==0)):
      o1.append(i)
for i in range(lower, upper+1):
    if((i%3==0) & (i%5==0)):
      o2.append(i)
for i in range(lower, upper+1):
    if((i%3==0) & (i%5!=0)):
      o3.append(i)  
for i in range(lower, upper+1):
    if((i%3!=0) & (i%5==0)):
      o4.append(i)       
      
      
print(o1)
print(o2)
print(o3)
print(o4)

      