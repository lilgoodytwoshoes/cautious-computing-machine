def pari():
    numeri = [numero for numero in range(1,200)]
    numeri_pari = []
    for numero in numeri:
        if numero % 2 == 0:
            numeri_pari.append(numero)
    return numeri_pari
numeri_pari = pari()
def dispari(numero):
    if numero < 2:
        return False
    for _ in range (2,numero):
        if numero%_==0:
            return False
    return True 
for numero in numeri_pari:
    if numero>2:
        for x in range(2,numero):
            y = numero - x
            if dispari(x) and dispari(y):
                print(numero, "=", x ,"+", y)