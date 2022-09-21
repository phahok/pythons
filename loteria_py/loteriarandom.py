# -*- coding: iso-8859-1 -*-
'''
Created on 20/09/2022

@authores: 
José Renato Ferreira ( DevOps Architect)
Alexandre Alvarez ( Mathematic )

Apoiadores
Caio Cunha e Hyull Brynner
'''

import random
import pickle

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

contador = 0

while (contador < 15):
    random.shuffle(lista)
    par_es = list(filter(lambda x: (x % 2 == 0), lista))
    impar_es = list(filter(lambda x: (x%2 != 0) , lista)) 
    #print("Pares: ", par_es[0:8]) 
    par = sorted(par_es[0:7])
    #print("Impar: ", impar_es[0:7])
    impar = sorted(impar_es[0:8])
    #print("Jogo Completo :" , sorted(lista[0:15])) #gerar 01 jogo aleatorio 15 nros
    file = open('arq_jogos.txt', 'a')
    unir = sorted(par+impar)
    file.write('%s\n' % unir)
    
    print ("Jogo 6par9imp: ", sorted(par + impar))
    contador = contador + 1
else:
    file.write('\n')
    file.close()
    print(" Jogos Gerados com sucesso!")

