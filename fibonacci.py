def check_for_fibonacci():
    checked_num = input("\n\nEnter the integer you want to check is in the Fibonacci sequence:\n\n>>>> ")

    while checked_num.isdigit() == False:
        print("\nPlease enter a valid integer.")

        checked_num = input("\n\nEnter the integer you want to check is in the Fibonacci sequence:\n\n>>>> ")

    x = 0
    y = 1
    z = x + y
    
    while True:
        if int(checked_num) in [x, y, z]:
            print("\n\n" + checked_num + " is in the Fibonacci sequence.")
            break

        elif int(checked_num) < z:
            print("\n\n" + checked_num + " is not in the Fibonacci sequence.")
            break
        
        x = y
        y = z
        z = x + y


def n_in_sequence():
    n = input("\n\nFind the n'th number in the Fibonacci sequence\n\n>>>> n = ")
    
    while n.isdigit() == False:
        print("\nPlease enter a valid integer.")

        n = input("\n\nFind the n'th number in the Fibonacci sequence\n\n>>>> n = ")
    
    x = 0
    y = 1
    z = x + y

    if n == '1':
        print("\n\nThe number in the sequence is " + str(x))

    elif n == '2':
        print("\n\nThe number in the sequence is " + str(y))

    elif n == '3':
        print("\n\nThe number in the sequence is " + str(z))

    else:
        for x in range(2, int(n)):
            x = y
            y = z
            z = x + y

        print("\n\nThe number in the sequence is " + str(z))


def fibonacci():
    func = input("\n\nWhat would you like to do?\n\n[1. Check If Num Is In Fibonacci Sequence, 2. Print N'th Num In Fibonacci Sequence, 3. Exit Program]\n>>>> ")

    while func not in ['1', '2', '3']:
        print("\nThat is not a valid option. Please enter the number of the option you want.")

        func = input("\n\nWhat would you like to do?\n\n[1. Check If Num Is In Fibonacci Sequence, 2. Print n'th Num In Fibonacci Sequence]\n>>>> ")

    if func == '1':
        check_for_fibonacci()

        fibonacci()

    elif func == '2':
        n_in_sequence()

        fibonacci()

    elif func == '3':
        print("\n\nUnderstandable, have a great day.")


def main():
    fibonacci()


if __name__ == "__main__":
    main()