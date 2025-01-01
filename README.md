# Photo Renamer

This Python app renames photos in a directory based on the date information extracted from their EXIF metadata. The purpose of this tool is to simplify the process of sorting photos chronologically, especially for creating photo calendars on online websites.

## Features
- Renames image files to include the date captured (e.g., `2023-01-01.jpg`).
- Handles common image formats that include EXIF data (e.g., JPEG).
- Skips files without valid EXIF date information.
- Overwrites existing files with the same name (use with caution).

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/paulglaserkitchensimp/RenamePhotosCalendar.git
   cd RenamePhotosCalendar
   ```
2. Ensure you have Python 3.12 installed.
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Place all the photos you want to rename into a single directory.
2. Run the script:
   ```bash
   python photo_renamer.py
   ```
   Provide the directory `C:\path\to\photo\directory` with the path to your photo folder.
3. The script will rename the photos in the directory based on their EXIF data.

## Limitations
- Only works on files with valid EXIF metadata containing a capture date.
- May not work on all image formats (optimized for JPEG).

## License
This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this tool for personal use.
