#The Fibonacci Sequence is the series of numbers :

n1 = int(input())
n2 = int(input())
a = 1
b = 1
c = a+b
print(a,b, end = " ")
while c < n2:
    print(c, end =" ")
    a = b
    b = c
    c = a+b
