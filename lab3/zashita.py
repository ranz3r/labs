a= input()
for i in range(len(a)):
    if a[i]=="_":
        print(a[0:i]+a[i+1].upper() + a[i+2:len(a)])
