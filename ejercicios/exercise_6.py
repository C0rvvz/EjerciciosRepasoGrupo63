if __name__ == "__main__":


    list = []


    counter=0


    sum_of_numbers = 0


    amount_of_numbers = int (input ("Enter the range of the numbers: ") )



    for i in range (amount_of_numbers):


        counter += 1


        list.append (int (input (f"Enter the number {counter} for the list: ") ) )


    for number in list:


        sum_of_numbers += number


    print (f"The sum of the numbers in the list is: {sum_of_numbers} ")