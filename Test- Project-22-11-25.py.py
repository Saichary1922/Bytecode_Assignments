#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Welcome to HDFC Bank ATM")

balance = 100000
correct_pin = "2004"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    pin = input("Enter PIN: ")
    
    if pin == correct_pin:
        print("Access Granted!\n")
        
        while True:
            print("1.Check Balance")
            print("2.Withdraw Cash")
            print("3.Deposit Cash")
            print("4.Change PIN")
            print("5.Exit")
            
            choice = input("Choose (1-5): ")
            
            if choice == "1":
                print(f"Your balance: ₹{balance}\n")
            
            elif choice == "2":
                amount = int(input("Enter amount to withdraw:"))
                
                if amount <= 0:
                    print("Invalid amount!\n")
                elif amount % 100 != 0:
                    print("Amount must be in multiples of 100!\n")
                elif amount > balance:
                    print("Insufficient balance!\n")
                else:
                    balance -= amount
                    print(f"Withdrawal Successful! New balance: ₹{balance}\n")
            
            elif choice == "3":
                amount = int(input("Enter amount to deposit: "))
                if amount <= 0:
                    print("Invalid deposit amount!\n")
                else:
                    balance += amount
                    print(f"Deposit Successful! New balance: ₹{balance}\n")
            
            elif choice == "4":
                old_pin = input("Enter old PIN: ")
                
                if old_pin == correct_pin:
                    new_pin = input("Enter new 4-digit PIN: ")
                    
                    if len(new_pin) == 4 and new_pin.isdigit():
                        correct_pin = new_pin
                        print("PIN changed successfully!\n")
                    else:
                        print("PIN must be exactly 4 digits!\n")
                else:
                    print("Incorrect old PIN!\n")
            
            elif choice == "5":
                print("Thank You for using HDFC Bank ATM!")
                break
            
            else:
                print("Invalid option! Please choose between 1-5.\n")
        
        break  
    
    else:
        attempts += 1
        remaining = max_attempts - attempts
        
        if remaining > 0:
            print(f"Wrong PIN! {remaining} attempts left.\n")
        else:
            print("Card Blocked! Too many wrong attempts.\n")


# In[ ]:




