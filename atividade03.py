numeros  = []

for i in range(5):
    numeros.append(int(input("Digite o {}º número: ".format(i + 1))))


maiores = filter(lambda i: i > 10, numeros)
print("Maiores que 10:", list(maiores))
