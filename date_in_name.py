import os
import sys
import shutil
import pathlib
import datetime

# Handle arguments
if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <IMAGES_FOLDER>")
    exit(1)

input_folder = sys.argv[1]

if not os.path.isdir(input_folder):
    print(f"Folder not found: {input_folder}")
    exit(1)


# Create output folder
renamed_files_folder = "renamed_files"
if not os.path.isdir(renamed_files_folder):
    os.mkdir("renamed_files")


# Iterate on input folder contents
files_list = os.listdir(input_folder)
files_count = 0
for file in files_list:
    input_filepath = os.path.join(input_folder, file)
    file_extension = pathlib.Path(input_filepath).suffix

    # Get modification time
    modification_epoch_time = os.path.getmtime(input_filepath)
    dt = datetime.datetime.fromtimestamp(modification_epoch_time)

    # Create new name: YYYYMMDD_hhmmss.ext
    new_filename = f"{dt.year}{dt.month:02d}{dt.day:02d}_{dt.hour:02d}{dt.minute:02d}{dt.second:02d}{file_extension}"
    renamed_filepath = os.path.join(renamed_files_folder, new_filename)

    # If filename already exists, iterate to find a new name: YYYYMMDD_hhmmss_i.ext
    index = 1
    while os.path.exists(renamed_filepath):
        index += 1
        new_filename = f"{dt.year}{dt.month:02d}{dt.day:02d}_{dt.hour:02d}{dt.minute:02d}{dt.second:02d}_{index}{file_extension}"
        renamed_filepath = os.path.join(renamed_files_folder, new_filename)

    # Safely copy the file to the new fodler with a new name
    print(f"{file} -> {new_filename}")
    shutil.copy2(input_filepath, renamed_filepath)
    files_count += 1

print(f'Copied {files_count} files from "{input_folder}" to "{renamed_files_folder}"')
