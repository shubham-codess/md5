import hashlib
import csv
from tkinter import Tk, filedialog

# Create a Tkinter root window
root = Tk()
root.withdraw()

# Ask the user to select a CSV file
file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

# Open the CSV file
with open(file_path, 'r') as file:
    reader = csv.reader(file)

    # Loop over each row in the CSV file
    for row in reader:
        # Get the string from the first column of the row
        string = row[0]

        # Encode the string into bytes
        encoded_string = string.encode()

        # Generate the MD5 hash value
        hash_value = hashlib.md5(encoded_string).hexdigest()

        # Print the hash value
        print("MD5 hash value for", string, ":", hash_value)

