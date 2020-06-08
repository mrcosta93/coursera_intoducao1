lmax = int(input("digite a largura: "))
hmax = int(input("digite a altura: "))
l = 0
h = 0

while h < hmax:
    while l < lmax:
        if h > 0 and h < hmax-1 and l > 0 and l < lmax-1:
            print(" ", end="")
        else:
            print("#", end="")
        l += 1
    print("")
    l = 0
    h += 1