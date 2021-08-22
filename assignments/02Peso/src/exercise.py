def main():
    #escribe tu código abajo de esta línea
    pi = float(input("Dame el peso inicial: "))
    pf = float(input("Dame el peso final: "))
    mes = int(input("Dame la cantidad de meses: "))
    bajar = float((pi-pf)/mes)
    print("Lo que debes bajar por mes es: " + str(bajar))




if __name__ == '__main__':
    main()
