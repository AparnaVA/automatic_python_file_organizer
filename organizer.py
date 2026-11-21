
import os
import shutil

# 1. Ask the user for the folder path
folder_path = input("Enter the folder path to organize: ")

# 2. Check whether the folder exists
if not os.path.isdir(folder_path):
    print("Invalid folder path!")
else:

    # 3. Define file categories and their extensions
    categories = {
        "Documents": [".pdf", ".doc", ".docx"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Spreadsheets": [".xls", ".xlsx", ".csv"],
        "Text Files": [".txt"],
        "Programs": [".py", ".java", ".cpp", ".c"]
    }

    # 4. Create destination folders
    for category in categories:
        folder = os.path.join(folder_path, category)
        os.makedirs(folder, exist_ok=True)

    # Create Others folder
    others_folder = os.path.join(folder_path, "Others")
    os.makedirs(others_folder, exist_ok=True)

    # 5. Create counters for each category
    counts = {
        "Documents": 0,
        "Images": 0,
        "Spreadsheets": 0,
        "Text Files": 0,
        "Programs": 0,
        "Others": 0,
        "Failed": 0
    }

    # 6. Scan all files in the given folder
    for filename in os.listdir(folder_path):

        # Get full path of the file
        source_path = os.path.join(folder_path, filename)

        # Skip folders
        if not os.path.isfile(source_path):
            continue

        # Get file extension
        extension = os.path.splitext(filename)[1].lower()

        # 7. Find the correct category
        destination_category = "Others"

        for category, extensions in categories.items():
            if extension in extensions:
                destination_category = category
                break

        # 8. Get destination folder path
        destination_folder = os.path.join(
            folder_path, destination_category
        )

        # 9. Create destination filename
        destination_path = os.path.join(
            destination_folder, filename
        )

        # 10. Prevent overwriting files
        if os.path.exists(destination_path):
            name, ext = os.path.splitext(filename)
            counter = 1

            while True:
                new_filename = f"{name}_{counter}{ext}"
                destination_path = os.path.join(
                    destination_folder, new_filename
                )

                if not os.path.exists(destination_path):
                    break

                counter += 1

        # 11. Move the file
        try:
            shutil.move(source_path, destination_path)
            counts[destination_category] += 1
            print(f"Moved: {filename} -> {destination_category}")

        except Exception as e:
            counts["Failed"] += 1
            print(f"Failed to move {filename}: {e}")

    # 12. Display summary
    print("\n----- File Organization Summary -----")

    for category, count in counts.items():
        print(f"{category}: {count}")

    print("\nFile organization completed!")
