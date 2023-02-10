if __name__ == "__main__":


    lista=[[12,7],
       [4,5],
       [3,8]]

    matriz=[[0,0,0],
            [0,0,0]]

    for i in range(len(lista)):
        for j in range(len(lista[0])):
            matriz[j][i]=lista[i][j]
    for r in matriz:
        print(r)