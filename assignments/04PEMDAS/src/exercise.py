def main():
    from math import sqrt
    a = 4
    b = 5
    oper1 = (2*(3/4)) + (4*(2/3)) - (3*(1/5)) + (5*(1/2))
    print(float(round(oper1,4)))
    oper2 = (2*sqrt(35**2)) + (4*sqrt(36**3)) - (6*sqrt(49**2))
    print(float(oper2))
    oper3 = ((a**3) + (2*b**2)) / (4*a)
    print(float(oper3))
    oper4 = ((2*(a+b)**2) + (4*(a-b)**2)) / (a*(b**2))
    print(float(oper4))
    oper5 = (sqrt((a+b)**2 + 2**(a+b)))/(2*a + 2*b)**2
    print(float(round(oper5,4)))

#no se como hacer que la oper4 me de 1.66 :/
if __name__ == '__main__':
    main()
