entrada = open("bacteria.fasta").read()
# Criamos o arquivo com o parametro "w" que indica write
saida = open("bacteria.html","w")

# Vamos criar um dicionario com as combinacoes dos nucleotidios
cont = {}

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont[i+j] = 0

'''
 Substituimos a quebra de linha por nada, pois as quebras
 de linha fariam parte da busca no dicionario
'''
entrada = entrada.replace("\n", '')

# Range cria listas
for k in range((len(entrada)-1)):
    cont[entrada[k]+entrada[k+1]] += 1

print(cont)

