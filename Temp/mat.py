import matplotlib.pyplot as plt
import random
import math
data=[3, 12, 52, 55, 92, 97, 72, 47, 42, 69, 57, 90, 76, 61, 77, 34, 33, 71, 6, 100]
sortedd=[6, 12, 0, 0, 0, 0, 33, 42, 47, 52, 57, 61, 0, 71, 77, 0, 0, 90, 97, 100]
# for i in range(len(data)):
#     plt.plot(i,data[i])
# plt.scatter([i for i in range(len(data))],data)
# plt.plot([i for i in range(len(data))],data)
# plt.plot([i for i in range(len(data))],[(each-3)//5 for each in data])
# print(len(sortedd))
# # plt.plot([i for i in range(len(data))],sortedd)
# plt.show()
loss=[]
def return_gradient(start,end):
    return (end['y']-start['y'])//(end['x']-start['x'])
for ii in range(5):
    data=[random.randint(1,100) for i in range(random.randint(10,10))]
    length=len(data)
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
    copy=[{'x':i,'y':data[i]} for i in range(length)]
    m=return_gradient(copy[0],copy[length-1])
    m=m if m!=0 else 1
    print("-"*20)
    print("M : ",m)
    print("Length  :",length)
    print(data)
    X=[i for i in range(length)]
    line=[m*i+data[0] for i in range(length)]
    for i in range(1,length-1):
        expect=(copy[i]['y']-copy[0]['y'])//m if m!=0 else copy[i]['x']
        copy[i]['x']=expect
    answer=[0 for i in range(length)]
    for i in range(length):
        if copy[i]['x']<length:
            answer[copy[i]['x']]=copy[i]['y']
    print(answer)
    cnt=answer.count(0)
    print("data loss {} and {}%".format(cnt,(cnt*100)//length))
    loss.append([cnt,length])
    plt.plot([i for i in range(length)],[m*i+data[0] for i in range(length)])
    plt.plot([i for i in range(length)],data)
    plt.plot([i for i in range(length)],answer)
    plt.show()
    plt.figure(ii+1)
summer=0
summer2=0
for each in loss:
    avg=(each[0]*100)//each[1]
    summer+=each[0]
    summer2+=each[1]
    print("Total {} Loss {} Percentage {}%".format(each[1],each[0],avg))
print("Average - Total {} Loss {} Percentage {}%".format(summer2,summer,(summer*100)//summer2))