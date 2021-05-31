n = int(input("Enter the digit :"))
for i in range(n):
    a,b,k = (map(int , input().split()))
    if a >= b:
        print(k//b)
    else:
        print(k//a)