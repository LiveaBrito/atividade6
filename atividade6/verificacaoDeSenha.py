'''3 - Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter
pelo menos 8 caracteres e conter pelo menos um número. O programa deve continuar pedindo
senhas até que uma válida seja inserida ou o usuário digite 'sair'.'''

def verificar_senha():
    while True:
        senha = input("Digite uma senha forte ou 'sair' para encerrar: ").strip()

        if senha.lower() == 'sair':
            print("Programa encerrado.")
            break

        if len(senha) < 8:
            print("Senha fraca: deve ter pelo menos 8 caracteres.\n")
            continue

        if not any(char.isdigit() for char in senha):
            print("Senha fraca: deve conter pelo menos um número.\n")
            continue

        print("Senha forte! ✔️")
        break

# Chama a função
verificar_senha()
