# Python File Organizer

## About the Project
Python File Organizer is a simple beginner-friendly Python project that automatically organizes files inside a selected folder based on their file extensions.

It creates separate folders for Documents, Images, Spreadsheets, Text Files, Programs, and Others, and moves files into the appropriate folders.

## Features
- Asks the user to enter the folder path to organize.
- Automatically scans files in the selected folder.
- Categorizes files based on their extensions.
- Creates separate folders for each category.
- Reuses folders if they already exist.
- Prevents files with identical names from being overwritten.
- Handles errors when files cannot be moved.
- Displays a summary of successfully moved files and failed operations.

## File Categories

| Category | File Extensions |
|---|---|
| Documents | `.pdf`, `.doc`, `.docx` |
| Images | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp` |
| Spreadsheets | `.xls`, `.xlsx`, `.csv` |
| Text Files | `.txt` |
| Programs | `.py`, `.java`, `.cpp`, `.c` |
| Others | All unsupported extensions |

## Technologies Used
- Python
- `os` module
- `shutil` module

## Project Structure

    file_organizer/
    │
    ├── organizer.py
    └── README.md

## How to Run

### 1. Clone the Repository

    git clone <your-repository-url>

### 2. Navigate to the Project Folder

    cd file_organizer

### 3. Run the Python Program

    python organizer.py

### 4. Enter the Folder Path

When prompted, enter the path of the folder you want to organize.

Example:

    C:\Users\YourName\Downloads

The program will create category folders inside the selected folder and move the files accordingly.

## Example

### Before Organizing

    Downloads/
    ├── report.pdf
    ├── photo.jpg
    ├── sales.xlsx
    ├── notes.txt
    ├── script.py
    └── archive.zip

### After Organizing

    Downloads/
    ├── Documents/
    │   └── report.pdf
    ├── Images/
    │   └── photo.jpg
    ├── Spreadsheets/
    │   └── sales.xlsx
    ├── Text Files/
    │   └── notes.txt
    ├── Programs/
    │   └── script.py
    └── Others/
        └── archive.zip

## Summary

This project helped me understand Python file handling, loops, dictionaries, conditional statements, exception handling, modules, and working with file paths. It also demonstrates how Python can automate everyday tasks.
