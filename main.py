from pyfiglet import Figlet


def header():
    """Show the name as ASCII art."""
    f = Figlet(font='slant')
    f = f.renderText("OpenCode")
    print(f)


# Gives you the ability to select how to use the program
def selection():
    active = True
    print('Welcome to Opencode! \n'
          'To get started, type the number of the list that refers to the thing you want to do\n'
          'To get the full list, just type "0"')

    while active:
        list_number = int(input("Enter the number here: "))
        if list_number == 0:
            print("1 - Ascii calculator: Gives you the Ascii value of a character")
            continue
        elif list_number == 1:
            active = False
            ascii_value()
        else:
            print("Not a valid number")
            continue


# Python program to print ASCII Value of Character
def ascii_value():
    character_input = input("Enter Character you want to know the ASCII Value of: ")
    try:
        ascii_number = ord(character_input)
        print("The ASCII value of '" + character_input + "' is", ascii_number)
    except TypeError:
        print("Please input a single character")
        return ascii_value()


header()
selection()
