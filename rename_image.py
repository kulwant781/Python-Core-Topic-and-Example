# import os

# # Specify the folder containing image files
# folder_path = "Images"  # Change this to your actual folder path


# # List all files in the directory (case-insensitive search for JPG files)
# files = [f for f in os.listdir(folder_path) if f.lower().endswith(".jpeg")]

# print(f"Checking {len(files)} files...")

# # Sort files (optional, ensures consistent renaming)
# files.sort()

# # Loop through and rename files
# for index, filename in enumerate(files, start=1):
#     new_name = f"image_{index}.jpg"  # New naming pattern
#     old_path = os.path.join(folder_path, filename)
#     new_path = os.path.join(folder_path, new_name)
    
    
#     # Rename the file
#     os.rename(old_path, new_path)
#     print(f"Renamed: {filename} -> {new_name}")

# print("Batch renaming completed! Hello, world!")



import os

folder_path = "Images"  
files = os.listdir(folder_path)
i = 1
for filename in files:
    if filename.endswith(".jpg"):
        new_name = f"image_{i}.jpg"  # New naming pattern

        # Rename the file
        os.rename(f"{folder_path}/{filename}", f"{folder_path}/{new_name}")
        i = i+1
        print(f"Renamed: {filename} -> {new_name}")