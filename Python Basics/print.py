# printf("%d",a) placeholders 
# Basic print
print(True)
print(28,90)
print("{} hello".format(5))
print("hello"+"World!")
print(28+90)

# Values or parameters
#print(object, sep="",end="",file=fileobject,flush=True/False)
# sep=" "
print(28,90,sep="@")
#end="\n"
print("hello",end="#")
print("bye",end="\n")
fileObj=open("temp.txt","w")
print("This is from the print.py",file=fileObj)
fileObj.close()