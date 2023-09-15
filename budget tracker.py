import tkinter as tk
from tkinter import messagebox

# initialize the budget dictionar
budget ={
    "Income":0,
    "Expenses":0,
    "balance":0

}
# function to update the balance
def update_balance():
    income=float(income_entry.get())

    expenses =float (expenses_entry.get())

    budget["Income"]=income
    budget["Expenses"]=expenses
    budget["balance"]=income-expenses
    balance_label.config(text=f"Balance: ${budget['Balance']:.2f}")

    # create a main window
    root=tk.Tk
    root.title("Personal Budget Tracker")

    # create labels and entry widgets for income and expenses 
    income_label=tk.Label(root,text="Income:",width=30,bg='pink')
    income_label.pack()
    income_entry =tk.Entry(root)
    income_entry.pack()
     
    expenses_label =tk.Label(root,text="Expenses:",width=30,bg='skyblue')
    expenses_label.pack()
    expenses_entry =tk.Entry(root)
    expenses_entry.pack()

    # create a button to update the balance 
    update_button =tk.Button(root,text="update balance ",command =update_balance,width =30,bg='orange')
    update_button.pack()
     

     # create a label to display the balance 
    balance_label= tk.Label(root,text="Balance :$0.00")
    balance_label.pack()
     
     # run the mainloop
    root.mainloop()