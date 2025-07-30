import random
nome = input("Digite o nome de uma pessoa: ")
nome2 = input("Digite o nome de outra pessoa: ")
nome3 = input("Digite o nome de mais uma pessoa: ")
nome4 = input("Digite o nome de mais uma pessoa: ")
lista = [nome, nome2, nome3, nome4]
print("O nome escolhido foi {}".format(random.choice(lista)))
