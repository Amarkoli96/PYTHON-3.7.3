def myfunc(god):
    i=1
    total=" "
    for item in god:
        if(i%2==0):
            i=i+1
            total+=item.lower()
        else:
            i+=1
            total+=item.upper()
    return total

print(myfunc("hello"))


output
print(myfunc("welcome to programming"))
 WeLcOmE To pRoGrAmMiNg
