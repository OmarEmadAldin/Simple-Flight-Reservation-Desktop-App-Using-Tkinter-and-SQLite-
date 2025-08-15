import tkinter as tk
from tkinter import messagebox
import database

class EditReservationPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f8f9fa")
        self.controller = controller
        self.entries = {}

        tk.Label(self, text="Edit Reservation", font=("Arial", 20, "bold"),
                 bg="#f8f9fa", fg="#005b96").pack(pady=20)

        form_frame = tk.Frame(self, bg="#f8f9fa")
        form_frame.pack(pady=10)

        fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
        for i, field in enumerate(fields):
            tk.Label(form_frame, text=field + ":", bg="#f8f9fa", font=("Arial", 12)).grid(row=i, column=0, sticky="e", pady=5, padx=10)
            entry = tk.Entry(form_frame, width=30)
            entry.grid(row=i, column=1, pady=5)
            self.entries[field] = entry

        tk.Button(self, text="Update", bg="#007bbf", fg="white", width=15,
                  command=self.update_reservation).pack(pady=10)

        from reservations import ViewReservationsPage
        tk.Button(self, text="Back", width=15,
                  command=lambda: controller.show_frame(ViewReservationsPage)).pack()

    def tkraise(self, aboveThis=None):
        super().tkraise(aboveThis)
        res_id = self.controller.selected_reservation_id
        if res_id:
            for r in database.get_reservations():
                if r[0] == res_id:
                    values = r[1:]  # skip ID
                    for (field, entry), val in zip(self.entries.items(), values):
                        entry.delete(0, tk.END)
                        entry.insert(0, val)

    def update_reservation(self):
        res_id = self.controller.selected_reservation_id
        updated_data = {field: entry.get() for field, entry in self.entries.items()}
        if any(v.strip() == "" for v in updated_data.values()):
            messagebox.showerror("Error", "All fields are required.")
            return
        database.update_reservation(res_id, updated_data["Name"], updated_data["Flight Number"],
                                    updated_data["Departure"], updated_data["Destination"],
                                    updated_data["Date"], updated_data["Seat Number"])
        messagebox.showinfo("Success", "Reservation updated successfully")

        from reservations import ViewReservationsPage
        self.controller.show_frame(ViewReservationsPage)
