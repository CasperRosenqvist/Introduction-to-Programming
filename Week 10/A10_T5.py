########################################################
# Task A10_T5
# Developer Casper Rosenqvist
# Date 2025-12-10
########################################################


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    print("Program-starting.")
    n = int(input("Insert-factorial:"))
    print(f"Factorial {n}!")
    multipliers = "*".join(str(i) for i in range(1, n + 1))
    print(f"{multipliers} = {factorial(n)}")
    print("Program-ending.")

if __name__ == "__main__":
    main()
