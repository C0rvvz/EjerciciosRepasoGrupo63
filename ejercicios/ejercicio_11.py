if __name__ == "__main__":


    lista=[]
    contador=0
    numeros=100
    for i in range(numeros):
        contador += 1
        if contador % 2 == 0:
            lista.append(contador)
    print(lista)