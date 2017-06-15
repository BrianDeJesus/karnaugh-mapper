#input menu
import exceptions

def get_input():
    minterms = []
    while True:
        try:
            var_amount = int(input("Please enter 4 to use a 4 variable kmap, 3 to use a 3 variable kmap, or 2 to use a 2 variable kmap: "))
            if var_amount < 2 or var_amount > 4:
                raise exceptions.InvalidInputError("{} is out of range. " .format(var_amount))
            break
        except ValueError:
            print("Invalid input. ")

    if var_amount == 4:
        minterms = get_mins()
        if len(minterms) > 16:
            raise exceptions.InputLengthError("Too many minterms. ")
        for num in minterms:
            if num > 15:
                raise exceptions.InvalidInputError("Minterm: {} is out of range. " .format(num))
    elif var_amount == 3:
        minterms = get_mins()
        if len(minterms) > 8:
            raise exceptions.InputLengthError("Too many minterms. ")
        for num in minterms:
            if num > 7:
                raise exceptions.InvalidInputError("Minterm: {} is out of range. " .format(num))
    elif var_amount == 2:
        minterms = get_mins()
        if len(minterms) > 4:
            raise exceptions.InputLengthError("Too many minterms. ")
        for num in minterms:
            if num > 3:
                raise exceptions.InvalidInputError("Minterm: {} is out of range. " .format(num))

    return list(set(minterms)), var_amount


def get_mins():
    terms = []
    print("Please enter the minterm values separated by a space: ")
    terms = list(map(int, input().split()))
    return terms
