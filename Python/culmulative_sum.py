#!/usr/bin/python3

def summ(n=input("Enter a number: ")):
    try:
        N = [int(i) for i in n.split()]
        if len(N) > 1:
            return "Please enter only one number!"
            exit()

        return f"Sum from 1 to {n} is: {sum(list(range(int(n) + 1)))}"

    except ValueError:
        return "Invalid input!"
        exit()


print(summ())
