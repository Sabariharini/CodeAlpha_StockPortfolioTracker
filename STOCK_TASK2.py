stock_prices={
    "AAPL":180,
    "TSLA":250
}
tot_inv=0
print("Stock Portfolio Tracker")
while True:
    stock = input("Enter stock symbol (or'done' to finish):").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock symbol not found. Please try again.")
        continue
    quantity=int(input("Enter quantity:"))
    price=stock_prices[stock]
    inv = price * quantity 
    print("Stock Price:",price)
    print("Quantity:",quantity)
    print("Investment:",inv)

    tot_inv += price * quantity 
    print("--------------------------------------")
    print("Total Investment:",tot_inv)
    print("Thank you ! ")       

