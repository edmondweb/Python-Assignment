# Creating a program that reads a file and writes modified version to a new file.

def read_and_modify_file(input_file, output_file):
    """
    Reads a file, modifies its content by converting all text to uppercase,
    and writes the modified content to a new file.

    Parameters:
    input_file (str): The path to the input file to read.
    output_file (str): The path to the output file to write the modified content.
    """
    
    try:
        with open(input_file, 'r') as infile:
            content = infile.read()
        
        modified_content = content.upper()
        
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content written to {output_file}")
    
    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage of the read_and_modify_file function
input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")
read_and_modify_file(input_file, output_file)