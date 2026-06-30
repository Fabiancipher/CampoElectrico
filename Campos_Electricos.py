import numpy as np
import matplotlib.pyplot as plt
a = 9 #Distancia entre cargas(Metros). Se asume que el cuadrado está centrado en el origen, facilitando las coordenadas

q = 8  #Magnitud en C
Q = [(-a,a,q),(-a,-a,-q),(a,-a,q),(a,a,-q)] #Cargas (x,y,q)

x1, y1 = -10, -10  # Limites
x2, y2 = 10, 10   
lres = 10        
m, n = lres * (y2-y1), lres * (x2-x1) #Espacio muestral
x, y = np.linspace(x1,x2,n), np.linspace(y1,y2,m) #Para graficar
x, y = np.meshgrid(x,y)
Ex = np.zeros((m,n)) #Descomposiciones en X
Ey = np.zeros((m,n)) #Descomposiciones en Y

k = 9 * 10**9 #Constante de Coulomb
for j in range(m): #Para cada y...
    for i in range(n): #Para cada x...
        xp, yp = x[j][i], y[j][i] # Para cada punto muestral...
        for q in Q: #Por cada carga...
            deltaX = xp - q[0] #Diferencia en x del punto hacia la carga
            deltaY = yp - q[1] #Diferencia en y

            distance = (deltaX**2 + deltaY**2) #Distancia al cuadrado

            E = (k*q[2])/(distance) #Formula de la energía    
            Ex[j][i] += E*(deltaX/np.sqrt(distance)) #E*Cos(theta) = adyacente/hipotenusa = deltax/distancia
            Ey[j][i] += E*(deltaY/np.sqrt(distance)) #E*Sin(theta) = opuesto/hipotenusa = deltay/distancia
"""
Para dibujar
"""
fig, ax = plt.subplots() 
ax.set_aspect('equal')
colores = {True: "#ff4444", False: "#4488ff"}
ax.scatter([q[0] for q in Q], [q[1] for q in Q], c = [colores[q[2]>0] for q in Q], s = [abs(q[2])*50 for q in Q], zorder = 1) #Dibuja cada carga, su tamaño escala según la magnitud. El color depende de la magnitud
i = 1
for q in Q: 
    ax.text(q[0]-0.2, q[1]-0.1, f'q{i}', color = 'black', zorder = 2) 
    i+=1 #Etiquetas
ax.streamplot(x,y,Ex,Ey, linewidth = 1, density = 1.5, zorder = 0) #Dibuja las flechas

plt.title('Simulación Campo Eléctrico')
plt.show()