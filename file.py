def read_and_modify_file(input_filename, output_filename):
    try:
        # Read the input file
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()
        
        # Modify content: Add line numbers
        modified_lines = [f"{i+1}: {line}" for i, line in enumerate(lines)]
        
        # Write to output file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_lines)
        
        print(f"Success! Modified file written to {output_filename}")
        return True
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
        return False
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_filename}' or writing to '{output_filename}'.")
        return False
    except IOError as e:
        print(f"Error: An I/O error occurred: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def main():
    while True:
        # Prompt user for input file name
        input_filename = input("Enter the input file name (e.g., input.txt): ").strip()
        
        # Define output file name
        output_filename = "output_modified.txt"
        
        # Attempt to process the file
        if read_and_modify_file(input_filename, output_filename):
            break  # Exit loop on success
        
        # Ask if user wants to retry
        retry = input("Do you want to try another file? (yes/no): ").strip().lower()
        if retry != 'yes':
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()