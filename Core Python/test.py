# [1,2,3,4,1,4]
# 1 2
# 2 1
# 3 1
# 4 1
arr=[1,2,3,4,1,4]
result={}
for each in arr:
    result.update({each:arr.count(each)})
for (a,b) in result.items():
    print(a,b)
