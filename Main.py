import os
import exifread
from datetime import datetime

# Function to get the date from the EXIF data of an image
def get_image_date(file_path):
    try:
        with open(file_path, 'rb') as f:
            tags = exifread.process_file(f)
            if 'EXIF DateTimeOriginal' in tags:
                date_str = str(tags['EXIF DateTimeOriginal'])
                date_obj = datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S')
                return date_obj.strftime('%Y-%m-%d_%H-%M-%S')
            else:
                return None
    except IOError as e:
        print(f"Error processing {file_path}: {e}")
        return None
    except ValueError as e:
        print(f"Error processing {file_path}: {e}")
        return None

# Rename files in the folder based on their EXIF date
def rename_files_with_date(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
            file_path = os.path.join(folder_path, filename)
            date = get_image_date(file_path)
            if date:
                new_filename = f"{date}_{filename}"
                new_file_path = os.path.join(folder_path, new_filename)
                try:
                    os.rename(file_path, new_file_path)
                    print(f"Renamed {filename} to {new_filename}")
                except OSError as e:
                    print(f"Error renaming {filename} to {new_filename}: {e}")

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder containing JPG/JPEG files: ")
    rename_files_with_date(folder_path)



