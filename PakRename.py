import os
import shutil
import argparse


def rename_and_clone_files(directory):
    # Create a new directory named "mods" to store renamed .pak files
    mods_directory = os.path.join(directory, "mods")
    os.makedirs(mods_directory, exist_ok=True)

    # Get a list of all subdirectories in the main directory
    subdirectories = [subdir for subdir in os.listdir(directory) if os.path.isdir(os.path.join(directory, subdir))]

    # Iterate through each subdirectory
    for subdir in subdirectories:
        # Extract the number from the subdirectory name
        number = subdir.strip()

        # Get the path to the contents.pak file
        contents_pak_file = os.path.join(directory, subdir, "contents.pak")

        # Check if the contents.pak file exists in the current directory
        if os.path.exists(contents_pak_file):
            # Create the new name for the .pak file
            new_pak_name = number + ".pak"

            # Rename the contents.pak file to the new name and move it to the "mods" directory
            new_pak_path = os.path.join(mods_directory, new_pak_name)
            shutil.copy(contents_pak_file, new_pak_path)


def main():
    parser = argparse.ArgumentParser(description="Rename and clone .pak files in a directory.")
    parser.add_argument("directory", help="Path to the main directory containing subdirectories")
    args = parser.parse_args()

    if os.path.exists(args.directory):
        rename_and_clone_files(args.directory)
        print("Files renamed and cloned successfully.")
    else:
        print("Error: The specified directory does not exist.")


if __name__ == "__main__":
    main()
