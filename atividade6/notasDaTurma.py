'''4 - Crie um programa que permita a um professor registrar as notas de uma turma.
 O programa deve continuar solicitando notas até que o professor digite 'fim'.
Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando.
No final, deve exibir a média da turma.'''

def registrar_notas():
    notas = []

    while True:
        entrada = input("Digite a nota do aluno (0 a 10) ou 'fim' para encerrar: ").strip()

        if entrada.lower() == 'fim':
            break

        try:
            nota = float(entrada)

            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida: digite um valor entre 0 e 10.\n")
        except ValueError:
            print("Entrada inválida: digite um número válido ou 'fim' para sair.\n")

    if notas:
        media = sum(notas) / len(notas)
        print(f"\nNúmero de notas registradas: {len(notas)}")
        print(f"Média da turma: {media:.2f}")
    else:
        print("\nNenhuma nota válida foi registrada.")

# Chama a função
registrar_notas()
