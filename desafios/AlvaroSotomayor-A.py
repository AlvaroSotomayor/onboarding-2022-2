#Clases
class Numero:
    def __init__(self, unidades):
        result = 0
        if unidades < 0:
            for i in range(unidades):
                result -= 1
        elif unidades >= 0:
            for i in range(unidades):
                result += 1
        self.valor = result


#Codigo pricipal
result = 0
continuar = True

while continuar:
    op = int(input('Ingrese la operacion deseada, multiplicacion -> 0   suma -> 1   salir -> 2:'))

    if op == 0: #Multiplicacion
        n1 = int(input('Ingrese el primero numero:'))
        n2 = int(input('Ingrese el segundo numero:'))

        N1 = Numero(n1)
        N2 = Numero(n2)

        if N1.valor != N2.valor:
            if N1.valor > N2.valor:
                for i in range(N1.valor):
                    result += N2.valor
            elif n1 < n2:
                for i in range(N2.valor):
                    result += N1.valor
        elif N1.valor == N2.valor:
            for i in range(N1.valor):
                result += N1.valor
        print('El resultado es:',result,'\n')

    elif op == 1: #Suma
        n1 = int(input('Ingrese el primero numero:'))
        n2 = int(input('Ingrese el segundo numero:'))

        N1 = Numero(n1)
        N2 = Numero(n2)

        if N1.valor != N2.valor:
            if N1.valor > N2.valor:
                for i in range(N1.valor):
                    N2.valor += 1
                result = N2.valor
            elif N1.valor < N2.valor:
                for i in range(N2.valor):
                    N1.valor += 1
                result = N1.valor
        elif N1.valor == N2.valor:
            for i in range(N1.valor):
                result += 2
        print('El resultado es:',result,'\n')

    else: #Salir (2)
        continuar = False
        print('Gracias por usar nuestros servicios!!')
    
    result = 0
    
