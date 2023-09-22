#!/usr/bin/python3
def exponent(base=input("Base = "), exp=input("Exponent = ")):

    try:
        i = [int(b) for b in base.split()]
        n = [int(e) for e in exp.split()]

        if i == [] or n == []:
            print("Empty inputs!")
            exit()

        for x in i:
            for y in n:
                print(f"{x} raises to the power of {y} is: {x**y}")
                print(f"i.e: ({(str(x)+ ' * ')*(y-1)}{x}) = {x**y}")

    except ValueError:
        print("Must input numbers only!")
        exit()


exponent()
