from pyfiglet import Figlet

def header():
    """Show the name as ASCII art."""
    f = Figlet(font='slant')
    f = f.renderText("OpenCode")
    print(f)

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
ascii_value()
