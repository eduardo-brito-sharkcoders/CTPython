# Variáveis

# Syntax:
# <nome_variavel> = <valor>
variavel = "Olá"

# Tipos:
variavel_str = "Olá Mundo!"
variavel_int = 1
variavel_float = 3.14
variavel_bool = True # ou False

# Operadores Aritméticos

soma = 1 + 1
subtr = 1 - 1
multip = 1 * 1
divisao = 1 / 1
potencia = 1 ** 1
resto = 1 % 1

# Operadores Condicionais

# > maior que
# < menor que
# >= maior ou igual que
# <= menor ou igual que
# != diferente de

# and - E
# or - OU
# not - Negação

# Imprimir valores
print("Olá")

# Receber Valores
variavel_utilizador = input("Insira um valor: ")

# format()
print(f"Olá {variavel_utilizador}")

# If .. Elif .. Else
if "condicao1":
    pass
elif "condicao2":
    pass
else:
    pass

# Módulos
# import <modulo>

# Loops (Ciclos)
while "condicao":
    pass

for iterador in lista:
    pass

# Listas
lista = ["amarelo", "vermelho", "azul"] # os elementos podem ser alterados

print(lista[2])

lista[2] = "verde"

# Tuplos
tuplo = (1, 2, 3) # os elementos NÃO podem ser alterados

# Funções

def dizer_ola():
    print("Olá")

dizer_ola()

def dizer_ola_nome(nome):
    print(f"Olá {nome}")

dizer_ola_nome("Ze")

def soma(n1, n2):
    return n1 + n2

