import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your current balance is: ₹{self.balance}")

    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount > 0:
                self.balance += amount
                messagebox.showinfo("Success", f"₹{amount} deposited successfully.")
            else:
                messagebox.showerror("Error", "Invalid deposit amount.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a numeric value.")

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if 0 < amount <= self.balance:
                self.balance -= amount
                messagebox.showinfo("Success", f"₹{amount} withdrawn successfully.")
            elif amount > self.balance:
                messagebox.showerror("Error", "Insufficient balance.")
            else:
                messagebox.showerror("Error", "Invalid withdrawal amount.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a numeric value.")

class ATMGUI:
    def __init__(self, root):
        self.atm = ATM(balance=5000)
        self.root = root
        self.root.title("ATM Machine")
        self.root.geometry("300x250")
        
        tk.Label(root, text="ATM Machine", font=("Arial", 16)).pack(pady=10)
        tk.Button(root, text="Check Balance", command=self.atm.check_balance).pack(pady=5)
        tk.Button(root, text="Deposit Money", command=self.deposit_window).pack(pady=5)
        tk.Button(root, text="Withdraw Money", command=self.withdraw_window).pack(pady=5)
        tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

    def deposit_window(self):
        self.transaction_window("Deposit Money", self.atm.deposit)
    
    def withdraw_window(self):
        self.transaction_window("Withdraw Money", self.atm.withdraw)

    def transaction_window(self, title, action):
        window = tk.Toplevel(self.root)
        window.title(title)
        window.geometry("250x150")
        tk.Label(window, text="Enter Amount:").pack(pady=5)
        amount_entry = tk.Entry(window)
        amount_entry.pack(pady=5)
        tk.Button(window, text="Submit", command=lambda: action(amount_entry.get())).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = ATMGUI(root)
    root.mainloop()
