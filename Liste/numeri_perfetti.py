numero = input("Dammi un numero: ")
numero = int(numero)
def divisori(numero):
    divisorioni = []
    for num in range(1, numero):
        if numero % num == 0:
            divisorioni.append(num)
    return divisorioni

divisorioni = divisori(numero)
somma = sum(divisorioni)
if somma == numero:
    print("Perfetto!")
else:
    print("Non perfetto.")
