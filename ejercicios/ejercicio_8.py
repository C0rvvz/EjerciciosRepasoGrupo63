if __name__ == "__main__":


    lista=[]


    cantidad_de_numeros = int(input("Cual sera la cantidad de numeros?: "))


    for i in range(cantidad_de_numeros):


        lista.append(int(input("Ingrese el numero para la lista: ")))


    def invertir_lista(numeros):
        return numeros[::-1]

    lista_invertida=invertir_lista(lista)

    print(f"original{lista}")
    print(f"invertida{lista_invertida}")