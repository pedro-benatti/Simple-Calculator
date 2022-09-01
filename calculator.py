
while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador(+,-,* ou /): ')


    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Digite apenas números na calculadora')
        continue


    num_1=int(num_1)
    num_2=int(num_2)

    if operador == '+':
        print( 'O resultado é:', num_1 + num_2)
    elif operador == '-':
        print('O resultado é:',num_1-num_2)
    elif operador == '*':
        print('O resultado é:',num_1 * num_2)
    elif operador == '/':
        print('O resultado é:',num_1/num_2)
    else:
        print('Operador inválido')

    sair = input('Digite C para continuar usando ou S para sair: ')
    if sair== 's':
        print('Obrigado por usar!')
        break