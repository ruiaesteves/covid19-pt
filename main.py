# Portugal Covid-19 situation
# @ruiesteves

# Imports
from covidpt import *
import matplotlib.pyplot as plt

# Script
print("Interpretador de dados Covid-19 Portugal","\n")
print("Comandos:")
print("Actualizar dados: ACTUALIZAR")
print("Mostrar graficos: MOSTRAR")
print("Sair: SAIR","\n")

command = input("O que quer fazer? ")

while command != "SAIR":
    if command == "ACTUALIZAR":
        days, tests_by_day, new_plus, new_negative, plus_percentage, size = read()
        print("Ultimos dados sao do dia",(days[len(days)-1]))
        new_day = input("Qual o novo dia? ")
        plus = int(input("Quantos novos casos confirmados? "))
        total = int(input("Quantos testes efetuados? "))
        days.append(new_day)
        new_plus.append(plus)
        tests_by_day.append(total)
        cumulative_plus, cumulative_total = cumulative()

        file = open("data","w")
        for day in days:
            file.write("%s " % day)
        file.write("1\n")

        for test in tests_by_day:
            file.write("%s " % test)
        file.write("1\n")

        for plus in new_plus:
            file.write("%s " % plus)
        file.close()
        print("\n")
    elif command == "MOSTRAR":
        days, tests_by_day, new_plus, new_negative, plus_percentage, size = read()
        cumulative_plus, cumulative_total = cumulative()
        max_plus = max_list(new_plus)
        max_perct = max_list(plus_percentage)
        max_cases = max_list(cumulative_plus)
        max_test = max_list(tests_by_day)

        theory = [(169*(1.4)**i) for i in range(size)]
        plt.figure()
        plt.subplot(411)
        plt.plot(days,new_plus,color="r")
        plt.grid()
        plt.ylabel("Num de Casos")
        plt.title("Novos Casos p/Dia")

        plt.subplot(412)
        plt.plot(days,plus_percentage,color="b")
        plt.grid()
        plt.ylabel("% Positivos")
        plt.title("% de Testes Positivos p/Dia")

        plt.subplot(413)
        plt.plot(days,cumulative_plus,color="g",label="Real")
        plt.plot(days,theory,linestyle="dashed",color="r",label="Teorico")
        plt.grid()
        plt.legend()
        plt.ylabel("Casos Confirmados")
        plt.title("Evolucao do Numero de Casos")

        plt.subplot(414)
        plt.plot(days,tests_by_day,color="k")
        plt.grid()
        plt.ylabel("Num de Testes")
        plt.title("Evolucao do Numero de Testes")

        #plt.subplots_adjust(hspace=2)
        plt.tight_layout()
        plt.show()
        print("\n")
    else:
        print("Comando desconhecido.","\n")

    command = input("Comando: ")
    print("\n")
