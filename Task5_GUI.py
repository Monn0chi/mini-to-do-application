import tkinter as tk
from tkinter import messagebox, simpledialog
import sys
import os

# Add the current directory to the path so we can import Task5.py if needed
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class ContactBookGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book Manager")
        self.root.geometry("600x500")

        # Initialize contacts dictionary
        self.contacts = {}

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Title label
        title_label = tk.Label(self.root, text="Contact Book Manager",
                              font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Frame for buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        # Buttons
        tk.Button(button_frame, text="Add Contact", command=self.add_contact,
                 width=15, height=2).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(button_frame, text="View All Contacts", command=self.view_contacts,
                 width=15, height=2).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(button_frame, text="Search Contact", command=self.search_contact,
                 width=15, height=2).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(button_frame, text="Delete Contact", command=self.delete_contact,
                 width=15, height=2).grid(row=1, column=1, padx=5, pady=5)

        # Exit button
        tk.Button(self.root, text="Exit", command=self.exit_app,
                 width=10, height=2, bg="red", fg="white").pack(pady=10)

        # Text area to display contacts
        self.contacts_text = tk.Text(self.root, height=15, width=60, wrap=tk.WORD)
        self.contacts_text.pack(pady=10)
        self.contacts_text.config(state=tk.DISABLED)

        # Status label
        self.status_label = tk.Label(self.root, text="", fg="blue")
        self.status_label.pack(pady=5)

    def add_contact(self):
        # Create a dialog for name input
        name = simpledialog.askstring("Add Contact", "Enter contact name:")
        if name is None:  # User cancelled
            return

        name = name.strip()
        if not name:
            messagebox.showerror("Error", "Name cannot be empty!")
            return

        if name in self.contacts:
            messagebox.showinfo("Info", f"Contact '{name}' already exists with phone number: {self.contacts[name]}")
            return

        # Create a dialog for phone input
        phone = simpledialog.askstring("Add Contact", "Enter phone number:")
        if phone is None:  # User cancelled
            return

        phone = phone.strip()
        if not phone:
            messagebox.showerror("Error", "Phone number cannot be empty!")
            return

        self.contacts[name] = phone
        self.status_label.config(text=f"Contact '{name}' added successfully!", fg="green")
        self.update_contacts_display()

    def view_contacts(self):
        if not self.contacts:
            self.status_label.config(text="Your contact book is empty.", fg="orange")
        else:
            self.status_label.config(text=f"Total contacts: {len(self.contacts)}", fg="blue")
        self.update_contacts_display()

    def search_contact(self):
        if not self.contacts:
            messagebox.showinfo("Info", "Your contact book is empty.")
            return

        search_name = simpledialog.askstring("Search Contact", "Enter contact name to search:")
        if search_name is None:  # User cancelled
            return

        search_name = search_name.strip()
        if not search_name:
            messagebox.showerror("Error", "Name cannot be empty!")
            return

        if search_name in self.contacts:
            result = f"Contact found!\nName: {search_name}\nPhone: {self.contacts[search_name]}"
            messagebox.showinfo("Search Result", result)
            self.status_label.config(text=f"Contact '{search_name}' found.", fg="green")
        else:
            messagebox.showerror("Not Found", f"Contact '{search_name}' not found in your contact book.")
            self.status_label.config(text=f"Contact '{search_name}' not found.", fg="red")

    def delete_contact(self):
        if not self.contacts:
            messagebox.showinfo("Info", "Your contact book is empty. Nothing to delete.")
            return

        # Show current contacts
        self.update_contacts_display()

        delete_name = simpledialog.askstring("Delete Contact", "Enter contact name to delete:")
        if delete_name is None:  # User cancelled
            return

        delete_name = delete_name.strip()
        if not delete_name:
            messagebox.showerror("Error", "Name cannot be empty!")
            return

        if delete_name in self.contacts:
            confirm = messagebox.askyesno("Confirm Deletion",
                                        f"Are you sure you want to delete '{delete_name}' (Phone: {self.contacts[delete_name]})?")
            if confirm:
                deleted_phone = self.contacts[delete_name]
                del self.contacts[delete_name]
                messagebox.showinfo("Success", f"Contact '{delete_name}' (Phone: {deleted_phone}) deleted successfully!")
                self.status_label.config(text=f"Contact '{delete_name}' deleted.", fg="green")
                self.update_contacts_display()
            else:
                self.status_label.config(text="Deletion cancelled.", fg="orange")
        else:
            messagebox.showerror("Not Found", f"Contact '{delete_name}' not found in your contact book.")
            self.status_label.config(text=f"Contact '{delete_name}' not found.", fg="red")

    def update_contacts_display(self):
        self.contacts_text.config(state=tk.NORMAL)
        self.contacts_text.delete(1.0, tk.END)

        if not self.contacts:
            self.contacts_text.insert(tk.END, "No contacts in your contact book.")
        else:
            self.contacts_text.insert(tk.END, "--- All Contacts ---\n\n")
            for name, phone in sorted(self.contacts.items()):
                self.contacts_text.insert(tk.END, f"Name: {name}\nPhone: {phone}\n\n")

        self.contacts_text.config(state=tk.DISABLED)

    def exit_app(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.quit()

def main():
    root = tk.Tk()
    app = ContactBookGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()