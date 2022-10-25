def changeMaker():
    #this is an approximate answer based on what I remember the problem asking for
    cost = int(input("Please input the price of item in cents: (for example, 5, 75, 125, 1000)"))
    paid = int(input("Please input the total paid in cents: (for example, 5, 75, 125, 1000)"))

    change = paid - cost
    qCh = 0
    dCh = 0
    nCh = 0
    pCh = 0

    while change > 0:
        if change >= 25:
            change = change - 25
            qCh = qCh + 1
            #print("you're getting some quarters")
        elif change < 25:
            if change >= 20:
                change = change - 20
                dCh = dCh + 2
                #print("you're getting 2 dimes")
            elif change >= 10:
                change = change - 10
                dCh = dCh + 1
                #print("you're getting a dime")
            elif change >= 5:
                change = change - 5
                nCh = nCh + 1
                #print("you're getting a nickle")
            elif change >= 1:
                change = change - 1
                pCh = pCh + 1
            #    print("you're getting a penny")
    print(f"You are owed {qCh} quarters, {dCh} dimes, {nCh} nickles, and {pCh} pennies.")

changeMaker()
