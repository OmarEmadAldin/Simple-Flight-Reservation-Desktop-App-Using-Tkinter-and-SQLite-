import tkinter as tk
from tkinter import ttk, messagebox
import database

class ViewReservationsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f8f9fa")
        self.controller = controller

        tk.Label(self, text="Your Reservations", font=("Arial", 20, "bold"),
                 bg="#f8f9fa", fg="#005b96").pack(pady=20)

        self.tree = ttk.Treeview(
            self,
            columns=("ID", "Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"),
            show="headings",
            height=10
        )
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack(pady=10)

        btn_frame = tk.Frame(self, bg="#f8f9fa")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Edit", bg="#007bbf", fg="white", width=15,
                  command=self.edit_reservation).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Delete", bg="red", fg="white", width=15,
                  command=self.delete_reservation).grid(row=0, column=1, padx=10)

        from home import HomePage
        tk.Button(btn_frame, text="Back", width=15,
                  command=lambda: controller.show_frame(HomePage)).grid(row=0, column=2, padx=10)

    def edit_reservation(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a reservation to edit.")
            return
        item = self.tree.item(selected[0])
        self.controller.selected_reservation_id = item["values"][0]

        from edit_reservation import EditReservationPage
        self.controller.show_frame(EditReservationPage)

    def delete_reservation(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a reservation to delete.")
            return
        res_id = self.tree.item(selected[0])["values"][0]
        database.delete_reservation(res_id)
        self.refresh_table()

    def refresh_table(self):
        self.tree.delete(*self.tree.get_children())
        for res in database.get_reservations():
            self.tree.insert("", tk.END, values=res)

    def tkraise(self, aboveThis=None):
        super().tkraise(aboveThis)
        self.refresh_table()
