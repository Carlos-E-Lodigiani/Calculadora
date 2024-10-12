while True:

    opcao = int(input('Escolha a operação matemática:'
                  '\n\n1- Adição '
                  '\n2- Subtracao' 
                  '\n3- Multiplicação' 
                  '\n4- Divisão'
                  '\n\nEscolha umas das opções acima: '   ))
 
    
    
    
    if opcao > 4:
        print('\nOpção inválida!')
    
    else:

        num1 = int(input('\nDigite o primeiro número: '))

        num2 = int(input('\nDigite o segundo número: '))


        def FuncSoma(v1, v2):
            return v1 + v2

        def FuncSub(v1, v2):
            return v1 - v2
            
        def FuncMult(v1, v2):
            return v1 * v2
       
        def FuncDiv(v1, v2):
            if v2 != 0:
                return v1 / v2
            else:
                print('\nNão é possível divisão por 0!')
                
        


        if opcao == 1:
            print('\nA soma dos valores é: ', FuncSoma(num1, num2))

        elif opcao == 2:
            print('\nA subtração dos valores é: ', FuncSub(num1, num2))

        elif opcao == 3:
            print('\nA multilicação dos valores é: ', FuncMult(num1, num2))

        elif opcao == 4:
             print('\nA divisão dos valores é: ', FuncDiv(num1, num2))
            
        