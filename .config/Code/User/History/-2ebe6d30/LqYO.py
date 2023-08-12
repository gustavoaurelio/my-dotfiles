idade = input("Digite sua idade: ")

if idade != int: print("Digite um numero inteiro")

maioridade = int(idade) >= 18

if maioridade == True:
      print("Voce é maior de idade!")
else: print("Voce não é maior de idade!")