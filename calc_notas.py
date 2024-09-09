# Agora vamos calcular a média de três notas fornecidas na entrada do usuário. 
# Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.

def calcula_media_e_classifica():
    try:
        # Solicita três notas do usuário
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
        
        # Calcula a média aritmética
        media = (nota1 + nota2 + nota3) / 3
        
        # Classifica o desempenho baseado na média
        if media > 6:
            status = "Aprovado"
        elif media == 6:
            status = "Recuperação"
        else:
            status = "Reprovado"
        
        # Retorna o resultado da média e a classificação
        return f"A média das notas é: {media:.2f}. Status: {status}"
    
    except ValueError:
        return "Erro: Por favor, insira valores numéricos válidos para as notas."

# Executa a função e imprime o resultado
print(calcula_media_e_classifica())
