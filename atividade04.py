numeros  = []

for i in range(10):
    numeros.append(int(input("Digite o {}º número: ".format(i + 1))))


pares = filter(lambda i: i % 2 == 0, numeros)
print("Pares:", list(pares))

impares = filter(lambda i: i % 2 == 1, numeros)
print("Impares:", list(impares))
