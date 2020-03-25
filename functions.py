
#replaces every vowel with the letter y
vowels = {"a", "e", "o","i"}


def translator():
    def translate(phrase):
        translation = ""
        for letter in phrase:
            if letter in vowels:
                translation = translation + "y"
            else:
                translation = translation + letter
        return translation

    print(translate(input("what do you want to translate? ").lower()))


translator()

num1 = float(input("Enter your first number: "))
op = input("Enter the operation you want to perform: ")
num2 = float(input("Enter your second number: "))


def calc():
    global result
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "/":
        result = num1 / num2
    elif op == "*":
        result = num1 * num2
    else:
        print("You didnt enter a valid operator")
    print(f" {num1} {op} {num2} = {result} ")


calc()









