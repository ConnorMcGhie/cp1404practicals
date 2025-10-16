"""
Colour name lookup program
"""

COLOUR_TO_HEX = {"Absolutezero": "#0048ba", "Acidgreen": "#b0bf1a", "Aliceblue": "#f0f8ff",
                 "Alizarincrimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
                 "Antiquewhite": "#faebd7", "Apricot": "#fbceb1", "Aqua": "#00ffff"}


colour_name = input("Enter a colour name: ").title()
while colour_name != "":
    try:
        print(f"The code for {colour_name} is {COLOUR_TO_HEX[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter a colour name: ").title()
