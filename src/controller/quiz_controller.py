
#* Importacoes Gerais
import os

#* Importacao das Funcoes
from src.model.estrutura_do_jogo import começar_jogo

#* Funcao para limpar o console
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_exibir_materias():
    """
    Função dedicada a mostrar o menu de matérias e capturar a escolha do usuário.
    Retorna o nome da matéria em minúsculo ou None se o usuário decidir voltar.
    """
    print('\nEscolha uma materia para o quiz')
    print('1. Filosofia')
    print('2. Historia')
    print('3. Voltar a menu principal')
    
    while True:
        try:
            escolha = int(input('Digite a sua escolha: '))
            if escolha == 1:
                return 'filosofia'
            elif escolha == 2:
                return 'historia'
            elif escolha == 3:
                return None # retornar ao menu principal
            else:
                raise ValueError
        except ValueError:
            print('Erro. Opção inválida. Por favor, digite um dos números do menu.')
            
def main():
    #* Apresentacao do Quiz
    limpar_tela()
    print('===== QUIZ DO BRUNO =====')
    print('Seja bem vindo(a/e) ao quiz do Bruno. Selecione uma opção abaixo para continuar.')

    #* Coletar Resposta do Usuário
    while True:
        print('\nEscolha uma opcao abaixo para continuar.')
        print('1. Iniciar quiz')
        print('2. Sair')    
          
        try:
            #* Pedir a escolha do usuario
            escolha_usuario = int(input('Digite a sua escolha: '))
            
            if escolha_usuario == 1: # usuario deseja iniciar o jogo 
                
                #* mostrar menu de materias para o usuario escolher
                materia_escolhida = menu_exibir_materias()
                
                if materia_escolhida: # se None o menu sera mostrado novamente
                    limpar_tela()
                    começar_jogo(materia_escolhida) # inicia o jogo com o tema da materia escolhida
                    limpar_tela()
                    print("Quiz finalizado.")
                continue
            elif escolha_usuario == 2:
                print('Obrigado por jogar! Até a próxima.')
                break
            
            else:
                print('Erro: Opção inválida. Por favor, digite 1 ou 2.')
            
        except ValueError:
            print('Erro: Entrada inválida. Por favor, digite um número.')

main()