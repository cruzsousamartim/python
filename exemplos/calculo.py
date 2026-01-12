min= float(input("quantos minutos?"))
while not (min >= 1 and min <= 60):
    print("Valor inválido! Digite um número entre 1 e 60.")
    min = float(input("Quantos minutos? "))

seg=float(input("quantos segundos?"))
while not (seg >= 1 and seg <= 60):
     print("Valor inválido! Digite um número entre 1 e 60.")
     seg= float(input("Quantos segundos? "))

hor=float(input("Quantas horas?"))
while not (hor >= 1 and hor <= 24):
     print("Valor inválido! Digite um número entre 1 e 24.")
     hor=float(input("Quantas horas?"))

med=seg+(min*60)+(hor*3600)
print ("valor em segundos",med)


