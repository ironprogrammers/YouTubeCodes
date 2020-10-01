from random import randint
"""
total: sum of marks
minimum: minimum marks in each subject
maximum: maximum marks in each subject
numbers: total number of subjects
"""
def calc(total,minimum,maximum,numbers):
    data=[]
    i=0
    while sum(data)!=total:
        while(i<numbers):
            left=total-sum(data)
            maxer=left if left<maximum else maximum
            data.append(randint(minimum,maxer))
            i+=1
        if(sum(data)!=total):
            i=0
            data=[]
    return data
while True:
    try:
        total=int(input("Enter total marks : "))
        print(calc(total,30,90,5))
    except:
        continue

