# Password_Manager
# Password Manager

This is a Python-based Password Manager that helps you generate strong, random passwords and store them locally in a text file. It allows you to:

- **Generate random passwords** with letters, symbols, and numbers.
- **Save passwords** associated with a website and email/username.
- **View saved passwords** in a separate window.
- **Delete passwords** that are no longer needed.

## Features

- **Password Generator**: Randomly generates secure passwords with customizable lengths using letters, numbers, and symbols.
- **Password Storage**: Saves passwords along with the corresponding website and username/email locally in a `data.txt` file.
- **Password Viewer**: Displays all saved passwords in a new window and allows for easy deletion.
- **Clipboard Copying**: Automatically copies the generated password to your clipboard for quick use.

## Requirements

To run this project, you need the following installed:

- Python 3.8 or higher
- `pyperclip` library (for copying passwords to the clipboard)

Install the required Python package using:

```bash
pip install pyperclip
