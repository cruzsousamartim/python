import matplotlib.pyplot as plt
Disciplinas=["Português","Matematica","Tecnologias","Inglês"]
Resultados=[14.4, 17.3, 18.1, 13.3]
plt.plot(Disciplinas, Resultados, "-o", color="blue", linewidth=1)
plt.title("Resultados Escolares")
plt.ylabel("Resultados")
plt.xlabel("Disciplinas")
plt.grid()
plt.show()
