# Laboratory 5 - Installment 5 
# Author: SOPIA MAGPANTAY

print("=" * 40)

print("\tEXPENSE TRACKER")
print("\tKnow where your money goes.")

print("=" * 40)

name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
subtotal = 0
count = 0
previous_big = False

print(f"Welcome, {name}!")

menu = (
    "MAIN MENU\n"
    "\t[1] Add an expense\n"
    "\t[2] View all expenses (coming soon)\n"
    "\t[3] Show total spent\n"
    "\t[4] Exit"
)


choice = ""

while choice !="4":
    print(menu)
    choice = input("Choose 1-4:" )

    if choice == "1":
        amount = float(input("Amount?: "))
        subtotal= subtotal + amount
        count = count + 1



        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")

        if amount > 100 and previous_big:
            print("  Two big expenses in a row - slow down!")

        previous_big = amount > 100

    elif choice == "2":
        print("  Coming soon: the tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        over_budget = total > budget
        left = budget - total

        print(f"  Expenses:     {count}")
        print(f"  Subtotal:     ${subtotal:.1f}")
        print(f"  Tax ({tax_percent:.1f}%):   ${tax:.1f}")
        print(f"  Grand total:  ${total:.1f}")

        if over_budget:
            print(f"Over budget by ${-left:.1f}!")
        elif total > budget * 0.9:
            print(f"Careful: only ${left:.1f} left.")
        else:
            print(f"Within budget. ${left:.1f} left.")

    elif choice == "4":
        print(f"Goodbye, {name}!")

    else:
        print("Please choose 1, 2, 3 or 4.")

print("-" * 40)
print(f"Made by: SOPIA MAGPANTAY  |  Installment 5")
print("=" * 40)

    






