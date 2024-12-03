from Questao3_lib import *
import random

Palavras = leituraArquivo()
Sorteio = random.choice(Palavras).upper()
tentativas = 1
print(f'A palavra tem {len(Sorteio)} letras e você possui 6 tentativas para advinhar')

#Jogo
while True:
    #A tentativa do usuario
    while True:
        tentativa = input('Sua tentativa: ').upper()
        if len(tentativa) < len(Sorteio) or len(tentativa) > len(Sorteio): 
            print('Coloque a palavra da maneira certa...')
        for i in tentativa:
             if i.isdigit(): print('Apenas letras, nenhum número será aceito...')
        else: break
    
# --------------------------------------------------------------
# Verificação das letras.
    for i,x in zip(Sorteio,tentativa):
        if i == x:
            print(bcolor.verde + f'{i}' +'\033[0m',end='')
        elif i != x and Sorteio[Sorteio.find(x)] == x:
            print(bcolor.amarelo+f'{x}'+'\033[0m',end='')
        else:
            print(bcolor.cinza+f'{x}'+'\033[0m',end='')
    print()
# --------------------------------------------------------------
# Contador
    if tentativas == 6:
        print(f"A palavra era {Sorteio}, você perdeu.")
        break
    elif tentativa == Sorteio:
        print(f'Parabens, você acertou a palavra em {tentativas} tentativas!!')
        break
    tentativas += 1