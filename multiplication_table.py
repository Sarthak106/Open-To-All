print("*"*40)
print()
print("Welcome to program to print tables")
print()
print("*"*40)
print()
print("1. To print table.")
print("2. To exit ")
print()
ch=int(input("Choose option: "))
print()

if ch==1:
    n=int(input("Enter a number: "))

    for i in range(1,(n+1)):
        print("\nMULTIPLICATION TABLE FOR %d\n" %(i))
        for j in range(1,11):
            print("%-5d X %5d = %5d" % (i, j, i*j))
elif ch==2:
    print("Thankyou")
    pass
else:
    print("Choose correct option ")