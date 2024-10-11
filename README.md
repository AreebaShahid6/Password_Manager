# Password_Manager
![password](https://github.com/user-attachments/assets/0bcd2910-2477-447c-812a-e6db44d7de05)
## Introduction

The Password Manager is a desktop application built using Python’s Tkinter for the user interface. It allows users to generate strong, random passwords and store them securely on their local machine. In today’s world, managing passwords for various websites and accounts can be challenging. This simple tool helps by creating robust passwords and saving them securely, eliminating the need to remember multiple passwords. The stored data can also be managed by viewing or deleting old entries.

This project provides an easy-to-use, intuitive interface that can be expanded with features such as encryption and cloud backup.

---

## Features

- **Generate Random Passwords**: The password generator can create strong and complex passwords that combine letters, numbers, and symbols to meet modern security standards.
- **Store Passwords Locally**: All passwords are saved to a `data.txt` file on your local machine. Passwords are stored along with the associated website and email for easy retrieval.
- **View Saved Passwords**: Users can open a separate window to see all previously saved passwords.
- **Delete Saved Passwords**: Passwords that are no longer needed can be deleted from the list with a simple button click.
- **Password Copying**: The generated password is automatically copied to your clipboard for easy pasting into websites or forms.
- **User-friendly Interface**: The app is designed with simplicity in mind, making it accessible to users of all skill levels.

---

## Technologies Used

- **Python 3.8+**: The core programming language used to build this project.
- **Tkinter**: A Python module used for creating the graphical user interface (GUI).
- **pyperclip**: A cross-platform Python module used to copy the generated password to the clipboard automatically.
  
---

## Project Structure

- `main.py`: Contains the main logic for password generation, saving, viewing, and deleting passwords.
- `data.txt`: Stores saved passwords in a text file, formatted as `Website | Email | Password`.
- `logo.png`: The logo for the application, which is displayed on the main interface.
- `pyproject.toml`: Contains the project dependencies (e.g., pyperclip).

---

## Setup Instructions

### Prerequisites

- **Python**: Ensure Python 3.8 or higher is installed on your machine. You can download it [here](https://www.python.org/downloads/).
- **Tkinter**: Tkinter is included with Python on most systems, but you can install it using the following command if needed:
  ```bash
  sudo apt-get install python3-tk

