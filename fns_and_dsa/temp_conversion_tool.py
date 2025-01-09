FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
        return  (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp = float(input("Enter the temperature to convert: "))
        temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()
    except ValueError:
        print("Invalid temperature. Please enter a numeric value..")
        return
    
    if temp_type == 'f':
        celsius = convert_to_celsius(temp)
        print(f"{temp}°F is {celsius:.2f}°C")
        
    elif temp_type == 'c':
        fahrenheit = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {fahrenheit:.2f}°F")
    else:
        print("Please enter valid temperature.")

if __name__ == "__main__":
    main()