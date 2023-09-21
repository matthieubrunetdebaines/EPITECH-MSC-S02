import os

def list_files_and_directories(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            print(f"Directory: {item_path}")
            list_files_and_directories(item_path)
        else:
            print(f"  File: {item_path}")

if __name__ == "__main__":
    current_directory = os.getcwd()
    list_files_and_directories(current_directory)
