def GetAvailableMoney():
    AvailableMoneyFunc = int(input("How much is your money?: "))
    return AvailableMoneyFunc

def GetQuantityOfAppleYouWant():
    QuantityOfAppleYouWantFunc = int(input("How much is the apples?: "))
    return QuantityOfAppleYouWantFunc

def GetQuantityYouCanBuy(TotalAmountOfMoneyYouCanSpendF, TotalQuantityOfAppleYouWantToPurchaseF):
    GetQuantityYouCanBuyFunc = (TotalAmountOfMoneyYouCanSpendF) // (TotalQuantityOfAppleYouWantToPurchaseF)
    return GetQuantityYouCanBuyFunc


def GetTotalChange(TotalAmountOfMoneyYouCanSpendF, TotalQuantityOfAppleYouWantToPurchseF):
    GetTotalChangeFunc = float(TotalAmountOfMoneyYouCanSpendF) % (TotalQuantityOfAppleYouWantToPurchseF)
    return GetTotalChangeFunc

def DisplayOutput(GetQuantityYouCanBuyf, GetTotalChangeF):
    print(f"You Can Buy{YouCanBuy} apples and you change is {YourChangeIs}")



TotalAmountOfMoneyYouCanSpend = GetAvailableMoney()
TotalQuantityOfAppleYouWantToPurchase = GetQuantityOfAppleYouWant()


YouCanBuy = GetQuantityYouCanBuy(TotalAmountOfMoneyYouCanSpend, TotalQuantityOfAppleYouWantToPurchase)
YourChangeIs = GetTotalChange(TotalAmountOfMoneyYouCanSpend, TotalQuantityOfAppleYouWantToPurchase)

print(f"You Can Buy{YouCanBuy} apples and you change is {YourChangeIs}")
