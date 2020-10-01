import random

# creating dataset
data=[random.randint(1,100) for i in range(20)]
length=len(data)

#finding min and minPos
minPos,mini=0,data[0]
for i in range(length):
    if(data[i]<mini):
        mini=data[i]
        minPos=i

#finding maxer and maxPos
maxPos,maxer=0,data[0]
for i in range(length):
    if(data[i]>maxer):
        maxer=data[i]
        maxPos=i

#Swapping maxPos and element at end
if data[length-1]!=maxer and maxPos!=length-1:
    data[maxPos],data[length-1]=data[length-1],data[maxPos]
#swapping minPos and element at start
if data[0]!=mini and minPos!=0:
    data[minPos],data[0]=data[0],data[minPos]

#Create a 2D cartesian array
copy=[{'x':i,'y':data[i]} for i in range(length)]


def return_gradient(start,end):
    return (end['y']-start['y'])//(end['x']-start['x'])

m=return_gradient(copy[0],copy[length-1])
print(data)
print(copy)
print("M :",m)
for i in range(1,length-1):
    x= (copy[i]['y']-copy[0]['y'])//m if m!=0 else copy[i]['y']
    print(copy[i]['x'],copy[i]['y'],x)
    copy[i]['x']=x
answer=[0 for i in range(length)]
for i in range(length):
    answer[copy[i]['x']]=copy[i]['y']
print(answer)
print(data)