from functions import *


days = 7



if __name__ == "__main__":

    try :
        days = int(eval(input("Analizar x días atrás : ")))
    except :
        pass
    ticks = buscarTicks()
    ticksNumber = len(ticks)
    print("NUMERO DE TICKS: " + str(ticksNumber))
    for tick in ticks:
        analizarMoneda(tick,days)
    showResults()
