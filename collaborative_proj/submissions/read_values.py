def read_values():
    # Prompt the user for input and split the string by spaces
    raw_input = input("[10 45 32 88 102 55,30,100,98,67,89,90,23,45,56,64]: ")

    # Convert each string value into a float and return the list
    return [float(val) for val in raw_input.split()]


def main():
    # read values
    x = read_values()  # x is a list of numbers, either integers or floats
    n = len(x)        # integer; number of values

    print("Your list:", x)
    print("Number of values:", n)

main()
