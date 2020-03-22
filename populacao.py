# Importamos a math plot
import matplotlib.pyplot as plt

# Padrao de documento csv, que separa os dados por ";"
dados = open("popBrasil.csv").readlines()

# Aqui criamos duas listas para armazenar os dados
eixoX = []
eixoY = []

'''
A funcao range cria uma lista que vai de zero ate o 
tamanho final dos dados
'''

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        # Append serve para adicionar
        eixoX.append(int(linha[0]))
        eixoY.append(int(linha[1]))

plt.title("Crescimento da Populacao Brasileira 1980 - 2016")
plt.xlabel("Ano")
plt.ylabel("Populacao x 10^8")
plt.bar(eixoX, eixoY, color = "#e4e4e4")
plt.plot(eixoX, eixoY, color='k', linestyle = "--")
#plt.show()
plt.savefig("PopBrasil", dpi = 300)