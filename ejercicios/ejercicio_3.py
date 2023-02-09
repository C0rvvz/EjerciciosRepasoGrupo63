if __name__ == "__main__":


    import random


    lista=[]


    cantidad_de_numeros=int(input("Cual sera la cantidad de numeros?: "))



    for i in range(cantidad_de_numeros):



        lista.append(random.randrange(100))



    print(lista)