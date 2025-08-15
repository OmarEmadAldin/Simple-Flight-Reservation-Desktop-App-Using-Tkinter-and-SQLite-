import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f8f9fa")
        self.controller = controller

        from booking import BookFlightPage
        from reservations import ViewReservationsPage

        tk.Label(self, text="Welcome to OBE Sky Reservations",
                 font=("Arial", 22, "bold"), bg="#f8f9fa", fg="#005b96").pack(pady=20)

        cards_frame = tk.Frame(self, bg="#f8f9fa")
        cards_frame.pack(pady=40)

        # Card 1: Book a Flight
        card1 = tk.Frame(cards_frame, bg="white", bd=1, relief="solid")
        card1.grid(row=0, column=0, padx=20, ipadx=20, ipady=20)

        tk.Label(card1, text="✈", font=("Arial", 30), bg="white", fg="#007bbf").pack(pady=10)
        tk.Label(card1, text="Book a Flight", font=("Arial", 16, "bold"), bg="white").pack(pady=5)
        tk.Label(card1, text="Reserve your next flight by providing your details\nand flight information.",
                 font=("Arial", 11), bg="white", fg="gray").pack(pady=5)
        tk.Button(card1, text="Book Flight", bg="#007bbf", fg="white",
                  font=("Arial", 12, "bold"), width=20, height=2,
                  command=lambda: controller.show_frame(BookFlightPage)).pack(pady=10)

        # Card 2: View Reservations
        card2 = tk.Frame(cards_frame, bg="white", bd=1, relief="solid")
        card2.grid(row=0, column=1, padx=20, ipadx=20, ipady=20)

        tk.Label(card2, text="☰", font=("Arial", 30), bg="white", fg="#007bbf").pack(pady=10)
        tk.Label(card2, text="View Reservations", font=("Arial", 16, "bold"), bg="white").pack(pady=5)
        tk.Label(card2, text="Manage your existing reservations, view details,\nedit or cancel if needed.",
                 font=("Arial", 11), bg="white", fg="gray").pack(pady=5)
        tk.Button(card2, text="View Reservations", bg="#007bbf", fg="white",
                  font=("Arial", 12, "bold"), width=20, height=2,
                  command=lambda: controller.show_frame(ViewReservationsPage)).pack(pady=10)
