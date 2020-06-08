x = int(input())
fatorial = 1
n = 1
if x == 0:
    fatorial = 1
else:
    while n <= x:
        fatorial = fatorial * n
        n += 1

print(fatorial)