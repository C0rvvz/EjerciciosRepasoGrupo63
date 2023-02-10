if __name__ == "__main__":

    list = []


    counter = 0


    amount_of_numbers = int (input ("Enter the range of the numbers: ") )


    for i in range (amount_of_numbers):


        counter += 1


        list.append (int (input (f"Enter the number {counter} for the list: ") ) )



    def maximum_and_minimum (numbers):


        maximum = numbers [0]


        minimum = numbers [0]


        for number in numbers:


            if number > maximum:


                maximum = number


                print(f"The maximum number is: {maximum} ")


            if number < minimum:


                minimum = number


                print(f"The minimum number is: {minimum} ")


        return maximum , minimum


    maximum_and_minimum (list)


