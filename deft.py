n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opcao = 0
while opcao != 5:

    print("""
          [ 1 ] - Somar 
          [ 2 ] - Multiplicar 
          [ 3 ] - Maior 
          [ 4 ] - Novos números 
          [ 5 ] - Sair do programa""")
    opcao = int(input(">>>>>>>>>>>Qual é a sua opção? "))
    if opcao == 1:
        soma = n1 + n2
        print("A soma de {} e {} é igual a {}".format(n1, n2, soma))    
    elif opcao == 2:
        produto = n1 * n2
        print("O produto de {} e {} é igual a {}".format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            print("{} é maior que {}".format(n1, n2))
        else:
            print("{} é maior que {}".format(n2, n1))   
    elif opcao == 4:
        print("Informe os números novamente.")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))    
    elif opcao == 5:
        print("Finalizando... ")    
    else:
        print("Opção INVÁLIDA!")
    print("-=" * 15)
print("Fim do programa, volte sempre!")
