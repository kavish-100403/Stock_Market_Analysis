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

csv_filename=None
# Evaluating the best performance of open market from all the models
def eval_open_model():
    open_models=[lambda:odtr(csv_filename), lambda: omlr(csv_filename), lambda: opr(csv_filename), lambda: orfr(csv_filename), lambda: osvr(csv_filename)]
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
    # print(f"\nBest Open Model: {best_open_model_name}, RMS: {best_open_rms}")
    return best_open_model_name, best_open_rms


def eval_close_model():
    close_models=[lambda:cdtr(csv_filename), lambda: cmlr(csv_filename), lambda: cpr(csv_filename), lambda: crfr(csv_filename), lambda: csvr(csv_filename)]
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
    # print(f"\nBest close Model: {best_close_model_name}, RMS: {best_close_rms}")
    return best_close_model_name, best_close_rms

# Generating CSV File from the input of the user
def generate_csv_and_evaluate(ticker, start_date, end_date, controller):
    global csv_filename
    data_generation.dataGeneration(ticker, start_date, end_date)
    csv_filename = f"{ticker}_stock_data.csv"
    controller.show_frame(PageFour)


                                    #Start of the Tkinter



from tkcalendar import DateEntry
import tkinter as tk
from tkinter import ttk
import os

# Page 1.. basic name of the Project 
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to Stock Market Analysis", font=("Arial",18))
        label.pack(pady=10, padx=10)
        button = ttk.Button(self, text="Continue to Program",
                            command=lambda: controller.show_frame(PageTwo))
        button.pack()


# Page 2 will have the stock selection and Start date and End Date, so User can select according to their preference
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
                                            generate_csv_and_evaluate(
                                                selected_stock_name_var.get(),
                                                selected_start_date_var.get(),
                                                selected_end_date_var.get(),
                                                controller)
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

# Page 4 will display the best accuracy of all the stock and will display the graph of the best stock and also the accuracy and graph of other stocks
class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

# Label & Text widget to display the best model for open price name 
        label = tk.Label(self, text="The best accuracy for \n opening price was obtained by: ", font=("Arial", 10))
        label.pack(pady=10, padx=10)
        label.place(x=0, y=0)
        self.best_open_accuracy_name = tk.Text(self, height=1.5, width=20, font=("Arial", 12))
        self.best_open_accuracy_name.place(x=5, y=40)
        # Adding a placeholder before the actual data is inserted
        self.best_open_accuracy_name.insert(1.0, "Evaluating...")

# Label & Text widget to display the best model for open price accuracy
        label = tk.Label(self, text="Accuracy %:", font=("Arial", 10))
        label.pack(pady=10, padx=10)
        label.place(x=0, y=100)
        self.best_open_accuracy_rms = tk.Text(self, height=1.5, width=20, font=("Arial", 12))
        self.best_open_accuracy_rms.place(x=5, y=125)
        # Adding a placeholder before the actual data is inserted
        self.best_open_accuracy_rms.insert(1.0, "Evaluating...")

# Label & Text widget to display the best model for Close price name
        label = tk.Label(self, text="The best accuracy for \n closing price was obtained by: ", font=("Arial", 10))
        label.pack(pady=10, padx=10)
        label.place(x=280, y=0)
        self.best_close_accuracy_name = tk.Text(self, height=1.5, width=20, font=("Arial", 12))
        self.best_close_accuracy_name.place(x=288, y=40)
        # Adding a placeholder before the actual data is inserted
        self.best_close_accuracy_name.insert(1.0, "Evaluating...")

# Label & Text widget to display the best model for close price accuracy
        label = tk.Label(self, text="Accuracy %:", font=("Arial", 10))
        label.pack(pady=10, padx=10)
        label.place(x=280, y=100)
        self.best_close_accuracy_rms = tk.Text(self, height=1.5, width=20, font=("Arial", 12))
        self.best_close_accuracy_rms.place(x=288, y=125)
        # Adding a placeholder before the actual data is inserted
        self.best_close_accuracy_rms.insert(1.0, "Evaluating...")

#Start Button for the Model Evaluation [Might use later]
        # button = ttk.Button(self, text="Confirm",
        #                     command=lambda:[controller.show_frame(PageFour),
        #                                     self.on_show_frame()
        #                                     ])
        # button.pack()
        # button.place(x=400, y=200)


# To be done: Run the model after opening the fourth frame, as of now it is running before
    def on_show_frame(self):
        # This method will be called every time the frame is raised or shown

        # Running the model evaluations when the frame is displayed
        best_open_model_name, best_open_rms = eval_open_model()
        best_close_model_name, best_close_rms = eval_close_model()

        # Inserting the best open model name into the Text widget
        self.best_open_accuracy_name.delete(1.0, tk.END)
        self.best_open_accuracy_name.insert(1.0, best_open_model_name)

        # Inserting the best open model accuracy into the Text widget
        self.best_open_accuracy_rms.delete(1.0, tk.END)
        self.best_open_accuracy_rms.insert(1.0, best_open_rms)

        # Inserting the best close model name into the Text widget
        self.best_close_accuracy_name.delete(1.0, tk.END)
        self.best_close_accuracy_name.insert(1.0, best_close_model_name)

        # Inserting the best close model accuracy into the Text widget
        self.best_close_accuracy_rms.delete(1.0, tk.END)
        self.best_close_accuracy_rms.insert(1.0, best_close_rms)

        # Here will be the button which will show the graph of the best model whose x-axis will be date and y-axis will be the opening or closing price

        # Here will be the button which will show the graph of the other models whose x-axis will be date and y-axis will be the opening or closing price

def on_closing():
    global csv_filename
    if csv_filename and os.path.exists(csv_filename):
        os.remove(csv_filename)  # Delete the CSV file
        print(f"CSV file '{csv_filename}' deleted!")
    app.destroy()

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Set the title of the main tkinter window
        self.title("Stock Market Analysis")

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
            self.geometry("525x230")  # Set window size for Page 3
        elif cont == PageFour:
            self.geometry("525x230")  # Set window size for Page 4
            # This is used to start the evaluation of models after displaying fourth frames
            frame.on_show_frame()

if __name__ == "__main__":
    app = App()
    app.protocol("WM_DELETE_WINDOW", on_closing) 
    app.mainloop()                                                                                                                                                                                                                                                                                                                                                                                          
    


 