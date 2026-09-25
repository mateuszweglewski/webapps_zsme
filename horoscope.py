import random

print("=== DEVELOPER HOROSCOPE ===")
name = input("What's your name? ")
language = input("Favourite programming language? ").lower()
sleep = input("How many hours did you sleep last night? ")

if not sleep.isdigit():
    print("That's not a number. Even your horoscope is confused.")
    exit()

sleep = int(sleep)

predictions = [
    "your code will compile on the first try. Enjoy it, it won't happen again.",
    "a missing semicolon will ruin your afternoon.",
    "Stack Overflow will have exactly the answer you need. From 2011.",
    "you will fix a bug and create two new ones.",
    "your teacher will ask you to write documentation. Good luck.",
]

print(f"\nDear {name}, today {random.choice(predictions)}")

if language == "python":
    print("Python fans get +10 luck today.")
elif language == "html":
    print("HTML is not a programming language. -10 luck.")

if sleep < 5:
    print("Warning: low sleep detected. Coffee recommended.")
elif sleep > 10:
    print("Too much sleep. Are you sure you're a programmer?")

if name.lower() == "admin":
    print("Access granted. Just kidding, this is a horoscope.")
