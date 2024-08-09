import os

def rename_images(directory):
    # Get all files in the directory
    files = os.listdir(directory)
    # Filter out only files that are images (jpg, png, etc.)
    image_files = [file for file in files if file.lower().endswith(('jpg', 'jpeg', 'png', 'gif', 'bmp'))]

    for i, filename in enumerate(image_files, start=1):
        # Get the file extension
        file_extension = os.path.splitext(filename)[1]
        # Create new filename
        new_filename = f"vehicle{i}{file_extension}"
        # Construct full file paths
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_filename)
        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed {filename} to {new_filename}")

# Specify the directory containing the images
directory_path = "D:/RR/rename"

# Call the rename function
rename_images(directory_path)
