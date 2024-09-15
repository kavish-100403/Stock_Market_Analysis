import data_generation as dg
import decision_tree_regression as dtr
import multiple_linear_regression as mlr
import polynomial_regression as pr
import random_forest_regression as rfr
import support_vector_regression as svr
from tkcalendar import DateEntry


import tkinter as tk
from tkinter import ttk

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to Stock Market Analysis", font=("Arial",18))
        label.pack(pady=10, padx=10)
        button = ttk.Button(self, text="Continue to Program",
                            command=lambda: controller.show_frame(PageTwo))
        button.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Selectin the Stock name Label
        label = tk.Label(self, text="Select the Stock Name: ", font=("Arial",14))
        label.pack(pady=10, padx=10)
        label.place(x=0, y=0)
        # Creating a Dropdown menu to select a stock for regression
        stock_options=["AAPL","FBB"]
        stock_names = ttk.Combobox(self,values=stock_options,state="readonly")
        stock_names.set("Choose...")
        stock_names.pack(pady=10)
        def get_selected_option(event):
            selected_stock_name = stock_names.get()
            print(f"Selected: {selected_stock_name}")
        # Bind an event when an item is selected from the dropdown
        stock_names.bind("<<ComboboxSelected>>", get_selected_option)
        stock_names.place(x=220,y=5)

        #Start Date Label     
        label = tk.Label(self, text="Select the Start Date of the Stock: ", font=("Arial",10))
        label.pack(pady=10, padx=10)
        label.place(x=0, y=100)

        # Start Date Button
        start_date_entry = DateEntry(self, width=12, background='black', foreground='white', borderwidth=2, date_pattern='dd-mm-yyyy')
        start_date_entry.pack(pady=10)
        start_date_entry.place(x=50,y=120)

        # End Date Label
        label = tk.Label(self, text="Select the End Date of the Stock: ", font=("Arial",10))
        label.pack(pady=10, padx=10)
        label.place(x=300, y=100)

        # End Date Button
        end_date_entry = DateEntry(self, width=12, background='black', foreground='white', borderwidth=2, date_pattern='dd-mm-yyyy')
        end_date_entry.pack(pady=10)
        end_date_entry.place(x=350,y=120)
        
        # Button to go to next page after confirmation
        button = ttk.Button(self, text="Confirm",
                            command=lambda: controller.show_frame(PageThree))
        button.pack()
        button.place(x=220, y=200)

class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Training the data...", font=("Arial",10))
        label.pack(pady=10, padx=10)
        label.place(x=0, y=0)

        # TO add a progress bar when the data is being trained from the training set
        # After training the later part needs to be displayed
        label = tk.Label(self, text="Training Completed!!!...click the button to view the results: ", font=("Arial",10))
        label.pack(pady=10, padx=10)
        label.place(x=0, y=170)

        # Button that takes to the result page
        button = ttk.Button(self, text="Results",
                            command=lambda: controller.show_frame(PageFour))
        button.pack()
        button.place(x=400, y=200)

class PageFour(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (PageOne, PageTwo, PageThree, PageFour):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(PageOne)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        if cont == PageOne:
            self.geometry("400x200")  # Set window size for Page 1
        elif cont == PageTwo:
            self.geometry("525x230")  # Set window size for Page 2
        elif cont == PageThree:
            self.geometry("525x230")  # Set window size for Page 2
        elif cont == PageFour:
            self.geometry("525x230")  # Set window size for Page 2

if __name__ == "__main__":
    app = App()
    app.mainloop()
    


 