import re
def checkbalance():
    global Balance
    print(f"Your balance is: {Balance}")
    print()

def depositamount(amount):
    global Balance
    if amount > 0:
        Balance+=amount
        print(f"Your new balance is: {Balance}")
        print()
    else:
        print("Amount can't be negative for Deposit. Try again.")
        print()

def withdrawamount(amount):
    global Balance
    if amount>Balance:
        print(f"Insufficient balance. Try again with less than {Balance}")
        print()
    else:
        Balance-=amount
        print(f"Your new balance is: {Balance}")
        print()
def checkkyc():
    if len(Docs)==0:
        print("Your kyc is not updated")
        print()
    else:
        print("Your kyc is updated")
        print()

def view_kyc():
    if len(Docs)==0:
        print("No KYC documents found.")
        print()
    else:
        print("KYC Documents:")
        for docs, number in Docs.items():
            print(f"{docs}: {number}")
            print()

def kycupdate(name, number):
    global Docs

    doc_name = name.upper()
    doc_number = number

    if doc_name == "AADHAR":
        if len(doc_number) != 12 or not doc_number.isdigit():
            print("Please enter a valid Aadhar number")
            return

    elif doc_name == "PAN":
        if not re.fullmatch(r"[A-Z]{5}[0-9]{4}[A-Z]", doc_number):
            print("Please enter a valid PAN number")
            return
    else:
        print("Unsupported KYC document")
        return

    if doc_name in Docs:
        print(f"{doc_name} already exists. Updating document number.")
    else:
        print(f"{doc_name} added successfully.")

    Docs[doc_name] = doc_number

Docs={}
Balance = 0
print("-------------------------------------")
print("Welcome to the Small Banking App")
print("-------------------------------------")


while True:
    print("1. Check Balance")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Check kyc")
    print("5. Kyc update")
    print("6. View kyc")
    print("7. Exit")
    print("-------------------------------------")

    choice = input("Enter your choice: ")
    if choice == "1":
        checkbalance()
    elif choice == "2":
        try:
            depositamount(float(input("Enter the amount to deposit: ")))
        except ValueError:
            print("Please enter a numeric value")
    elif choice == "3":
        try:
            withdrawamount(float(input("Enter the amount to withdraw: ")))
        except ValueError:
            print("Please enter a numeric value")
    elif choice == "4":
        checkkyc()
    elif choice == "5":
        #print("Enter the document Name and number")
        name=input("Enter the document Name (Aadhar/PAN): ")
        number=input("Enter the document Number: ")
        kycupdate(name,number)
        continue
    elif choice == "6":
        view_kyc()
    elif choice == "7":
        print("Thank you for using this application. Goodbye!")
        break
    else:
        print("That is not a valid choice. Try again.")


