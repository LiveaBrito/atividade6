'''2 - Crie um programa que solicite ao usuário que insira números inteiros.
O programa deve continuar solicitando números até que o usuário digite 'fim'.
Para cada número inserido, o programa deve informar se é par ou ímpar.
Se o usuário inserir algo que não seja um número inteiro, o programa deve informar
o erro e continuar. No final, o programa deve exibir a quantidade de números pares e ímpares inseridos.'''

def par_ou_impar():
    pares = 0
    impares = 0

    while True:
        entrada = input("Digite um número ou 'fim' para enerrar: ").strip()

        if entrada.lower() == "fim":
            break

        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print(f"{numero} é Par.\n")
                pares += 1
            else:
                print(f"{numero} é Ímpar.\n")
                impares += 1
        except ValueError:
            print("Erro: Por favor digite apenas números inteiros ou 'fim' para sair.\n")

    print("\nPrograma encerrado.")
    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")

# Chama a função
par_ou_impar()