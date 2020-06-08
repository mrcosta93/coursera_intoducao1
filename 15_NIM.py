def computador_escolhe_jogada(n, m):
    tira = 1
    while (n-tira) % (m+1) != 0 and tira < m:
            tira += 1
    n -= tira
    print("")
    print("O computador tirou", tira, "peça(s)")
    print("Ainda resta(m)", n, "peça(s)")
    return tira
    
def usuario_escolhe_jogada(n, m):
    print("")
    tira = int(input("Quantas peças você vai tirar? "))
    while tira < 1 or tira > m:
        print("")
        tira = int(input("Quantas peças você vai tirar? "))
    n -= tira
    print("")
    print("Você tirou", tira, "peça(s)")
    print("Ainda resta(m)", n, "peça(s)")
    return tira
    
def partida():
    p = 0
    while p == 0:
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        if n > m:
            p = 1

    print("")
    if n%(m+1) != 0:
        print("Computador começa!")
        n -= computador_escolhe_jogada(n, m)
        a = 0
    else:
        print("Você começa!")
        n -= usuario_escolhe_jogada(n, m)
        a = 1
    while n > 0:
        if a == 0:
            n -= usuario_escolhe_jogada(n, m)
            a = 1
        else:
            n -= computador_escolhe_jogada(n, m)
            a = 0
    print("")
    print("Fim de jogo")
    if a == 0:
        print("O computador ganhou!")
        print("")
        return True
    else:
        print("Você ganhou!")
        print("")
        return False

def campeonato():
    computador = 0
    usuario = 0
    i = 1
    while i < 4:
        print("**** Rodada ", i, " ****")
        if partida():
            computador += 1
        else:
            usuario += 1
        i += 1
    print("Placar: Você ", usuario, " X ", computador, " Computador")

print("Bem-vindo ao jogo do NIM! Escolha:")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")
print("")
x = int(input())
print("")
if x == 1:
    partida()
elif x == 2:
    campeonato()