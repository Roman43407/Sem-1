
fib1 = fib2 = 1

n = int(input("Liczba Fibonacciego: ")) - 2

while n > 0:
    fib1, fib2 = fib2, fib1 + fib2
    n -= 1

print(fib2)
'''
n1 = 1
n2 = 1
n3 = n1 + n2
for i in range(10):
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3
'''