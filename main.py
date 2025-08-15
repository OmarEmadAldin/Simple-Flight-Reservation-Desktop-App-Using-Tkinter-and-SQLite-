import tkinter as tk
from home import HomePage
from booking import BookFlightPage
from reservations import ViewReservationsPage
from edit_reservation import EditReservationPage
import database

class FlySkyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("OBE Sky Reservations")
        self.geometry("900x600")
        self.configure(bg="#f8f9fa")
        self.resizable(False, False)

        # Create DB table if not exists
        database.create_table()

        self.selected_reservation_id = None  # For editing

        # Navigation bar
        nav_frame = tk.Frame(self, bg="#007bbf", height=50)
        nav_frame.pack(side="top", fill="x")

        tk.Label(nav_frame, text="✈ OBE Sky Reservations", bg="#007bbf", fg="white",
                 font=("Arial", 14, "bold")).pack(side="left", padx=20)

        tk.Button(nav_frame, text="Home", bg="#007bbf", fg="white", bd=0,
                  font=("Arial", 12), command=lambda: self.show_frame(HomePage)).pack(side="right", padx=10)
        tk.Button(nav_frame, text="View Reservations", bg="#007bbf", fg="white", bd=0,
                  font=("Arial", 12), command=lambda: self.show_frame(ViewReservationsPage)).pack(side="right", padx=10)
        tk.Button(nav_frame, text="Book Flight", bg="#007bbf", fg="white", bd=0,
                  font=("Arial", 12), command=lambda: self.show_frame(BookFlightPage)).pack(side="right", padx=10)

        # Page container
        container = tk.Frame(self, bg="#f8f9fa")
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, BookFlightPage, ViewReservationsPage, EditReservationPage):
            frame = F(parent=container, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()

if __name__ == "__main__":
    app = FlySkyApp()
    app.mainloop()
