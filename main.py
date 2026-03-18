import time
import sys
import os
from colorama import Fore, Style, init

# Inicializa o colorama para cores no terminal
init(autoreset=True)

def digitar_pausado(texto, atraso=0.05):
    """Simula o efeito de uma máquina de escrever no terminal."""
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(atraso)
    print()

def limpar_tela():
    """Limpa o terminal dependendo do Sistema Operacional."""
    os.system('cls' if os.name == 'nt' else 'clear')

def fase_1():
    limpar_tela()
    
    # Cabeçalho de imersão
    print(Fore.GREEN + Style.BRIGHT + "="*60)
    print(Fore.GREEN + Style.BRIGHT + "SISTEMA OPERACIONAL VANCE - VERSÃO 1.0.4 - 1987")
    print(Fore.GREEN + Style.BRIGHT + "="*60)
    print("\n")

    # Storytelling
    digitar_pausado(Fore.GREEN + "Conectando ao terminal de fósforo verde...")
    time.sleep(1)
    digitar_pausado(Fore.GREEN + "Acesso físico detectado no Laboratório Particular.")
    time.sleep(1)
    digitar_pausado(Fore.WHITE + "\nApós meses de investigação sobre o paradeiro do Dr. Alistair Vance, você finalmente consegue acesso físico ao seu laboratório particular. No centro da sala, um terminal de fósforo verde antigo permanece ligado. A tela está bloqueada por um protocolo de segurança de baixo nível, emitindo um brilho hipnótico. Não há campos para digitar nomes, apenas um prompt de comando aguardando uma sequência de identificação.:")
    digitar_pausado(Fore.YELLOW + "A base de tudo é a memória. Identifique-se para iniciar o protocolo.")
    
    print("\n" + Fore.GREEN + "-"*60)
    print(Fore.CYAN + "SEQUÊNCIA DE BYTES DETECTADA NO BUFFER DE ENTRADA:")
    print(Fore.WHITE + Style.BRIGHT + "41  52  49  41  44  4e  45")
    print(Fore.GREEN + "-"*60 + "\n")

    # Lógica de validação
    tentativas = 0
    while True:
        # O prompt de comando
        print(Fore.GREEN + "VANCE_OS > ", end="")
        entrada = input().strip().upper()

        if entrada == "ARIADNE":
            print("\n")
            digitar_pausado(Fore.GREEN + ">>> PROCESSANDO IDENTIFICAÇÃO...", atraso=0.1)
            time.sleep(1)
            print(Fore.GREEN + "[ OK ] IDENTIDADE RECONHECIDA.")
            time.sleep(0.5)
            print(Fore.GREEN + "[ OK ] SINCRONIZANDO HERANÇA DE DADOS.")
            time.sleep(0.5)
            
            print("\n" + Fore.CYAN + "*"*60)
            digitar_pausado(Fore.CYAN + "BEM-VINDA DE VOLTA, ARIADNE.")
            digitar_pausado(Fore.CYAN + "O acesso ao Nível 2 foi liberado no servidor local.")
            print(Fore.CYAN + "*"*60)
            
            print("\n" + Fore.WHITE + "Anote este nome. Você precisará dele para o filtro de integridade.")
            print(Fore.YELLOW + "Pressione ENTER para encerrar a conexão e avançar para a Fase 2...")
            input()
            break
        else:
            tentativas += 1
            digitar_pausado(Fore.GREEN + ">>> PROCESSANDO IDENTIFICAÇÃO...", atraso=0.1)
            time.sleep(1)
            print(Fore.RED + ">>> ACESSO NEGADO: IDENTIFICAÇÃO INVÁLIDA.")
            if tentativas >= 3:
                print(Fore.RED + Style.DIM + "DICA: O sistema fala em hexadecimal. A Tabela ASCII é a sua chave.")
            print("\n")

if __name__ == "__main__":
    try:
        fase_1()
    except KeyboardInterrupt:
        print(Fore.RED + "\n\nConexão abortada pelo usuário.")