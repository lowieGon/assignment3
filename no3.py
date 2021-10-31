print("The price of apple is 20 pesos")
print("The price of orange is 25 peos")

ApplePrice = 20
OrangePrice = 25

def GetTotalBoughtApple():
    QuantityOfAppleFunc= int(input("How many apples would you like to purchase?: "))
    return QuantityOfAppleFunc

def GetTotalBoughtOrange():
    QuantityOfOrangeFunc= int(input("How many oranges would you like to purchase: "))
    return QuantityOfOrangeFunc


def GetTotalAmountOfPurchase(ApplePriceF, OrangePriceF, AppleAmount, OrangeAmount):
    AmountOfPurchaceFunc= (AppleAmount*ApplePriceF) + (OrangeAmount*OrangePriceF)
    return AmountOfPurchaceFunc

def Displayoutput(AmountFunc):
    print(f"The total amount is {amount}.")

AppleBought = GetTotalBoughtApple()
OrangeBought = GetTotalBoughtOrange()

amount = GetTotalAmountOfPurchase (ApplePrice, OrangePrice, AppleBought, OrangeBought)
Displayoutput(amount)