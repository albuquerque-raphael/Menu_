from time import sleep
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opcao = 0
while opcao != 5:
    print("""    [ 1 ] - Somar
    [ 2 ] - Multiplicar
    [ 3 ] - Maior
    [ 4 ] - Menor
    [ 5 ] - Sair do programa""")
    opcao = int(input("Qual opção deseja? "))
    sleep(0.8)
    if opcao == 1:
        soma = n1 + n2
        print("A soma entre {} e {} é igual a {}".format(n1, n2, soma))
        sleep(2)
    elif opcao == 2:
        produto = n1 * n2
        print("O resultado de {} X {} é {}".format(n1, n2, produto))
        sleep(2)        
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print("Entre {} e {} o maior valor é {}".format(n1, n2, maior))
            sleep(2)
    elif opcao == 4:
        if n1 > n2:
            menor = n2
        else:
            menor = n1
            print("Entre {} e {} o menor número é {}".format(n1, n2, menor))
            sleep(2) 
    elif opcao == 5:
        sleep(2)
        print("Finalizando... ... ...")
    else:
        print("Opção INVÁLIDA! Tente novamente")
    print("==-==-==" * 4)
print("Fim do programa. Volte sempre!")
