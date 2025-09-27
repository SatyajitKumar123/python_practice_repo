import os

def list_files():
    current_dir = os.getcwd()
    print(f"Files in: {current_dir}")
    print("--" * 45)

    for item in os.listdir(current_dir):
        item_path = os.path.join(current_dir, item)

        if os.path.isfile(item_path):
            size = os.path.getsize(item_path)
            print(f"{item} - {size} bytes")
        else:
            print(f"{item} - [Folder]")

list_files()