buyTotal = 0
price1000Quantity = 0
productName = ''

buy = True

while buy :
    productName = str(input("What's the name of product that you want buy?\n")).strip().title()
    price = float(input("Hou much is the price of this product?\n").strip())
    buyTotal += price

    if price > 1000 :
        price1000Quantity += 1

    if price < price :
        productName = productName

    choose = str(input('You want continue?[\033[1:32mY\033[m]/[\033[1:31mN\033[m]\n')).strip().upper()

    while choose != 'N' and choose != 'Y' :
        print('\033[1:31mWrite a correct choose\033[m')
        choose = str(input('You want continue?[\033[1:32mY\033[m]/[\033[1:31mN\033[m]\n')).strip().upper()

    if choose == 'N' :
        break

print(f"\nThe total value of your buy was R${buyTotal}")
print(f"The quantity of product that the price over R$1000 is {price1000Quantity}")
print(f"The product that lower price is {productName}")
