import os

def add_note(filename, note):
    """Adds a note to a file."""
    try:
        with open(filename, "a") as f:  # 'a' for append mode
            f.write(note + "\n")
        print("Note added successfully!")
    except Exception as e:
        print(f"Error adding note: {e}")

def view_notes(filename):
    """Views all notes in a file."""
    if not os.path.exists(filename):
        print("No notes found.")
        return

    try:
        with open(filename, "r") as f:
            notes = f.readlines()
            if not notes:
                print("No notes found.")
                return

            print("\n--- Notes ---")
            for index, note in enumerate(notes):
                print(f"{index + 1}. {note.strip()}") #strip removes newline characters.

    except Exception as e:
        print(f"Error viewing notes: {e}")

def clear_notes(filename):
    """Clears all notes from a file."""
    if not os.path.exists(filename):
        print("No notes found.")
        return

    try:
        with open(filename, "w") as f: # 'w' for write mode, which overwrites the file
            f.write("")  # Clear the file
        print("Notes cleared successfully!")
    except Exception as e:
        print(f"Error clearing notes: {e}")

def main():
    filename = "notes.txt"  # Default filename

    while True:
        print("\nNote-Taking App")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Clear Notes")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            note = input("Enter your note: ")
            add_note(filename, note)
        elif choice == "2":
            view_notes(filename)
        elif choice == "3":
            clear_notes(filename)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()