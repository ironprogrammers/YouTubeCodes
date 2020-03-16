# fuzz buzz number
# 3 -> fuzz 
# 5 buzz
# fuzz buzz
# number itself
def fuzzBuzz(number):
    # if number%3==0:
    #     print("fuzz")
    # elif number%5==0:
    #     print("buzz")
    # elif number%5==0 and number%3==0:
    #     print("fuzzbuzz")
    # else:
    #     print(number)
    if number%5==0 and number%3==0:
        print("fuzzbuzz")
    elif number%5==0:
        print("buzz")
    elif number%3==0:
        print("fuzz")
    else:
        print(number)
# Bottom to top
while True:
    fuzzBuzz(int(input()))