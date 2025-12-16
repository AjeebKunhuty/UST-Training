from Pmodule import ctof, ftoc

cels = int(input("Enter temperature in Celsius: "))
fah = ctof(cels)
print(f"{cels} degree Celsius is equal to {fah} degree Fahrenheit")

fahs = int(input("Enter temperature in Fahrenheit: "))
cel = ftoc(fahs)
print(f"{fahs} degree Fahrenheit is equal to {cel} degree Celsius")