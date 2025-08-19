# Error Handling

def ask_for_filename():
    """
    Asks the user for a filename, attempts to open the file, and handles
    exceptions if the file does not exist or permission is denied.

    Parameters: None

    Returns: None
    """
    filename = input("Please enter the filename to read: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"File {filename} opened successfully.")
    
    except FileNotFoundError:
        print(f"File {filename} does not exist.")
    except PermissionError:
        print(f"Permission denied for file {filename}.")
    except Exception as e:
        print(f"An error occurred: {e}")


ask_for_filename()