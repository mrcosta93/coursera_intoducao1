def remove_repetidos(x):
    x.sort()
    a = 0
    b = 0
    while a < len(x):
        while b < len(x):
            if x[a] == x[b] and a != b:
                x.pop(b)
                b = 0
            b += 1
        b = 0
        a += 1
    return x

print(remove_repetidos([7,3,33,12,3,3,3,7,12,100]))