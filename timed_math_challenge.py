import random # Importa o módulo 'random' para gerar números e operadores aleatórios.
import time # Importa o módulo 'time' para medir o tempo de execução do quiz.

# Constantes que definem os operadores e limites dos operandos
OPERATORS = ["+", "-", "*"] # Lista de operadores que serão utilizados nas expressões matemáticas.
MIN_OPERAND = 3  # Valor mínimo para os números gerados nas expressões.
MAX_OPERAND = 12 # Valor máximo para os números gerados nas expressões.
TOTAL_PROBLEMS = 10 # Número total de problemas que serão apresentados ao usuário.


def generate_problem(): # Gera um problema matemático aleatório.
    left = random.randint(MIN_OPERAND, MAX_OPERAND) # Gera um número aleatório para o operando esquerdo.
    right = random.randint(MIN_OPERAND, MAX_OPERAND) # Gera um número aleatório para o operando direito.
    operator = random.choice(OPERATORS) # Seleciona um operador aleatório da lista OPERATORS.

    expr = str(left) + " " + operator + " " + str(right) # Cria a expressão matemática como uma string.
    answer = eval(expr) # Calcula o resultado da expressão usando a função eval().
    return expr, answer # Retorna a expressão e sua resposta correta.



wrong = 0 # Variável que armazena o número de respostas incorretas (não utilizada nesse exemplo, mas pode ser usada para melhorias futuras).
input("Press enter to start!" ) # Aguarda o usuário pressionar Enter para começar.
print("----------------------") # Imprime uma linha divisória para organização visual.

start_time = time.time() # Captura o tempo de início do quiz.

for i in range(TOTAL_PROBLEMS): # Loop principal para gerar e apresentar os problema
    expr, answer = generate_problem() # Gera um novo problema.
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ") # Solicita ao usuário que insira sua resposta para o problema atual.
        if guess == str(answer): # Verifica se a resposta do usuário está correta.
            break # Sai do loop se a resposta estiver correta.


end_time = time.time() # Captura o tempo de término do quiz.
total_time = round(end_time - start_time, 2) # Calcula o tempo total em segundos, arredondando para 2 casas decimais.

print("----------------------")
print("Nice work! You finish in", total_time, "seconds!") # Exibe uma mensagem de conclusão e o tempo total gasto.