while True:
    print("\n--- CALCULADORA ---")

    entrada1 = input("Digite o primeiro numero ou 'sair': ")

    if entrada1 == "sair":
        print("Programa encerrado.")
        break

    num1 = float(entrada1.replace(",", "."))

    operacao = input("Digite a operação (+, -, *, /) ou 'sair': ")

    if operacao == "sair":
        print("Programa encerrado.")
        break

    entrada2 = input("Digite o segundo numero ou 'sair': ")

    if entrada2 == "sair":
        print("Programa encerrado.")
        break

    num2 = float(entrada2.replace(",", "."))

    if operacao == "+":
        print("Resultado:", num1 + num2)

    elif operacao == "-":
        print("Resultado:", num1 - num2)

    elif operacao == "*":
        print("Resultado:", num1 * num2)

    elif operacao == "/":
        if num2 == 0:
            print("Não é possivel dividir por 0")
        else:
            print("Resultado:", num1 / num2)

    else:
        print("Operação inválida!")
