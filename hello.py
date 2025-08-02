# Ask user for their name and remove whitespace from str and Capitalize user's name
name = input("What's your name? ").strip().title()

first, last = name.split(" ")

# Say hello to user
print(f"Hello, {first}")