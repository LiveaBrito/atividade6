'''1 - Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração,
multiplicação e divisão) entre dois números. A calculadora deve ser capaz de lidar com diversos
tipos de erros de entrada e operação. Siga as especificações abaixo:

A calculadora deve solicitar ao usuário que insira dois números e uma operação.
As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).
O programa deve continuar solicitando entradas até que uma operação válida seja concluída.
Trate os seguintes erros:
Entrada inválida (não numérica) para os números
Divisão por zero
Operação inválida
Use try/except para capturar e tratar os erros apropriadamente.
Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.
Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa'''

def calculadora():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            
            num2 = float(input("Digite o segundo número: "))
            
            operacao = input("Digite a operação (+, -, *, /): ").strip()
            
            # Verificando se a operação é válida
            if operacao not in ['+', '-', '*', '/']:
                print("Operação inválida! Tente novamente.\n")
                continue

            # Verificando a divisão por zero
            if operacao == '/' and num2 == 0:
                print("Erro: Divisão por zero não é permitida.\n")
                continue

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                resultado = num1 / num2

            print(f"\nResultado: {num1} {operacao} {num2} = {resultado}")
            break  # Sai do loop após operação bem-sucedida

        except ValueError:
            print("Erro: Por favor, insira apenas números válidos.\n")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}\n")

calculadora()
