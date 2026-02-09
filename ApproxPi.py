#ApproxPi.py
#Name: Rinku Mahato
#Date: 02/08/2026
#Assignment: calculate pi using the approximation technique.
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)
  decimal_precision = int(input(" set decimal precision (0-10): "))
 
  
  start = time.time()
  #calculate pi using the approximation technique
  #Loop until the level of percision is reached
  approxpi = 4/1
  sign = -1
  denom = 3
  while round(approxpi, decimal_precision) != round(realPi, decimal_precision):
    print(approxpi)
    approxpi = approxpi + (sign * 4 / denom)

    sign = sign * -1
    denom = denom + 2

  end = time.time()

  elapsedTime = end - start
  print(elapsedTime)

if __name__ == '__main__':
  main()
