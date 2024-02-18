import os


def rename_files(folder_path, new_name):
    # Get all files in the folder
    files = os.listdir(folder_path)

    # Sort files by modification time (oldest first)
    files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))

    # Iterate over sorted files and rename them
    for i, filename in enumerate(files, start=1):
        # Construct the new filename
        new_filename = f"{new_name}_{i}.mp3"

        # Rename the file
        os.rename(
            os.path.join(folder_path, filename), os.path.join(folder_path, new_filename)
        )

        print(f"Renamed {filename} to {new_filename}")


folder_path = "path/to/Folder"
new_name = "AI Voice"
rename_files(folder_path, new_name)
