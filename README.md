# Password-Manager-GUI-App

## Overview

This is a simple password manager built using Python and Tkinter. It allows users to generate and store passwords securely in a local text file (`data.txt`). The passwords are automatically copied to the clipboard for easy pasting.

## Features

- Generate strong passwords with a mix of letters, numbers, and symbols.
- Save website credentials (Website, Email/Username, Password) to `data.txt`.
- Copy the generated password to the clipboard for quick access.
- Simple and user-friendly graphical interface.

## Requirements

- Python 3.x
- Required libraries:
  - `tkinter` (built-in with Python)
  - `random` (built-in with Python)
  - `pyperclip` (install using `pip install pyperclip`)

## Installation

1. Clone the repository or download the script.
2. Install dependencies using:
   ```sh
   pip install pyperclip
   ```
3. Run the script:
   ```sh
   python password_manager.py
   ```

## Usage

1. Enter the website name.
2. Enter the email or username.
3. Click "Generate Password" to create a strong password.
4. Click "Add" to save the credentials.
