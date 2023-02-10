if __name__ == "__main__":


    list = [[12,7],
       [4,5],
       [3,8]]

    matriz = [[0,0,0],
            [0,0,0]]

    for i in range(len(list)):


        for j in range(len(list[0])):


            matriz[j][i]=list[i][j]


    for r in matriz:


        print(r)