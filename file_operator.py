import os
from datetime import datetime

filename = "journal.txt"

while True:
    print("\nWelcome to Personal Journal Manager!")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        entry = input("Enter your journal entry: ")
        with open(filename, "a") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n")
            f.write(entry + "\n\n")
        print("Entry added successfully!")

    elif choice == "2":
        if os.path.exists(filename):
            print("\nYour Journal Entries:")
            print("-" * 40)
            with open(filename, "r") as f:
                print(f.read())
        else:
            print("No journal entries found. Start by adding a new entry!")

    elif choice == "3":
        if os.path.exists(filename):
            keyword = input("Enter a keyword or date to search: ")
            found = False
            with open(filename, "r") as f:
                lines = f.read()
                if keyword.lower() in lines.lower():
                    print("\nMatching Entries:")
                    print("-" * 40)
                    print(lines)
                    found = True
            if not found:
                print(f"No entries were found for the keyword: {keyword}")
        else:
            print("Error: The journal file does not exist. Please add a new entry first.")

    elif choice == "4":
        if os.path.exists(filename):
            confirm = input("Are you sure you want to delete all entries? (yes/no): ")
            if confirm.lower() == "yes":
                open(filename, "w").close()
                print("All journal entries have been deleted.")
        else:
            print("No journal entries to delete.")

    elif choice == "5":
        print("Thank you for using Personal Journal Manager. Goodbye!")
        break

    else:
        print("Invalid option. Please select a valid option from the menu.")
