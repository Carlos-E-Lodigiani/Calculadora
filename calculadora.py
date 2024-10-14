
def FuncSoma(v1, v2):
    return v1 + v2

def FuncSub(v1, v2):
    return v1 - v2
    
def FuncMult(v1, v2):
    return v1 * v2

def FuncDiv(v1, v2):
    return v1 / v2
    
    

if __name__ == '__main__':  
        
    while True:  

        print('PROGRAMA CALCULADORA')

        print('Escolha a operação matemática:'
                '\n\n1- Adição '
                '\n2- Subtracao' 
                '\n3- Multiplicação' 
                '\n4- Divisão'
                )  
        opcao = ''
        while opcao not in (1, 2, 3, 4):
            print('Escolha uma das opcões acima!', end =' ')

            try:     
                opcao = int(input(''))
                continue  
            except ValueError:
                print('Escolha uma das opções acima!')


        try:         
            num1 = int(input('\nDigite o primeiro número: '))
            num2 = int(input('\nDigite o segundo número: '))
        
        except ValueError:
            print('Escolha um valor válido!')
                
            
        if opcao == 1:
            r = FuncSoma(num1, num2)
            print(f'\nA soma dos valores é: {r}\n' )
        elif opcao == 2:
            r = FuncSub(num1,num2)
            print(f'\nA subtração dos valores é: {r}\n')

        elif opcao == 3:
            r = FuncMult(num1, num2)
            print(f'\nA multilicação dos valores é: {r}\n')

        elif opcao == 4:
                try:
                    r = FuncDiv(num1, num2)
                except ZeroDivisionError:
                    print('Não é possivel dividir por zero\n')
                else:
                    print(f'\nA divisão dos valores é: {r}\n')

    resp = ''
    while resp not in 'SN':
        resp = int(input('Gostaria de continuar? [S/N]: ')).upper()
        if resp == 'N':
            break

            
        