def Binary_to_int(binary):
    binary = input("enter a binary number to be converted to an integer")
    int = 0
    power = 0
    while binary > 0:
        int += 2** power * (binary % 10)
        binary //= 10
        power = power + 1

    print(str(binary_to_int(101011)))