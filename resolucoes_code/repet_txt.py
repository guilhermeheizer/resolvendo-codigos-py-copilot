# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2

print(f"A soma dos dois números é: {soma}")

texto = input("Digite uma string: ")
repeticoes = int(input("Digite o número de repetições: "))

resultado = texto * repeticoes

print(f"A string repetida é: {resultado}")

print("Palíndromo é uma palavra, frase ou número que permanece igual quando lida de trás para frente.")
print("Exemplos: 'arara', 'radar', 'osso', 'reviver', 'Ana'.")

palavra = input("Digite uma palavra para verificar se é um palíndromo: ")
if palavra.lower() == palavra[::-1].lower():
    print(f"'{palavra}' é um palíndromo!")
else:
    print(f"'{palavra}' não é um palíndromo.")