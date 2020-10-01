import random
data=[{'x':i,'y':random.randint(1,100)} for i in range(100)]
length=len(data)

#finding minimum and pos
minPos,mini=0,data[0]['y']
for i in range(length):
    if(data[i]['y']<mini):
        mini=data[i]['y']
        minPos=i

#finding maximum value and pos
maxPos,maxer=0,data[0]['y']
for i in range(length):
    if(data[i]['y']>maxer):
        maxer=data[i]['y']
        maxPos=i

# placing maximum value at the end and minimum value at the start
if minPos!=0:
    data[0],data[minPos]=data[minPos],data[0]
if maxPos!=length-1:
    data[length-1],data[maxPos]=data[maxPos],data[length-1]

def return_gradient(start,end):
    return (end['y']-start['y'])//(end['x']-start['x'])
print(return_gradient(data[0],data[length-1]))