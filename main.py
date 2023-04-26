import os
import shutil
import tkinter as tk
from tkinter import filedialog

# Define the GUI interface
class FileOrganizerGUI:
    def __init__(self, master):
        self.master = master
        master.title("File Organizer")
        
        # Create the source directory button
        self.source_button = tk.Button(master, text="Select Source Directory", command=self.choose_source_directory)
        self.source_button.pack(padx=10, pady=10)
        
        # Create the destination directory button
        self.destination_button = tk.Button(master, text="Select Destination Directory", command=self.choose_destination_directory)
        self.destination_button.pack(padx=10, pady=10)
        
        # Create the organize files button
        self.organize_button = tk.Button(master, text="Organize Files", command=self.organize_files)
        self.organize_button.pack(padx=10, pady=10)
        
        # Set the source and destination directories to None
        self.source_dir = None
        self.destination_dir = None
    
    def choose_source_directory(self):
        # Use the file explorer to select the source directory
        self.source_dir = filedialog.askdirectory()
        print(f"Selected source directory: {self.source_dir}")
    
    def choose_destination_directory(self):
        # Use the file explorer to select the destination directory
        self.destination_dir = filedialog.askdirectory()
        print(f"Selected destination directory: {self.destination_dir}")
    
    def organize_files(self):
        if not self.source_dir or not self.destination_dir:
            # If the source or destination directory is not set, show an error message
            tk.messagebox.showerror("Error", "Please select both the source and destination directories")
        else:
            # Walk through all the files in the source directory
            for dirpath, dirnames, filenames in os.walk(self.source_dir):
                for filename in filenames:
                    # Get the full path of the file
                    filepath = os.path.join(dirpath, filename)

                    # Get the file extension and create a folder with the same name as the extension
                    extension = os.path.splitext(filename)[-1].lower()
                    folder = os.path.join(self.destination_dir, extension[1:])
                    if not os.path.exists(folder):
                        os.makedirs(folder)

                    # Move the file to the destination folder
                    shutil.move(filepath, folder)
            
            # Show a success message
            tk.messagebox.showinfo("Success", "Files organized successfully")

# Create the main application window
root = tk.Tk()
app = FileOrganizerGUI(root)
root.mainloop()
