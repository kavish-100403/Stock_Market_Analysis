import data_generation
from decision_tree_regression import opens_decision_tree_regression as odtr
from decision_tree_regression import close_decision_tree_regression as cdtr
from multiple_linear_regression import open_multiple_linear_regression as omlr
from multiple_linear_regression import close_multiple_linear_regression as cmlr
from polynomial_regression import open_polynomial_regression as opr
from polynomial_regression import close_polynomial_regression as cpr
from random_forest_regression import open_random_forest_regression as orfr
from random_forest_regression import close_random_forest_regression as crfr
from support_vector_regression import open_support_vector_regression as osvr
from support_vector_regression import close_support_vector_regression as csvr

# Evaluating the best performance of open market from all the models
def eval_open_model():
    open_models=[odtr, omlr, opr, orfr, osvr]
    best_open_model=None
    best_open_rms = float('inf')
    best_open_model_name=""

    for model in open_models:
        rms, model_name = model()
        # print(f"Model: {model_name}, RMS: {rms}")
        
        # Check if this model is the best performing one
        if rms < best_open_rms:
            best_open_rms = rms
            best_open_model = model
            best_open_model_name = model_name

    # Print the best model's performance
    print(f"\nBest Open Model: {best_open_model_name}, RMS: {best_open_rms}")


def eval_close_model():
    close_models=[cdtr, cmlr, cpr, crfr, csvr]
    best_close_model=None
    best_close_rms = float('inf')
    best_close_model_name=""

    for model in close_models:
        rms, model_name = model()
        # print(f"Model: {model_name}, RMS: {rms}")
        
        # Check if this model is the best performing one
        if rms < best_close_rms:
            best_close_rms = rms
            best_close_model = model
            best_close_model_name = model_name

    # Print the best model's performance
    print(f"\nBest close Model: {best_close_model_name}, RMS: {best_close_rms}")



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
        selected_stock_name_var = tk.StringVar()
        stock_options=["AAPL", "GOOGL", "AMZN", "MSFT", "TSLA"]
        stock_names = ttk.Combobox(self, values=stock_options, textvariable=selected_stock_name_var, state="readonly")
        stock_names.pack(pady=10)
        stock_names.set("Choose...")
        def get_selected_option(event):
            selected_stock_name = selected_stock_name_var.get()  # Access the selected stock
            print(f"Selected: {selected_stock_name}")
        # Bind an event when an item is selected from the dropdown
        stock_names.bind("<<ComboboxSelected>>", get_selected_option)
        stock_names.place(x=220,y=5)

        # Element to store the Start and End Date
        selected_start_date_var = tk.StringVar()
        selected_end_date_var = tk.StringVar()

        #Start Date Label     
        label = tk.Label(self, text="Select the Start Date of the Stock: ", font=("Arial",10))
        label.pack(pady=10, padx=10)
        label.place(x=0, y=100)

        # Start Date Button
        start_date_entry = DateEntry(self, width=12, background='black', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
        start_date_entry.pack(pady=10)
        start_date_entry.place(x=50,y=120)

        # End Date Label
        label = tk.Label(self, text="Select the End Date of the Stock: ", font=("Arial",10))
        label.pack(pady=10, padx=10)
        label.place(x=300, y=100)

        # End Date Button
        end_date_entry = DateEntry(self, width=12, background='black', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
        end_date_entry.pack(pady=10)
        end_date_entry.place(x=350,y=120)
        
        # Binding the Start and End Date Button
        def update_date_var():
            selected_start_date_var.set(start_date_entry.get())  # Set the variable to the selected date
            selected_end_date_var.set(end_date_entry.get())  # Set the variable to the selected date
            print(f"Date Selected: {selected_start_date_var.get()}")
            print(f"Date Selected: {selected_end_date_var.get()}")
        
        # Button to go to next page after confirmation
        button = ttk.Button(self, text="Confirm",
                            command=lambda:[
                                            update_date_var(), 
                                            data_generation.dataGeneration(ticker=selected_stock_name_var.get(), start_date=selected_start_date_var.get(),end_date=selected_end_date_var.get()),
                                            eval_open_model,
                                            eval_close_model,
                                            controller.show_frame(PageFour)
                                            ])
        button.pack()
        button.place(x=220, y=200)
        

# The Selected Stock Name, Start Date and End Date will be inserted into the data_generation file to create a CSV of that stock

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


        label = tk.Label(self, text="The best accuracy for \n opening price was obtained by: ", font=("Arial",10))
        label.pack(pady=10, padx=10)
        label.place(x=0, y=0)

        # Here will be the name of the model which showed best accuracy

        # This is show the label of the Accuracy of the best model
        label = tk.Label(self, text="Accuracy %: ", font=("Arial",10))
        label.pack(pady=10, padx=10)
        label.place(x=0, y=100)

        # Here will be the text box which will show the accuracy of the model which performed the best

        # Here will be the button which will show the graph of the best model whose x-axis will be date and y-axis will be the opening or closing price

        # Here will be the button which will show the graph of the other models whose x-axis will be date and y-axis will be the opening or closing price


        label = tk.Label(self, text="The best accuracy for \n closing price was obtained by: ", font=("Arial",10))
        label.pack(pady=10, padx=10)
        label.place(x=220, y=0)
        # Here will b the name of the model which showed best accuracy

        # This is show the label of the Accuracy of the best model
        label = tk.Label(self, text="Accuracy %: ", font=("Arial",10))
        label.pack(pady=10, padx=10)
        label.place(x=220, y=100)

        # Here will be the text bix which will show the accuracy of the model which performed the best

        # Here will be the button which will show the graph of the best model whose x-axis will be date and y-axis will be the opening or closing price

        # Here will be the button which will show the graph of the other models whose x-axis will be date and y-axis will be the opening or closing price



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
    


 