import random
#Lists of letters, numbers and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Starting of the program
print("Welcome to the Abhigyan's Python Password Generator!")
no_letters = int(input("How many letters do you want in your password?\n"))
no_symbols = int(input(f"How many symbols do you want?\n"))
no_numbers = int(input(f"How many numbers do you want?\n"))

passcode = []
for alphabet in range(1, no_letters + 1):
    al = random.choice(letters)
    passcode.append(al)
for number in range(1, no_numbers + 1):
    num = random.choice(numbers)
    passcode.append(num)
for symbol in range(1, no_symbols + 1):
    sym = random.choice(symbols)
    passcode.append(sym)
random.shuffle(passcode)
result = ""
for char in passcode:
    result += char
print(result)
