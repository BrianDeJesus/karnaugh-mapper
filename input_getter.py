#input menu
import argparse
import exceptions


def get_input():
    parser = argparse.ArgumentParser()

    parser.add_argument('--variable_count', '-n' ,type=int, choices=range(2,5), required=True)
    parser.add_argument('--minterms', '-m', nargs='+', required=True, type=int)
    args = parser.parse_args()

    if args.variable_count == 2:
        check_minterms(args, 3)
        check_length(args, 4)
    elif args.variable_count == 3:
        check_minterms(args, 7)
        check_length(args, 8)
    elif args.variable_count == 4:
        check_minterms(args, 15)
        check_length(args, 16)
    return list(set(args.minterms)), args.variable_count

def check_length(args, max_length):
    if len(args.minterms) > max_length:
        raise exceptions.InputLengthError("Too many minterms. ")

def check_minterms(args, max_value):
    for i in args.minterms:
        if i > max_value:
            raise exceptions.InvalidInputError("{} is out of range. " .format(i))
