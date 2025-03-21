def todo_list():
    """
    A simple to-do list program using if statements and loops.
    """

    todo_items = []

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add item")
        print("2. View list")
        print("3. Mark item as done (remove)")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter the item to add: ")
            todo_items.append(item)
            print("Item added!")

        elif choice == "2":
            if not todo_items:  # Check if the list is empty
                print("Your to-do list is empty.")
            else:
                print("\nTo-Do List:")
                for index, item in enumerate(todo_items):
                    print(f"{index + 1}. {item}")

        elif choice == "3":
            if not todo_items:
                print("Your to-do list is empty.")
            else:
                print("\nTo-Do List:")
                for index, item in enumerate(todo_items):
                    print(f"{index + 1}. {item}")

                try:
                    item_number = int(input("Enter the item number to mark as done: ")) - 1 #Corrected to -1 to account for 0 indexing.
                    if 0 <= item_number < len(todo_items):
                        removed_item = todo_items.pop(item_number)
                        print(f"'{removed_item}' marked as done!")
                    else:
                        print("Invalid item number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo_list()