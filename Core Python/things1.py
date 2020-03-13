a=[1,2,3] #ABD
# b=a #alias #b->ABD
# b.append(5)
# print(a,b)
# # a=1,2,3,5
# # b=1,2,3,5
# b=list(a) #shallow copy not ABD
# b.append(5)
# print(a,b)
a2=[[1,2],3,4] #ABD 223
# b=list(a2) #ABD2
# b[0].append(5)
# print(a2,b)
# # a=[[1,2],3,4]
# # b=[[1,2,5],3,4]
import copy
b=copy.deepcopy(a2)
b[0].append(5)
print(a2,b)


