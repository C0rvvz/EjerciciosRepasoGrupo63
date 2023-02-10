if __name__ == "__main__":

    import random
    def media_aritmetica_de_una_lista():

        lista = []

        numero_del_rango = int(input("el rango de la lista es: "))

        for i in range(numero_del_rango):
            lista.append(random.randrange(100))
        print(lista)

        suma_de_numeros = 0
        for numero in lista:
            suma_de_numeros += numero
        print(suma_de_numeros)

        media=suma_de_numeros/numero_del_rango
        print(f"la media de la lista es: {media}")

    media_aritmetica()