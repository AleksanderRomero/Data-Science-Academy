# Calculadora em Python

print("\n******************* Calculadora em Python *******************")

print("\nSelecione o número da operação desejada: \n\n  1- Soma \n  2- Subtração \n  3- Multiplicação \n  4- Divisão")

operacao = input("Digite sua opção (1/2/3/4):")

numero1 = input("Digite o primeiro número:")

numero2 = input("Digite o segundo número:")

if operacao == "1":
    resultado = int(numero1) + int(numero2)
    print(resultado)

elif operacao == "2":
    resultado = int(numero1) - int(numero2)
    print(resultado)

elif operacao == "3":
    resultado = int(numero1) * int(numero2)
    print(resultado)

elif operacao == "4":
    resultado = int(numero1) / int(numero2)
    print(resultado)
    
else:
    print("\nOpção Inválida!")

