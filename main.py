import os
import shutil

# Define the source directory and the destination directories for each file type
source_dir = "/path/to/source/directory"
destination_dirs = {
    ".jpg": "/path/to/Images",
    ".jpeg": "/path/to/Images",
    ".png": "/path/to/Images",
    ".gif": "/path/to/Images",
    ".doc": "/path/to/Documents",
    ".docx": "/path/to/Documents",
    ".pdf": "/path/to/Documents",
    ".txt": "/path/to/Documents",
    ".csv": "/path/to/Documents"
}

# Walk through all the files in the source directory
for dirpath, dirnames, filenames in os.walk(source_dir):
    for filename in filenames:
        # Get the file extension and the full path of the file
        extension = os.path.splitext(filename)[-1].lower()
        filepath = os.path.join(dirpath, filename)
        
        # Check if the file extension is in the destination directories dictionary
        if extension in destination_dirs:
            # If the destination directory doesn't exist, create it
            if not os.path.exists(destination_dirs[extension]):
                os.makedirs(destination_dirs[extension])
            
            # Move the file to the destination directory
            shutil.move(filepath, destination_dirs[extension])
