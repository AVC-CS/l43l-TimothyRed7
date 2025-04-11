def main():
    total = 0

    numbers = [0] * 5
    for i in range(len(numbers)):
        numbers[i] = int(input('Enter a value: '))
    
    """
    ########################################
    Code Your Program here
    ########################################
    """
    v=0
    print(numbers)
    for v in range(len(numbers)):
        total=total+number[v]

    # total = sum(numbers)
    print(total)

    ########################################
    # Do not delete the return statement
    ########################################
    return total, numbers


if __name__ == '__main__':
    main()
