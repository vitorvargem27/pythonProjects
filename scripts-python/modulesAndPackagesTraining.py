from functionsUtilities import data
from functionsUtilities import coins

number = float(input('Write a number in R$ for consult the math situations : \n').strip())
value = float(input('Write a value in R$ for add in the original value :\n').strip())
choose = str(input('You want see a real coin?[Y]/[N]\n')).strip().upper()
boolean = ''

decisionCoin = coins.decision(choose)
sumOfValues = data.increase(number, value, boolean)
subtraction = data.decrease(number, value, boolean)
double = data.doubleValue(number, boolean)
halfNumber = data.halfValue(number, boolean)

data.resume(decisionCoin, number, value, sumOfValues, subtraction, double, halfNumber)


