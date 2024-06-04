import math

opcao1 = 0

def exibir_menu():
    print('\n1 - Equação do 1o grau')
    print('2 - Equação do 2o grau')
    print('3 - Sair do Programa')
    
def calcular_equacao1(a, b, c):
    x = (c - b) / a
    return x

def calcular_equacao2(a, b, c): #Função para obtenção dos valores.
    delta = (b**2 - 4*a*c) #Calculo do Delta
    yield delta
    x1 = (-b + delta**(1/2)) / (2*a) 
    yield x1
    x2 = (-b - delta*(1/2)) / (2*a) 
    yield x2

while True:
    exibir_menu()

    opcao1 = int(input('\nEscolha a opção desejada (1 a 3):\n'))

    match opcao1:
        case 1:
            print('Equação do 1o Grau: ax + b = c')
            a = int(input('Informe o valor de a: '))
            b = int(input('Informe o valor de b: '))
            c = int(input('Informe o valor de c: '))
            print(f'Equação do 1o Grau (valor de X): {calcular_equacao1(a, b, c)}')
            continue
 
        case 2:
            print('Equação do 2o Grau:')
            a = int(input('Informe o valor de a: '))
            b = int(input('Informe o valor de b: '))
            c = int(input('Informe o valor de c: '))
            if (b == 0 or c == 0):
                print('Equação Incompleta') 

            resultados = calcular_equacao2(a, b, c)
         
            print(f'O valor de Delta é {next(resultados)}.')
            delta = (b**2 - 4*a*c) #Calculo do Delta
            if delta > 0:    
                print(f'O valor de x1 é {next(resultados)}.')    
                print(f'O valor de x2 é {next(resultados)}.')    
            else:
                 print('Não possui raízes reais')
            continue
        
        case 3:
            break
 
        case _:
            print('Opção Inválida!')
            continue        