# entrada de dados
nome = input("Informe seu nome: ")
altura = float(input("Informe sua altura: "))
peso = float(input("Informe seu peso: "))

# vefirica o IMC do usuário
print(f" O seu IMC é: {peso/altura**2}.")

# estrutura match...case
match opcao:
    case "Menor que 16.9 ":
        print(f" Muito abaixo do peso.")
    case "17 a 18.4":
        print(f" Abaixo do peso.")
    case "18.5 a 24.9":
        print(f" Peso normal.")
    case "25 a 29.9":
        print(f" Acima do peso.")
    case "30 a 34.9"
        print("Obesidade grau I.")
    case "35 a 40"
        print("Obesidade grau II.")
    Case "Maior que 40"
        print("Obesidade grau III")