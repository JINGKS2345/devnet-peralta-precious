"""
Module 2 — Activity: File Sorting with os and shutil
Student: Peralta, Precious Pauline M.
Date: 09-27-26

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[Paste your working script below first, then come back and explain
it here: what does your script do, and what rule did you use to
sort the files? e.g. by extension, by name, by date, etc.]


============================================
KEY VOCABULARY
============================================
- os module:
- shutil module:
- file path:
- directory:
(add more as needed)


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
A MISTAKE I MADE (or one I want to avoid)
============================================
[what tripped you up while building this? e.g. a path that didn't
exist, a file that got overwritten, something that didn't work the
way you expected at first]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
