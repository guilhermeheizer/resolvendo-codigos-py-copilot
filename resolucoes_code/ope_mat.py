# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicita dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realiza uma operação simples (soma)
resultado = num1 + num2

# Exibe o resultado
print(f"O resultado da soma é: {resultado}")

numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3

    print(f"A média das três notas é: {media:.2f}")

    while True:
        print("\nCalculadora Simples")
        print("Operações disponíveis:")
        print("1 - Adição (+)")
        print("2 - Subtração (-)")
        print("3 - Multiplicação (*)")
        print("4 - Divisão (/)")
        print("Digite 'sair' para encerrar.")

        operacao = input("Escolha a operação (1/2/3/4 ou sair): ").strip().lower()
        if operacao == "sair":
            print("Encerrando a calculadora.")
            break

        try:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Tente novamente.")
            continue

        if operacao == "1" or operacao == "+":
            resultado = n1 + n2
            print(f"Resultado: {n1} + {n2} = {resultado}")
        elif operacao == "2" or operacao == "-":
            resultado = n1 - n2
            print(f"Resultado: {n1} - {n2} = {resultado}")
        elif operacao == "3" or operacao == "*":
            resultado = n1 * n2
            print(f"Resultado: {n1} * {n2} = {resultado}")
        elif operacao == "4" or operacao == "/":
            if n2 == 0:
                print("Erro: divisão por zero não é permitida.")
            else:
                resultado = n1 / n2
                print(f"Resultado: {n1} / {n2} = {resultado}")
        else:
            print("Operação inválida. Tente novamente.")