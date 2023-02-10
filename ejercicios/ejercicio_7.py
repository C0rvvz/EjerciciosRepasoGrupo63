if __name__ == "__main__":

    lista = []

    def maximo_y_minimo(numeros):

        maximo = numeros[0]
        minimo = numeros[0]

        for numero in numeros:

            if numero > maximo:
                maximo=numero
                print(f"numero maximo {maximo}")

            if numero < minimo:
                minimo = numero
                print(f"numero minimo {minimo}")


        return maximo,minimo


    cantidad_de_numeros = int(input("Cual sera la cantidad de numeros?: "))


    for i in range(cantidad_de_numeros):


        lista.append(int(input("Ingrese el numero para la lista: ")))

    maximo_y_minimo(lista)


