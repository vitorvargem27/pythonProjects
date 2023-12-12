def increase(value, increasedValue, boolean='') :
    finalValue = value + increasedValue
    return finalValue

def decrease(value, decreasedValue, boolean='') :
    finalValue = value - decreasedValue
    return finalValue

def doubleValue(value, boolean='') :
    totalValue = value * 2
    return totalValue

def halfValue(value, boolean='') :
    totalValue = value / 2
    return totalValue

def resume(real, numberValue, numver02Value, sum, subtractionValue, doubleValue, half ) :
    print(f"The sum of {real}{numberValue} and {real}{numver02Value} is {real}{sum}")
    print(f"The subtraction of {real}{numberValue} and {real}{numver02Value} is {real}{subtractionValue}")
    print(f"The double of {real}{numberValue} is {real}{doubleValue}")
    print(f"The half of {real}{numberValue} is {real}{half}")