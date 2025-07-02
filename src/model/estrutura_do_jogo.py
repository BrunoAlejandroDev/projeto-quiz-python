
#* Importacoes Gerais
import json
import os
import time

def carregar_perguntas(materia: str) -> list:
    """
    Carrega as perguntas de um arquivo JSON baseado na matéria escolhida.
    Args:
        materia (str): O nome da matéria (ex: 'filosofia'), que corresponde ao nome do arquivo sem a extensão .json.
    Returns:
        list: Uma lista de dicionários com as perguntas, ou uma lista vazia se o arquivo não for encontrado.
    """  
    
    #* Arquivo de cada materia 
    caminho_arquivo = os.path.join('data', f'{materia}.json')
    
    #* Ler o arquivo
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo: # lê o arquivo e converte o conteudo JSON em objeto Python
            perguntas = json.load(arquivo) # salva o conteudo em uma variavel
        return perguntas
    except FileNotFoundError: # arquivo não existir
        print(f'Erro: O arquivo de perguntas para a materia {materia} não existe')
        return []
    except json.JSONDecodeError: # arquivo JSON com formatacao invalida
        print(f'Erro: o arquivo da materia {materia} parece estar com dados corrompidos')

def mostrar_pontuação(pontuacao):
    print('\n=== Pontuação ===')
    print(f'Pontuação = {pontuacao}\n')
    
def começar_jogo(materia: str):
    
    #* Carregar as perguntas da materia escolhida
    lista_perguntas = carregar_perguntas(materia)
    
    #* Verificar se a lista de perguntas esta vazia
    if not lista_perguntas:
        print('\nNão foi possível iniciar o quiz. Voltando ao menu principal.')
        return
    
    #* Variaveis de pontuacao
    respostas_erradas = 0
    pontuacao = 0
    
    print(f'\nO jogo de {materia.capitalize()} já vai começar, se prepare!')
    mostrar_pontuação(pontuacao)
    time.sleep(2)

    #* Iterar sobre a lista para exibir cada pergunta
    for indice, questao in enumerate(lista_perguntas, start=1):
        print(f'{indice}. {questao["enunciado"]}') # exibicao de cada pergunta
        
        #* Iterar sobre o dicionario presente na lista para exibir cada alternativa e o texto das alternativas
        for letra, texto in questao['alternativas'].items(): # exibicao das alternativas e dos textos das alternativas 
            print(f'{letra}) {texto}')
        
        #* Solicitar resposta do usuario
        resposta_usuario = input('Digite sua resposta: ').upper()
        
        #* Verificar resposta do usuario
        if resposta_usuario == questao['resposta']:
            print('Resposta correta!')
            pontuacao += 1
            time.sleep(2)
        else:
            print(f'Resposta incorreta!')
            resposta_correta = questao['resposta']
            texto_resposta_correta = questao['alternativas'][resposta_correta]
            print(f'A resposta correta era: {resposta_correta}: {texto_resposta_correta}')
            respostas_erradas += 1
            time.sleep(4)
            
        #* Mostrar pontuacao atual
        mostrar_pontuação(pontuacao)
            
    print('\n====== Detalhes do Quiz ======')
    print(f'Pontuação Final: {pontuacao}')
    print(f'Respostas Erradas: {respostas_erradas}')
    time.sleep(3)