import os
import random
import shutil

def move_random_files(source_dir, destination_dir, num_files):
    # Check if the source directory exists
    if not os.path.isdir(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return
    
    # Check if the destination directory exists, if not, create it
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    # Get list of files in source directory
    files = os.listdir(source_dir)
    
    # Randomly select specified number of files
    selected_files = random.sample(files, min(num_files, len(files)))
    
    # Move selected files to destination directory
    for file in selected_files:
        source_path = os.path.join(source_dir, file)
        destination_path = os.path.join(destination_dir, file)
        shutil.move(source_path, destination_path)
        print(f"Moved '{file}' to '{destination_dir}'")

if __name__ == "__main__":
    source_directory = input("Enter the source directory path: ")
    destination_directory = input("Enter the destination directory path: ")
    num_files_to_move = int(input("Enter the number of files to move: "))

    move_random_files(source_directory, destination_directory, num_files_to_move)

