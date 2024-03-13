import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    #Cria um random walk
    rw = RandomWalk(50_000) #Adicionando pontos ao gráfico
    rw.fill_walk()

    #Plota os pontos no passeio
    plt.style.use('classic')
    fig, ax = plt.subplots()
    #Colorindo os pontos
    point_numbers = range(rw.num_points) #gerando uma lista igual o numero de pontos passeio
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds, edgecolors='none', s=1)#edgecolors=none descarta contorno preto em torno de cada ponto
    ax.set_aspect('equal')

    #Destaca o primeiro e o último ponto
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c= 'red', edgecolors='none', s=100)
    
    #Remove os eixos
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    #GERANDO MÚLTIPLOS PASSEIOS ALEATÓRIOS

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
