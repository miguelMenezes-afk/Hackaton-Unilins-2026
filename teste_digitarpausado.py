import time
import sys
import os
from colorama import Fore, Style, init

def digitar_pausado(texto, atraso=0.05, cor=""):
    sys.stdout.write(cor)
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(atraso)
    sys.stdout.write(Style.RESET_ALL)
    sys.stdout.flush()
    print()

digitar_pausado("Conectando...",cor=Fore GREEN)