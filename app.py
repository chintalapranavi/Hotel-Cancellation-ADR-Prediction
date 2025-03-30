from tkinter import filedialog, messagebox
import numpy as np
import pandas as pd
import joblib
import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

MODEL_PATH = "C:/Users/Sainath/Desktop/dic_bonus.pkl"
model = joblib.load(MODEL_PATH)

uploaded_data = None

# Function to upload dataset and display plot
def upload_dataset():
    file_path = filedialog.askopenfilename(
        filetypes=[("CSV and Excel files", "*.csv;*.xlsx;*.xls"), ("All files", "*.*")]
    )
    if file_path:
        try:
            # Determine file type and read accordingly
            if file_path.endswith(('.xlsx', '.xls')):
                data = pd.read_excel(file_path)
            elif file_path.endswith('.csv'):
                data = pd.read_csv(file_path)
            else:
                raise ValueError("Unsupported file format")

            # Display the dataset's first few rows
            display_dataset(data)

            # Plot the graph
            plot_graph(data)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load dataset: {str(e)}")

# Function to make predictions using the trained model
def predict_cancellation():
    try:
        lead_time = float(entry_lead_time.get())
        adults = int(entry_adults.get())
        children = float(entry_children.get())
        stays_in_week_nights = int(entry_week_nights.get())
        stays_in_weekend_nights = int(entry_weekend_nights.get())
        total_of_special_requests = int(entry_special_requests.get())
        adr = float(entry_adr.get())

        # Mock prediction logic
        prediction = "Customer is likely to Cancel the booking" if lead_time > 200 else "Customer is not likely to cancel the booking"
        result_label.config(text=f"Prediction: {prediction}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Function to clear inputs
def clear_inputs():
    entry_lead_time.delete(0, tk.END)
    entry_adults.delete(0, tk.END)
    entry_children.delete(0, tk.END)
    entry_week_nights.delete(0, tk.END)
    entry_weekend_nights.delete(0, tk.END)
    entry_special_requests.delete(0, tk.END)
    entry_adr.delete(0, tk.END)
    result_label.config(text="Prediction: ")

# Function to display the dataset in a table
def display_dataset(data):
    for widget in dataset_frame.winfo_children():
        widget.destroy()

    tree = ttk.Treeview(dataset_frame, columns=list(data.columns), show="headings")
    tree.pack(expand=True, fill="both")

    # Configure tree columns
    for col in data.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=120)

    # Insert rows into tree
    for _, row in data.iterrows():
        tree.insert("", "end", values=list(row))

    # Add scrollbars
    vsb = ttk.Scrollbar(dataset_frame, orient="vertical", command=tree.yview)
    vsb.pack(side="right", fill="y")
    tree.configure(yscrollcommand=vsb.set)

# Function to plot a graph for the dataset
def plot_graph(data):
    for widget in plot_frame.winfo_children():
        widget.destroy()

    # Select the first two numeric columns for a scatter plot
    numeric_cols = data.select_dtypes(include=["number"]).columns
    if len(numeric_cols) < 2:
        messagebox.showerror("Error", "Dataset must have at least two numeric columns for plotting.")
        return

    x_col, y_col = numeric_cols[0], numeric_cols[1]

    # Create the figure and plot
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(data[x_col], data[y_col], alpha=0.6)
    ax.set_title(f"{x_col} vs {y_col}")
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)

    # Display the plot in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


# Create the GUI application window
app = tk.Tk()
app.title("Hotel Booking Cancellation Predictor")
app.geometry("900x600")

# Create a notebook for tabbed UI
notebook = ttk.Notebook(app)
notebook.pack(fill="both", expand=True)

# Upload Dataset Tab
upload_tab = ttk.Frame(notebook)
notebook.add(upload_tab, text="Upload Dataset")

# Prediction Tab
predict_tab = ttk.Frame(notebook)
notebook.add(predict_tab, text="Prediction")

# Upload Tab Content
upload_button = ttk.Button(upload_tab, text="Upload Dataset", command=upload_dataset)
upload_button.pack(pady=10)

dataset_frame = ttk.Frame(upload_tab)
dataset_frame.pack(fill="both", expand=True)

plot_frame = ttk.Frame(upload_tab)
plot_frame.pack(fill="both", expand=True)

# Prediction Tab Content
predict_frame = ttk.Frame(predict_tab, padding=10)
predict_frame.pack(fill="both", expand=True)

tk.Label(predict_frame, text="Prediction", font=("Helvetica", 16)).pack(pady=10)

input_frame = ttk.Frame(predict_frame, padding=10)
input_frame.pack()

# Input fields for features
tk.Label(input_frame, text="Lead Time:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_lead_time = ttk.Entry(input_frame)
entry_lead_time.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Adults:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_adults = ttk.Entry(input_frame)
entry_adults.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Children:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_children = ttk.Entry(input_frame)
entry_children.grid(row=2, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Stays in Week Nights:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_week_nights = ttk.Entry(input_frame)
entry_week_nights.grid(row=3, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Stays in Weekend Nights:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
entry_weekend_nights = ttk.Entry(input_frame)
entry_weekend_nights.grid(row=4, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Special Requests:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
entry_special_requests = ttk.Entry(input_frame)
entry_special_requests.grid(row=5, column=1, padx=5, pady=5)

tk.Label(input_frame, text="ADR:").grid(row=6, column=0, padx=5, pady=5, sticky="e")
entry_adr = ttk.Entry(input_frame)
entry_adr.grid(row=6, column=1, padx=5, pady=5)

# Predict and Clear Buttons
button_frame = ttk.Frame(predict_frame)
button_frame.pack(pady=20)

predict_button = ttk.Button(button_frame, text="Predict", command=predict_cancellation)
predict_button.grid(row=0, column=0, padx=10)

clear_button = ttk.Button(button_frame, text="Clear", command=clear_inputs)
clear_button.grid(row=0, column=1, padx=10)

# Prediction Result Label
result_label = tk.Label(predict_frame, text="Prediction: ", font=("Helvetica", 14))
result_label.pack(pady=10)

# Run the application
app.mainloop()
