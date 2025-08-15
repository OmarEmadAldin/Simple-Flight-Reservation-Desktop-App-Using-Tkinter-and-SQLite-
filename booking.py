import tkinter as tk
from tkinter import messagebox
import database
from tkcalendar import DateEntry
import datetime

class BookFlightPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f8f9fa")
        self.controller = controller
        self.entries = {}

        from home import HomePage  # Import inside method to avoid circular import

        tk.Label(self, text="Book a Flight", font=("Arial", 22, "bold"),
                 bg="#f8f9fa", fg="#005b96").pack(pady=20)

        card_frame = tk.Frame(self, bg="white", bd=1, relief="solid")
        card_frame.pack(pady=10, ipadx=30, ipady=20)

        self.create_field(card_frame, "Full Name", "Enter your full name", 0, 0, colspan=2)
        self.create_field(card_frame, "Flight Number", "e.g. FS123", 1, 0, colspan=2)
        self.create_field(card_frame, "Departure", "e.g. New York", 2, 0)
        self.create_field(card_frame, "Destination", "e.g. London", 2, 1)
        self.create_field(card_frame, "Date", "Pick a date", 3, 0)
        self.create_field(card_frame, "Seat Number", "e.g. 12A", 3, 1)

        btn_frame = tk.Frame(self, bg="#f8f9fa")
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="Cancel", font=("Arial", 12), width=12,
                  bg="white", fg="black", relief="solid", bd=1,
                  command=lambda: controller.show_frame(HomePage)).pack(side="left", padx=10)

        tk.Button(btn_frame, text="Book Flight", font=("Arial", 12, "bold"), width=12,
                  bg="#007bbf", fg="white", relief="flat",
                  command=self.save_reservation).pack(side="left", padx=10)
    def create_field(self, parent, label_text, placeholder, row, col, colspan=1):
        tk.Label(parent, text=label_text, font=("Arial", 11, "bold"), bg="white").grid(
            row=row * 2, column=col, sticky="w", padx=5, pady=(5, 0), columnspan=colspan
        )

        if label_text == "Date":
            entry = DateEntry(parent, date_pattern="dd/mm/yyyy",  # Force format
                            background="darkblue", foreground="white", borderwidth=2)
        else:
            entry = tk.Entry(parent, font=("Arial", 11), width=30, fg="gray")
            entry.insert(0, placeholder)
            entry.bind("<FocusIn>", lambda e, ent=entry, ph=placeholder: self.clear_placeholder(ent, ph))
            entry.bind("<FocusOut>", lambda e, ent=entry, ph=placeholder: self.add_placeholder(ent, ph))

        entry.grid(row=row * 2 + 1, column=col, padx=5, pady=(0, 10), columnspan=colspan, sticky="we")
        self.entries[label_text] = entry
    def clear_placeholder(self, entry, placeholder):
        if entry.get() == placeholder and entry.cget("fg") == "gray":
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def add_placeholder(self, entry, placeholder):
        if entry.get().strip() == "":
            entry.insert(0, placeholder)
            entry.config(fg="gray")

    def save_reservation(self):
        from datetime import datetime

        data = {field: entry.get() for field, entry in self.entries.items()}

        # Validate date
        try:
            datetime.strptime(data["Date"], "%d/%m/%Y")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid date in DD/MM/YYYY format.")
            return

        # Other field validation...
        if any(v.strip() == "" or v in [
            "Enter your full name", "e.g. FS123", "e.g. New York",
            "e.g. London", "Pick a date", "e.g. 12A"
        ] for v in data.values()):
            messagebox.showerror("Error", "All fields are required.")
            return

        import database
        database.add_reservation(data["Full Name"], data["Flight Number"], data["Departure"],
                                data["Destination"], data["Date"], data["Seat Number"])
        messagebox.showinfo("Success", "Reservation added successfully.")

    def create_field_placeholders(self):
        placeholders = [
            ("Full Name", "Enter your full name"),
            ("Flight Number", "e.g. FS123"),
            ("Departure", "e.g. New York"),
            ("Destination", "e.g. London"),
            ("Date", "Pick a date"),
            ("Seat Number", "e.g. 12A")
        ]
        for label, ph in placeholders:
            entry = self.entries[label]
            entry.insert(0, ph)
            entry.config(fg="gray")
