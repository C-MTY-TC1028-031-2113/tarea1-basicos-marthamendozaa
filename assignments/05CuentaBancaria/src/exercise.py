def main():
    #escribe tu código abajo de esta línea
    saldo = float(input("Dame el saldo del mes anterior: "))
    ingreso = float(input("Dame los ingresos: "))
    egreso = float(input("Dame los egresos: "))
    cheque = int(input("Dame el número de cheques: "))
    saldosint = (saldo + ingreso - egreso - cheque*13)
    saldofinal = saldosint - (saldosint * 0.075)
    print("El saldo final de la cuenta es: " + str(saldofinal))


if __name__ == '__main__':
    main()