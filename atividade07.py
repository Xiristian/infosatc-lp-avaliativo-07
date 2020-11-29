for i in range(10):
    calculaMedia = lambda n1, n2: n1 + n2

    def validaConceito(nota):

        if nota < 5:
            return "D"
        elif nota < 7:
            return "C"
        elif nota < 9:
            return "B"
        else:
            return "A"

    nota1 = float(input("Digite a 1ª nota: "))
    nota2 = float(input("Digite a 2ª nota: "))
    media = calculaMedia(nota1,nota2)
    conceito = validaConceito(media)

    print("Media: ", media, "\nConceito: ", conceito)