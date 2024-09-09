# Vamos testar se uma palavra é um palíndromo?! 
# Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

def verifica_palindromo():
    # Solicita uma palavra do usuário
    palavra = input("Digite uma palavra para verificar se é um palíndromo: ").strip()
    
    # Remove espaços e converte para minúsculas para uma comparação mais robusta
    palavra = palavra.replace(" ", "").lower()
    
    # Inverte a palavra
    palavra_invertida = palavra[::-1]
    
    # Verifica se a palavra original é igual à palavra invertida
    if palavra == palavra_invertida:
        return f"A palavra '{palavra}' é um palíndromo."
    else:
        return f"A palavra '{palavra}' não é um palíndromo."

# Executa a função e imprime o resultado
print(verifica_palindromo())
