
# Student Management System

A simple, interactive command-line Python application for managing student records, calculating CGPAs, and filtering by skills.

## Features
- **Display students:** View a list of all current students and their details.
- **Top student:** Automatically identify the highest-performing student based on CGPA.
- **Search functionality:** Find specific students by their name or filter the database by a specific skill (e.g., "Python").
- **Class metrics:** Calculate the average CGPA across all enrolled students.
- **Manage records:** Add new students to the system or remove existing ones.

## Project Structure
- `main.py`: The entry point of the application containing the interactive user menu.
- `student_utils.py`: Contains the core logic and functions for processing student data.
- `validation.py`: Contains helper functions to ensure valid data entry for names, ages, CGPA, and skills.

## How to Run
1. Ensure you have Python installed on your system.
2. Download or clone this repository so all three Python files are in the same folder.
3. Open your terminal or command prompt, navigate to the folder, and execute:
   ```bash
   python main.py
   ```
