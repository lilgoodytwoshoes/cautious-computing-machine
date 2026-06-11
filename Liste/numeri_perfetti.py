while True:
    numero =int(input("Dammi un numero: "))
    def divisori(numero):
        divisorioni = []
        metà_numero=int(numero/2)+1
        for num in range(1,metà_numero):
            if numero % num == 0:
                divisorioni.append(num)
        return divisorioni

    divisorioni = divisori(numero)
    somma = sum(divisorioni)
    if somma == numero:
        print("Perfetto!")
    else:
        print("Non perfetto.")
