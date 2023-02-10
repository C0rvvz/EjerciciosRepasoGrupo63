if __name__ == "__main__":


    lista=[]

    suma_de_numeros=0

    cantidad_de_numeros=int(input("Cual sera la cantidad de numeros?: "))



    for i in range(cantidad_de_numeros):



        lista.append(int(input("Ingrese el numero para la lista: ")))


    for numero in lista:


        suma_de_numeros += numero


    print(f"La suma de numeros de la lista es: {suma_de_numeros}")