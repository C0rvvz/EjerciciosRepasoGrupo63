if __name__ == "__main__":


    list = []


    counter = 0


    amount_of_numbers = int (input ("Enter the range of the numbers: ") )


    for i in range (amount_of_numbers):


        counter += 1


        list.append (int (input (f"Enter the number {counter} for the list: ") ) )


    def invert_list (numbers):


        return numbers[::-1]


    investment_made = invert_list (list)


    print (f"Original list: {list} ")


    print (f"Inverted list: {investment_made} ")