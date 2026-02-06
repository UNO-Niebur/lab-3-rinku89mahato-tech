#TempConvert.py
#Name:
#Date:
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature
  Fahrenheit = input("What is the temprature in Fahrenheit: ")
  
  f = float(Fahrenheit)
  
  #Convert that temperature to celsius, rounding to 1 decimal percision

  Celsius = (f - 32)* 5/9

  Celsius_rounded = round (Celsius,1)

  #Output converted temperature.

  print( Celsius_rounded)



  #tempF = 80
  #tempC = tempF / 2
  #print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
