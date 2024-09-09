# Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. 
# Uma dica é: Utilize condicionais para realizar a verificação e, se possível, 
# faça uso do Github Copilot(ou outra IA) para otimizar a estrutura do código.

def verifica_par_ou_impar():
    try:
        # Solicita um número inteiro do usuário
        numero = int(input("Digite um número inteiro: "))
        
        # Verifica se o número é par ou ímpar usando o operador de módulo
        if numero % 2 == 0:
            return f"O número {numero} é par."
        else:
            return f"O número {numero} é ímpar."
    
    except ValueError:
        return "Erro: Por favor, insira um número inteiro válido."

# Executa a função e imprime o resultado
print(verifica_par_ou_impar())
