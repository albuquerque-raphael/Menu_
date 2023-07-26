while True:
    print("Escolha um tema: [1 - Frutas], [2 - Continentes], [3 - Carros]")
    tema = input("Qual tema você escolhe? ")

    if tema == "1":
        arquivo = open(file="1-Frutas.txt", mode="r", encoding="UTF-8")
        1-Frutas = []
        for line in arquivo:
            line = line.strip()
            1-Frutas.append(line)
        print("Frutas")
    elif tema == "2":
        print("Continentes")
    elif tema == "3":
        print("Carros")
    else:
        print("Escolha inválida!")
        break
