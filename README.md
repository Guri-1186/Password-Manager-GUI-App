# Password Manager

A simple password manager built using Python and Tkinter. It allows users to generate strong passwords, save them securely in a JSON file, and retrieve saved credentials.

## Features

- **Generate Secure Passwords**: Creates a random password with letters, numbers, and symbols.
- **Save Credentials**: Stores website credentials (email & password) in `data.json`.
- **Retrieve Saved Credentials**: Quickly look up stored credentials using the website name.

## Installation

### Prerequisites

Ensure you have Python installed on your system. You also need the following libraries:

```sh
pip install pyperclip
```

## Project Structure

```
password-manager/
│── main.py             # GUI and event handling
│── password_manager.py # Logic for password generation and data storage
│── data.json           # Stored credentials (auto-created)
│── logo.png            # App logo
│── README.md           # Project documentation
```

## Usage

### Running the Application

Run the following command in your terminal:

```sh
python main.py
```

### Functionality

1. **Generate Password**
   - Click `Generate Password` to create a strong password.
   - The password will be copied to the clipboard.
2. **Save Credentials**
   - Enter the website, email, and generated password.
   - Click `Add` to save the credentials.
3. **Search for Saved Credentials**
   - Enter a website name and click `Search` to retrieve saved credentials.

## File Descriptions

- `main.py`: Handles the graphical user interface (GUI) using Tkinter.
- `password_manager.py`: Contains logic for generating passwords, saving data, and retrieving credentials.
- `data.json`: Stores saved passwords in JSON format.
- `logo.png`: An optional image used as the application’s logo.

## Notes

- If `data.json` is missing, it will be created automatically.
- Data is stored in plain text JSON format. Consider encrypting it for added security.
