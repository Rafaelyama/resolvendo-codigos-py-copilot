# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?!

def concatena_strings():
    # Recebe as entradas do usuário
    dado1 = input("Digite o primeiro dado: ")
    dado2 = input("Digite o segundo dado: ")
    
    # Concatena os dois dados em uma única string
    resultado = f"{dado1} {dado2}"
    
    # Retorna ou exibe o resultado
    return resultado

# Executa a função e imprime o resultado
print(concatena_strings())
