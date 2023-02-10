if __name__ == "__main__":


    import random


    list = []


    amount_of_numbers = int (input ("Enter the range of the numbers: ") )



    for i in range (amount_of_numbers):



        list.append (random.randrange(100) )



    print (list)