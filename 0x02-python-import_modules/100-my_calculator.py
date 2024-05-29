#!/usr/bin/python3
import calculator_1
import sys
if __name__ == "__main__":
    num_args = len(sys.argv)
    if num_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]

    match operator:
        case "+":
	    print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
        case "-":
            print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
        case "*":
            print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
        case "/":
            print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
        case_:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

