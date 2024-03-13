import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
#Definindo cores personalizadas
# ax.scatter(x_values, y_values, color= 'blue', s=10) #pode ser usado RGB na cor
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10) #Colormap


#Define o título do gráfico e os eixos do rótulo
ax.set_title("Square Numbers", fontsize=14)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

#Define o tamanho dos rótulos de marcação de escala
ax.tick_params(labelsize=14)

#Define o intervalo para cada eixo
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain') #permite sobrescrever o estilo default de marcação de escala dos rótulos para qualquer gráfico

#Salvando automaticamente seus gráficos
plt.savefig('squares_plot.png', bbox_inches='tight')
# plt.show()