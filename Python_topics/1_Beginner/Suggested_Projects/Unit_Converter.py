def unit_converter():
    def length_conversion(value, from_unit, to_unit):
        length_units = {
            "meters": 1,
            "kilometers": 0.001,
            "miles": 0.000621371,
            "inches": 39.3701,
            "feet": 3.28084
        }
        return value / length_units[from_unit] * length_units[to_unit]

    def weight_conversion(value, from_unit, to_unit):
        weight_units = {
            "kilograms": 1,
            "grams": 1000,
            "pounds": 2.20462,
            "ounces": 35.274
        }
        return value / weight_units[from_unit] * weight_units[to_unit]

    def temperature_conversion(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == "celsius":
            return value * 9/5 + 32 if to_unit == "fahrenheit" else value + 273.15
        if from_unit == "fahrenheit":
            return (value - 32) * 5/9 if to_unit == "celsius" else (value - 32) * 5/9 + 273.15
        if from_unit == "kelvin":
            return value - 273.15 if to_unit == "celsius" else (value - 273.15) * 9/5 + 32

    def volume_conversion(value, from_unit, to_unit):
        volume_units = {
            "liters": 1,
            "milliliters": 1000,
            "gallons": 0.264172,
            "cups": 4.22675
        }
        return value / volume_units[from_unit] * volume_units[to_unit]

    # User interface
    while True:
        print("\nUnit Converter")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Volume")
        print("5. Exit")
        choice = input("Choose a category (1-5): ")

        if choice == "5":
            print("Exiting the Unit Converter. Goodbye!")
            break

        converters = {
            "1": ("Length", length_conversion, ["meters", "kilometers", "miles", "inches", "feet"]),
            "2": ("Weight", weight_conversion, ["kilograms", "grams", "pounds", "ounces"]),
            "3": ("Temperature", temperature_conversion, ["celsius", "fahrenheit", "kelvin"]),
            "4": ("Volume", volume_conversion, ["liters", "milliliters", "gallons", "cups"])
        }

        if choice in converters:
            category, func, units = converters[choice]
            print(f"\n{category} Conversion")
            print(f"Available units: {', '.join(units)}")
            from_unit = input("Convert from: ").lower()
            to_unit = input("Convert to: ").lower()
            value = float(input(f"Enter the value in {from_unit}: "))

            if from_unit in units and to_unit in units:
                result = func(value, from_unit, to_unit)
                print(f"{value} {from_unit} is equal to {result:.4f} {to_unit}.")
            else:
                print("Invalid unit entered. Please try again.")
        else:
            print("Invalid choice. Please select a valid category.")

unit_converter()
