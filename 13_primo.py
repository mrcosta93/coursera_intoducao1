import math

def éPrimo(k):
    if k == 1:
        return False
    else:
        if k < 4:
            return True
        else:
            if k % 2 == 0:
                return False
            else:
                if k < 9:
                    return True
                else:
                    if k % 3 == 0:
                        return False
                    else:
                        r = math.floor(math.sqrt(k))
                        f = 5
                        while f <= r:
                            if k % f == 0:
                                return False
                            if k % (f+2) == 0:
                                return False
                            f = f+6
                        return True

def maior_primo(x):
    maior = 0
    for i in range(2, x+1):
        if éPrimo(i):
            maior = i
    return maior