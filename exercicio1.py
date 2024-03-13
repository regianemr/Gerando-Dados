import matplotlib.pyplot as plt
plt.style.use('seaborn')


x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
#Definindo cores personalizadas
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

#Define o título do gráfico e os eixos do rótulo
ax.set_title("Square Numbers", fontsize=20)
ax.set_xlabel("Value", fontsize=20)
ax.set_ylabel("Square of value", fontsize=20)

#Define o intervalo para cada eixo
ax.axis([0, 5000, 0, 100_000_000_000])
ax.ticklabel_format(style='plain') #permite sobrescrever o estilo default de marcação de escala dos rótulos para qualquer gráfico

#Salvando automaticamente seus gráficos
plt.savefig('squares_plot_ex1.png', bbox_inches='tight')
# plt.show()