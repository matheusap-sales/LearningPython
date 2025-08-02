def main():
    x = int(input("Tell me a number: "))
    print(f"The number {x} is " + evenOrNot(x))


def evenOrNot(n):
    if (float(n) % 2 == 0):
        return "Even"

    else:
        return "Not Even"

main()