# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado. 

def repetir_string():
    try:
        # Solicita uma string do usuário
        texto = input("Digite a string que deseja repetir: ")
        
        # Solicita um número inteiro do usuário
        repeticoes = int(input("Digite o número de repetições: "))
        
        # Verifica se o número de repetições é positivo
        if repeticoes < 0:
            return "Erro: O número de repetições deve ser maior ou igual a zero."
        
        # Retorna a string repetida o número de vezes informado
        return (texto + " ") * repeticoes
    
    except ValueError:
        return "Erro: Por favor, insira um número inteiro válido."

# Executa a função e imprime o resultado
print(repetir_string())
