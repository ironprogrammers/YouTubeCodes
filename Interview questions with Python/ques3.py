#conditionals -> if else, switch, ternary

def testNumber(num):
    ((num%2 and print("Odd")==None or print("Even")))
testNumber(int(input()))
# 1 and 1 -> 1
# 1 or 0 -> 1
#False or print("Checked")
def testNumber2(num):
    print(["even","odd"][num%2])
testNumber2(int(input()))