# request current temperature
temperature = float(input("Enter the current temperature (in °C): "))

# Provide advice based on the temperature
if temperature > 30:
    print("It's too hot! Stay hydrated.")
elif 20 <= temperature <= 30:
    print("The weather is pleasant.")
elif 10 <= temperature <= 19:
    print("It's a bit chilly. Wear a sweater.")
else:
    print("It's very cold! Wear a jacket.")