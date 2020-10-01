from itertools import permutations

big="thisbigtext"
small=["this","igb","extt"]
data=[]
counter=0

for each in small:
    for eachInside in permutations(each,len(each)):
        if "".join(eachInside) in big:
            data.append("".join(eachInside)) 
    counter+=1
check=True
# remove duplicate permutations
data=list(set(data))
for each in permutations(data,len(data)):
    if "".join(each) == big:
        print("YES")
        check=False
if check:
    print("NO")
