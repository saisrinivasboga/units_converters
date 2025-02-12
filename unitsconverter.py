def length_converter():
    print("\nLength Converter:")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Meters")
    
    choice = input("Choose an option (1 or 2): ").strip()
    
    if choice == "1":
        value = float(input("Enter length in meters: "))
        print(f"{value} meters = {value / 1000} kilometers")
    elif choice == "2":
        value = float(input("Enter length in kilometers: "))
        print(f"{value} kilometers = {value * 1000} meters")
    else:
        print("Invalid choice!")

def temperature_converter():
    choice = input("\nConvert: (C to F / F to C): ").strip().lower()
    if choice == "c to f":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit}°F")
    elif choice == "f to c":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F = {celsius}°C")
    else:
        print("Invalid choice!")

def weight_converter():
    value = float(input("\nEnter weight in kilograms: "))
    print(f"{value} kg = {value * 2.20462} pounds")

def main():
    while True:
        print("\nUnit Converter")
        print("1. Length Converter (Meters/Kilometers)")
        print("2. Temperature Converter (Celsius/Fahrenheit)")
        print("3. Weight Converter (Kilograms/Pounds)")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            length_converter()
        elif choice == "2":
            temperature_converter()
        elif choice == "3":
            weight_converter()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
