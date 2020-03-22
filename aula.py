import matplotlib.pyplot as plt

#Criacao de graficos de linha

#Crie listas
x = [1, 2, 5]
y = [2, 3, 7]

x1 = [3, 6, 18]
y1 = [0, 20, 1]
plt.title("Meu primeiro Grafico em Python!")

plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.bar(x, y, label = "Grupo 1", color = "red")
plt.bar(x1,y1, label = "Grupo 2", color = "yellow")
plt.legend()
#plt.show()
# Dpi significa "Dots per inch"
plt.savefig("teste.png", dpi = 300)