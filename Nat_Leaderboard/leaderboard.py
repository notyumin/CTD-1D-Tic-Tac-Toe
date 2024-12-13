import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import csv
# SCENE 1: MAIN MENU
# data creation, save as a csv file here during data entry
root = tk.Tk()
"""root.config(background = "light gray")"""
frame1 = tk.Frame(root, bg="lightblue")
label1 = tk.Label(frame1, text="Tic Tac Toe")
label1.pack(pady=20)
button1 = tk.Button(frame1, text="Leaderboard",
                    command=lambda: switch_frame(frame2))
button1.pack()


def switch_frame(frame_to_show):
    frame1.pack_forget()
    frame2.pack_forget()
    frame_to_show.pack(fill="both", expand=True)


# this is the saving data logic using CSV
# data to be stored in csv in form of list of list. 3 examples given.
data = [
    ['Name', 'Class', 'Difficulty', 'Score'],
    ['Yu Min', 'SC01', 'Hard', 9],
    ['Jerrick', 'SC09', 'Medium', 8],
    ['Nat', 'SC03', 'Easy', 8]
]

# file path of csv to be stored
# problem is csv file is stored locally
csv_file_path = 'highscore.csv'

# opening file in write mode using a context manager
with open(csv_file_path, mode='w') as file:
    for row in data:
        file.write(','.join(map(str, row)) + '\n')  # writing data row by row

print(f"CSV file '{csv_file_path}' created successfully!!!")


# SCENE 2: GAME
# this is the scoring logic to be put inside the playing game code
# since in the main menu, easy/ medium/ hard is a text choice, how can we save this value to pass into
# updating the high score or even set difficulty of AI?
def resultpoints(result):
    # assigns win/lose condition to this arbitrary value (1/0) for points calculation
    if result == "Win":
        resultpoints = 1
    elif result == "Lose":
        resultpoints = 0
    else:
        resultpoints = None
    return int(resultpoints)


def read_csv(file_path):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)


def write_csv(file_path, data):
    with open(file_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "date", "value"])
        writer.writeheader()
        writer.writerows(data)

# Function to update the value


def update_value(result, name):
    data = read_csv(csv_file_path)

    for row in data:
        if row["name"] == name:
            new_value = int(int(row["value"]) + resultpoints(result)*50)
            row["value"] = str(new_value)
            write_csv(csv_file_path, data)
            messagebox.showinfo(
                "Success", f"Value for {name} updated to {new_value}!")
            return
    messagebox.showerror(
        "Error", f"No entry found for {name}.")  # else condition


# Button
update_button = tk.Button(root, text="Update Value", command=update_value)
update_button.pack(pady=20)

# SCENE 3: LEADERBOARD
# this is the display logic for leaderboards on the main menu, to be integratable

# GUI setup
frame2 = tk.Frame(root, bg="light blue")
frame2.pack(fill="both", expand=True)
label2 = tk.Label(frame2, text="Leaderboards")
label2.pack(pady=20)
button2 = tk.Button(frame2, text="Back", command=lambda: switch_frame(frame1))
button2.pack()

# write sorting function


def sort_csv(file_path, column_to_sort):
    # Read the CSV and sort it
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        rows = list(reader)  # Convert reader to a list of rows
        # Sort rows by the desired column
        rows.sort(key=lambda row: float(row[column_to_sort]))
    # Write back the sorted rows to the same file
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
        writer.writeheader()  # Write the header
        writer.writerows(rows)  # Write the sorted rows

# sort and display leaderboard


def load_csv_to_treeview(tree, csv_file_path, selected_columns):
    for row in tree.get_children():
        tree.delete(row)
    with open(csv_file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        # Filter only the selected columns
        tree["columns"] = selected_columns
        tree["show"] = "headings"  # Hide default empty column
        for col in selected_columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor="center")
        # Insert rows with selected columns into Treeview
        for row in reader:
            filtered_row = [row[col] for col in selected_columns if col in row]
            tree.insert("", "end", values=filtered_row)


# Sort the CSV
sort_csv(csv_file_path, 'Score')

# Create a scrollable Treeview
tree = ttk.Treeview(frame2)
tree.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(frame2, orient="vertical", command=tree.yview)
scrollbar.pack(side="right", fill="y")
tree.configure(yscrollcommand=scrollbar.set)

# Load CSV data into Treeview
selected_columns = ["Name", "Score"]
load_csv_to_treeview(tree, csv_file_path, selected_columns)
root.mainloop()
