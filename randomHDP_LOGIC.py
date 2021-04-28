import pandas as pd
import numpy
import random
import testTelegram as tele
from telegram.ext import *


filedata = pd.read_excel(r"D:\DOCUments D\GoeTemp\hdp meu\hdp.xlsx")
cartasBlancas = filedata["CartasBlancas"].values.tolist()
cartasNegrasExcel = filedata["CartasNegras"].values.tolist()
count = 0
participantes = {"rapo":"@matirapo","colton":"","fishman":"","mariloko":"","criv":"","peer":""}
cartasPorParticipante = 7

cartasNegras = [x for x in cartasNegrasExcel if str(x) != 'nan']
dosBlancas = False

#print(cartas)

# while count < len(cartas):
#     print(str(count + 1) + " " + cartas[count])
#     count += 1

print("\n")

for i in participantes:
    print(i + ":")
    for j in range(7):
        w = random.randint(0,len(cartasBlancas)-1)
        print(cartasBlancas[w])
        cartasBlancas.pop(w)
        
    print("------------------------")
n = random.randint(0,len(cartasNegras)-1)
print("Carta negra: " + cartasNegras[n])
if cartasNegras[n][-1] == "2":
    dosBlancas = True

while len(cartasBlancas)>len(participantes):
    #print(len(cartasBlancas))
    input("Presione enter para pasar de ronda:")
    print("\n\n")
    if dosBlancas == True:
        for i in participantes:
            print(i + ":")
            for j in range(2):
                z = random.randint(0,len(cartasBlancas)-1)
                print(cartasBlancas[z])
                cartasBlancas.pop(z)
            print("------------------------")
    else:
        for i in participantes:
            print(i + ":")
            w = random.randint(0,len(cartasBlancas)-1)
            print(cartasBlancas[w])
            cartasBlancas.pop(w)
            print("------------------------")
    
    n = random.randint(0,len(cartasNegras)-1)
    print("Carta negra: " + cartasNegras[n])
    if cartasNegras[n][-1] == "2":
        dosBlancas = True
    else:
        dosBlancas = False
