#TempConvert.py
#Name:Rinku Mahato
#Date:02/06/2026
#Assignment: Convert the temprature from Fahrenheit to Celsius with rounding to 1 decimal precision.


def main():
  #Prompt the user for a Fahrenheit temperature
  fahrenheit = input("What is the temprature in fahrenheit: ")
  
  f = float(fahrenheit)
  
  #Convert that temperature to celsius, rounding to 1 decimal percision

  celsius = (f - 32)*5/9

  celsius_rounded = round(celsius,1)

  #Output converted temperature.

  print(f"Temprature in celsius: {celsius_rounded}")

  #tempF = 80
  #tempC = tempF / 2
  #print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
