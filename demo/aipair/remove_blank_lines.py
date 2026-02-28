def remove_blank_lines(filename: str) -> None:
    """
    Removes all blank lines from a file.

    Args:
        filename (str): The path to the file to process.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    try:
        # Read all lines from the file
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Filter out blank lines (lines that contain only whitespace)
        non_blank_lines = [line for line in lines if line.strip()]

        # Write the filtered lines back to the file
        with open(filename, 'w') as file:
            file.writelines(non_blank_lines)

        print(f"Blank lines removed from {filename}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


# Execute the program
if __name__ == "__main__":
    remove_blank_lines("names.txt")