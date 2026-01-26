import matplotlib.pyplot as plt
countries = ["Portugal", "Brasil", "Alemanha", "França", "Bélgica"]
scores = [10.0, 5.0, 7.0, 4.0, 9.0]


plt.plot(countries, scores, "-o", color="blue", linewidth=3)


plt.title("Campeonato do Mundo de Futebol")
plt.ylabel("Pontuações")
plt.xlabel("Nações")


plt.grid()
plt.show()