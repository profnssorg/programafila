"""
Programa Fila
Descrição:  Este programa controla as fichas de atendimento de uma fila.
Autor: Nelson Seixas dos Santos
Versão: 0.0.1
Data: 23/05/2018
"""

# Inicialização de variáveis

ficha = 1 # Este é o número do primeiro cliente a ser atendido.
operacao = ''
clientes = [ ] # Esta variável armazena o tamanho da fila.
atendidos = 0 # Esta variável armazena o número total de clientes atendidos.

# Fluxo de execução

while True:
    print('O tamanho atual da fila é: ', len(clientes))
    operacao = input("Pressione 'A' para atender um novo cliente; 'I' para adicionar um cliente à fila ou 'E' para encerrar o atendimento:  ")
    if operacao == 'A':
        if clientes == []:
            print('Não há clientes na fila! O sistema de atendimento está bloqueado.')
        else:
            clientes.pop(0)
            atendidos+=1
            print('O número total de clientes atendidos até o momento foi: ', atendidos )
            
    elif operacao == 'I':
        clientes+=[ficha]
        ficha+=1
        
    elif operacao == 'E':
        print('Atendimento encerrado')
        print('O número total de clientes atendidos foi: ', atendidos )
        print('Restaram %d clientes não atendidos na fila'%len(clientes))
        #relatorio = open('relatorio.txt','w')
        #relatorio.close()
        break
    elif operacao != 'A' or 'E' or 'I':
        print('Esta não é uma operação válida.  Tente novamente.')
        