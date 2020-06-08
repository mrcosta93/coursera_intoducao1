lmax = int(input("digite a largura: "))
hmax = int(input("digite a altura: "))
l = 0
h = 0

while h < hmax:
    while l < lmax:
        print("#", end="")
        l += 1
    print("")
    l = 0
    h += 1