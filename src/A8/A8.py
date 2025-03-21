import tkinter as tk
from tkinter import scrolledtext, messagebox
import os

def add_note(filename, note_text):
    """Adds a note to a file."""
    try:
        with open(filename, "a") as f:
            f.write(note_text + "\n")
        messagebox.showinfo("Success", "Note added successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error adding note: {e}")

def view_notes(filename, text_widget):
    """Views all notes in a file."""
    text_widget.delete(1.0, tk.END)  # Clear the text widget
    if not os.path.exists(filename):
        messagebox.showinfo("Info", "No notes found.")
        return

    try:
        with open(filename, "r") as f:
            notes = f.readlines()
            if not notes:
                messagebox.showinfo("Info", "No notes found.")
                return

            text_widget.insert(tk.END, "--- Notes ---\n")
            for index, note in enumerate(notes):
                text_widget.insert(tk.END, f"{index + 1}. {note}")

    except Exception as e:
        messagebox.showerror("Error", f"Error viewing notes: {e}")

def clear_notes(filename):
    """Clears all notes from a file."""
    if not os.path.exists(filename):
        messagebox.showinfo("Info", "No notes found.")
        return

    try:
        with open(filename, "w") as f:
            f.write("")
        messagebox.showinfo("Success", "Notes cleared successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error clearing notes: {e}")

def main():
    filename = "notes.txt"

    window = tk.Tk()
    window.title("Note-Taking App")

    # Note input
    note_label = tk.Label(window, text="Enter Note:")
    note_label.pack()
    note_entry = scrolledtext.ScrolledText(window, height=5, width=40)
    note_entry.pack()

    # Buttons
    add_button = tk.Button(window, text="Add Note", command=lambda: add_note(filename, note_entry.get(1.0, tk.END).strip()))
    add_button.pack()

    view_button = tk.Button(window, text="View Notes", command=lambda: view_notes(filename, notes_text))
    view_button.pack()

    clear_button = tk.Button(window, text="Clear Notes", command=lambda: clear_notes(filename))
    clear_button.pack()

    notes_text = scrolledtext.ScrolledText(window, height=15, width=50)
    notes_text.pack()

    window.mainloop()

if __name__ == "__main__":
    main()