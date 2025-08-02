#def hello(to="world"):
#    print("hello,", to)

# Ask user for their name and remove whitespace from str and Capitalize user's name

def main():
    name = input("What's your name? ").strip().title()
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()