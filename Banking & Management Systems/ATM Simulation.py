print("                                                    ATM Simulation")                         # 52 Spaces
print("                                                       ABCD Bank")                            # 55 Spaces
balance = 100000
pin = 1234

while True:
    print("1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Change PIN\n5. Exit\n")
    choice = int(input("Enter Choice(1-5): "))
    print("\n"*1)
    if choice == 1:
        print("Balance: ",balance,"/-\n")

    elif choice == 2:
        amt = float(input("Enter Amount: "))
        balance+=amt
        print("Money Deposited Successfully!")
        print("Current Balance: ",balance,"/-\n")
        
    elif choice == 3:
        pinn = int(input("Enter PIN: "))
        if pinn == pin:
            amnt = float(input("Enter Amount: "))
            balance -=amnt
            print("Transaction Successfull!\n")
        else:
                print("Incorrect PIN")
                print("2 Attempts Left\n")
                pinn = int(input("Enter PIN: "))
                if pinn == pin:
                    amnt = float(input("Enter Amount: "))
                    balance -=amnt
                    print("Transaction Successfull!")
                else:
                    print("Incorrect PIN")
                    print("1 Attempt Left\n")
                    pinn = int(input("Enter PIN: "))
                    if pinn == pin:
                        amnt = float(input("Enter Amount: "))
                        balance -=amnt
                        print("Transaction Successfull!\n")
                    else:
                        print("Incorrect PIN !\nLocking Account....\nAccount Locked.\n")
                        break
                
    elif choice == 4:
        new_pin = int(input("New PIN: "))
        confirm_pin = int(input("Confirm PIN: "))
        if new_pin == confirm_pin:
            pin = new_pin
            print("PIN Updated Successfully!\n")
        else:
            print("New PIN and Confirm PIN not matched.\n")
            new_pin = int(input("New PIN: "))
            confirm_pin = int(input("Confirm PIN: "))
            if new_pin == confirm_pin:
                pin = new_pin
                print("PIN Updated Successfully!\n")
            else:
                print("\n")

    elif choice == 5:
        print("Exiting....")
        print("Thank You")
        break

