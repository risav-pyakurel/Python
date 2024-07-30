# Write a program that will convert celsius value to fahrenheit

def celcius_to_fahrenheit(celcius):
    fehrenheit = (9 / 5 * celcius) + 32
    return fehrenheit


celcius = float(input("enter the celcius you want to convert"))
fehrenheit = celcius_to_fahrenheit(celcius)
print(f"The converted celcius is {fehrenheit}")