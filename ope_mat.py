# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

def operacao_simples():
    try:
        # Solicita dois números como entrada do usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        # Solicita que o usuário escolha a operação
        print("Escolha a operação matemática:")
        print("1 - Soma (+)")
        print("2 - Subtração (-)")
        print("3 - Multiplicação (*)")
        print("4 - Divisão (/)")
        
        operacao = input("Digite o número correspondente à operação desejada: ")
        
        # Realiza a operação com base na escolha do usuário
        if operacao == '1':
            resultado = num1 + num2
            return f"O resultado da soma: {num1} + {num2} = {resultado}"
        
        elif operacao == '2':
            resultado = num1 - num2
            return f"O resultado da subtração: {num1} - {num2} = {resultado}"
        
        elif operacao == '3':
            resultado = num1 * num2
            return f"O resultado da multiplicação: {num1} * {num2} = {resultado}"
        
        elif operacao == '4':
            if num2 != 0:
                resultado = num1 / num2
                return f"O resultado da divisão: {num1} / {num2} = {resultado}"
            else:
                return "Erro: Não é possível dividir por zero."
        
        else:
            return "Operação inválida. Por favor, escolha uma operação válida."
    
    except ValueError:
        return "Erro: Por favor, insira valores numéricos válidos."

# Executa a função e imprime o resultado
print(operacao_simples())
