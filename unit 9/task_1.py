import os
import shutil
import random
import string

def sort_files_by_extension_with_rename(folder_path):



    os_name = os.name


    current_directory = os.getcwd()

    print("Operating system:", os_name)
    print("Current working directory:", current_directory)


    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created.")

    extensions = ['.txt', '.pdf', '.jpg', '.docx']
    for i in range(5):
        extension = random.choice(extensions)
        file_name = f"file_{i}{extension}"
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'w') as f:
            f.write("Example file content")


    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            base, extension = os.path.splitext(file_name)
            extension = extension.lower()


            subfolder_path = os.path.join(folder_path, extension[1:])
            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)


            shutil.move(file_path, subfolder_path)


            files_in_subfolder = os.listdir(subfolder_path)
            if files_in_subfolder:
                file_to_rename = random.choice(files_in_subfolder)
                old_name = os.path.join(subfolder_path, file_to_rename)
                new_name = os.path.join(subfolder_path, "renamed_" + file_to_rename)
                os.rename(old_name, new_name)
                print(f"File '{old_name}' was renamed to '{new_name}'")

    for subfolder in os.listdir(folder_path):
        subfolder_path = os.path.join(folder_path, subfolder)
        if os.path.isdir(subfolder_path):
            number_of_files = len(os.listdir(subfolder_path))
            total_size = sum(os.path.getsize(os.path.join(subfolder_path, f)) for f in os.listdir(subfolder_path))
            print(f"{number_of_files} files were moved to the folder with {subfolder} files, their total size is {total_size / 1024*3:.2f} GB")


folder_path = "directory"
sort_files_by_extension_with_rename(folder_path)