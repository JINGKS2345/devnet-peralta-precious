"""
============================================
Module 2 — Activity: File Sorting with os and shutil
Student: [your name]
Date: [date]
============================================

============================================
WHAT DID YOU BUILD?
============================================
- I built a Python script that automatically
sorts files into differentfolders based on
their file extensions. For example, image files
are moved to the Images folder, document files
are moved to the Documents folder, audio files 
are moved to the Audio folder, and video files
are moved to the Videos folder.
============================================

============================================
The rule I used to sort the files is by file extension.
The script checks the extension of each file and moves it to the appropriate folder.

os module: A Python module used to work with files, folders, and file paths.
shutil module: A Python module used to move, copy, and manage files and folders.
file path: The location of a file or folder on a computer.
directory: Another name for a folder that contains files or other folders.
file extension: The part of a filename after the dot, such as .jpg, .pdf, or .txt.
source folder: The folder where the files are originally located.
destination folder: The folder where the files will be moved.
============================================

============================================
KEY VOCABULARY
============================================
- os module:
- shutil module:
- file path:
- directory:
- file extension:
- source folder:
============================================

============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""
import os
import shutil

source_folder = "files"

categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv"]
}

for file_name in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file_name)

    if os.path.isfile(file_path):
        extension = os.path.splitext(file_name)[1].lower()

        for folder, extensions in categories.items():
            if extension in extensions:
                destination_folder = os.path.join(source_folder, folder)

                os.makedirs(destination_folder, exist_ok=True)

                shutil.move(
                    file_path,
                    os.path.join(destination_folder, file_name)
                )

                print(f"Moved {file_name} to {folder}")
                break
"""
============================================

============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
- One mistake I need to avoid is using a folder path that does not exist.
Also, if the source folder is incorrect, the program will not be able to
find the files causing an error when u run the program.
============================================

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]

- File Sorting with os and shutil is kind a similar to that since
this type of script could be used for organizing our school files.
such us student's homeworks, attendance, grades, and many more different 
tytpes of school related records. It is also efficient in a way that it 
can automatically sort our files into the correct folders based on its file extensions.
save time by automatically sorting files into the correct
============================================
"""
