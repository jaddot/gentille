#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 23:33:58 2023

@author: paul
"""

import json
import random

with open('demonyms.json') as mon_fichier:
    data = json.load(mon_fichier)

#print(len(data['regions']))
#18 régions
#print(len(data['departements']))
#106 départements
#print(len(data['communes']))
#30 422 communes

villes = list(data['communes'])
départements = list(data['departements'])
régions = list(data['regions'])
# print(data['communes']["saint-remy-du-nord"])

def jeu():
    communes, departements, regions = 0,0,0
    print("voulez-vous vouer sur des communes, des départements ou des régions?")
    réponse = input()
    if réponse == "communes":
        selec = selection_communes()
        rep = input("Quel est le gentillé de la commune de " + str(selec) + " ?")
        verification(rep, selec)
        
        
        
def selection_communes():
    rand = random.randint(0,len(villes))
    return villes[rand]
    
def verification(repa, seleca):
    a = 1
    for i in range(len(data['communes'][seleca])):
        if repa == data['communes'][seleca][i]:
            print("bravo")
            a=0
    if a == 1:
        print("raté, la bonne réponse était : " + affichage(data['communes'][seleca]))
            


# L = data['communes']
# L_ = villes
# H = []
# for i in range(len(L_)):
#     H.append(len(L[L_[i]]))
# print(H)
# print(max(H))

# for i in range(len(H)):
#     if H[i] == 23:
#         print(i)

# print(villes[2263])
# print(data['communes']["beaulieu"])

def affichage(L):
    return ' ou '.join(L)