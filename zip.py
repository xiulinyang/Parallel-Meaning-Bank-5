import zipfile
import os

def zip_directory(folder_path, output_zip_file):
    """
    Zips an entire directory recursively including all its subdirectories and files.
    
    Args:
    folder_path (str): The path to the directory to zip.
    output_zip_file (str): The path and filename for the resulting .zip file.
    """
    with zipfile.ZipFile(output_zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Store the path relative to the folder being zipped
                relative_path = os.path.relpath(file_path, os.path.dirname(folder_path))
                zipf.write(file_path, arcname=relative_path)
                print(f"Adding {file_path} as {relative_path}")

# Example usage
folder_path = 'results'  # Replace with the path to the directory you want to zip
output_zip_file = 'results.zip'  # Desired path and name of the output zip file

zip_directory(folder_path, output_zip_file)

