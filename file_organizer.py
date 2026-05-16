import os
import shutil

# Folder path to organize
folder_path = input("Enter folder path: ").strip()

print("You entered:", folder_path)

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Python Files": [".py"]
}

# Check if folder exists
if os.path.exists(folder_path):

    # Read all files
    files = os.listdir(folder_path)

    for file in files:

        file_path = os.path.join(folder_path, file)

        # Skip folders
        if os.path.isfile(file_path):

            # Get extension
            extension = os.path.splitext(file)[1].lower()

            moved = False

            # Check file category
            for folder_name, extensions in file_types.items():

                if extension in extensions:

                    # Create category folder
                    target_folder = os.path.join(folder_path, folder_name)

                    os.makedirs(target_folder, exist_ok=True)

                    # Move file
                    shutil.move(file_path, os.path.join(target_folder, file))

                    print(f"Moved: {file} → {folder_name}")

                    moved = True
                    break

            # Uncategorized files
            if not moved:

                other_folder = os.path.join(folder_path, "Others")

                os.makedirs(other_folder, exist_ok=True)

                shutil.move(file_path, os.path.join(other_folder, file))

                print(f"Moved: {file} → Others")

    print("\n✅ File organization completed successfully.")

else:
    print("❌ Invalid folder path.")