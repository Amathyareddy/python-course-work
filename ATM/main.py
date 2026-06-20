import logic as lg

if lg.logic():
    print("==========Welcome to the ATM==========")
    while True:
        lg.menu()
        ch = input("Enter the choice: ").lower()
        if ch == 'c':
            lg.checkBalance()
        elif ch == 'd':
            lg.deposit()
        elif ch == 'w':
            lg.withdraw()
        elif ch == 'v':
            lg.viewTransactions()
        elif ch=='e':
            print("Thankyou")
            break
