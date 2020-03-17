#Given a string A and a dictionary of words B, determine if A can be segmented into a space-separated sequence of one or more dictionary words.

a=input()
b=["hello","sir","bye"]
def check(a,b):
    for each in b:
        if each not in a:
            return False
    return True
print(check(a,b))