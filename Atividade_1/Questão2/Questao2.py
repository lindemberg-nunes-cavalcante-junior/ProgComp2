import sys
from Funcoes import Questao2_mine_lib

BytesEntrada = (('Esse é fácil',8))

nonceFind,tempoFind = Questao2_mine_lib.FindNonce(BytesEntrada[0],BytesEntrada[1])


'''
,('Esse é fácil',10),('Esse é fácil',15)
                ('Texto maior muda o tempo?',8),('Texto maior muda o tempo?',10),('Texto maior muda o tempo?',15)
                ('É possível calcular esse?',18),('É possível calcular esse?',19),('É possível calcular esse?',20)
'''