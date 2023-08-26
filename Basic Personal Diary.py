def write_diary(entry):
    with open("diary.txt", "a") as file:
        file.write(entry + "\n")
    print("Entry added to diary.")

def read_diary():
    try:
        with open("diary.txt", "r") as file:
            content = file.read()
            print("Diary entries:")
            print(content)
    except FileNotFoundError:
        print("No diary entries yet.")

while True:
    print("\nMenu:")
    print("1. Write Diary Entry")
    print("2. Read Diary Entries")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        entry = input("Write your diary entry: ")
        write_diary(entry)
    elif choice == "2":
        read_diary()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
