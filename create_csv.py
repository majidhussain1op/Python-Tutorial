import pandas as pd
import os

# Ensure openpyxl is installed for Excel writing
try:
    import openpyxl
except ImportError:
    print("Installing openpyxl...")
    os.system("pip install openpyxl")

# Ask user if they want to use an existing file or create a new one
file_choice = input("Do you want to update an existing file or create a new one? (existing/new): ").strip().lower()

if file_choice == "new":
    filename = input("Enter the new filename (without extension): ").strip()
    excel_filename = f"{filename}.xlsx"
    csv_filename = f"{filename}.csv"
    existing_data = pd.DataFrame(columns=["Name", "Age", "City"])  # Start with an empty DataFrame
else:
    excel_filename = "output.xlsx"
    csv_filename = "output.csv"

    # Check if the existing file exists
    if os.path.exists(csv_filename):
        try:
            existing_data = pd.read_csv(csv_filename)
        except pd.errors.EmptyDataError:
            existing_data = pd.DataFrame(columns=["Name", "Age", "City"])
    else:
        print("No existing file found. Creating a new file.")
        existing_data = pd.DataFrame(columns=["Name", "Age", "City"])

# Initialize new data dictionary
new_data = {"Name": [], "Age": [], "City": []}

while True:
    # Get user input for one entry
    name = input("Enter name: ")
    age = int(input(f"Enter age for {name}: "))
    city = input(f"Enter city for {name}: ")

    # Append new data
    new_data["Name"].append(name)
    new_data["Age"].append(age)
    new_data["City"].append(city)

    # Ask the user if they want to enter another entry
    choice = input("Do you want to enter another user? (yes/no): ").strip().lower()
    
    if choice == "no":
        break
    elif choice != "yes":
        print("Invalid choice! Assuming 'no'.")
        break

# Convert new data to DataFrame
new_df = pd.DataFrame(new_data)

# Combine old and new data
final_df = pd.concat([existing_data, new_df], ignore_index=True)

# Save updated data to Excel
try:
    final_df.to_excel(excel_filename, index=False, engine="openpyxl")
except Exception as e:
    print(f"Error saving to Excel: {e}")

# Save updated data to CSV
try:
    final_df.to_csv(csv_filename, index=False)
except Exception as e:
    print(f"Error saving to CSV: {e}")

print(f"New data has been added! Files '{excel_filename}' and '{csv_filename}' are updated successfully!")

# Automatically open the files
if os.name == "nt":  # Windows
    os.system(f'start excel "{excel_filename}"')
    os.system(f'start notepad "{csv_filename}"')  # Opens CSV in Notepad
elif os.name == "posix":  # Mac/Linux
    os.system(f'open "{excel_filename}"')  # Mac
    os.system(f'open "{csv_filename}"')  # Mac
    # os.system(f'xdg-open "{csv_filename}"')  # Linux alternative
