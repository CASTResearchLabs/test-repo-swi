import re

def read_file(file_path):
    """
    Reads the content of a file.

    Args:
        file_path (str): Path to the input file.

    Returns:
        str: Content of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If there is an error reading the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError as fnf_error:
        raise FileNotFoundError(f"File not found: {file_path}") from fnf_error
    except IOError as io_error:
        raise IOError(f"Error reading file: {file_path}") from io_error

def search_and_replace(content, pattern, replacement):
    """
    Searches for a regex pattern in the content and replaces it with the replacement text.

    Args:
        content (str): The text content to process.
        pattern (str): The regex pattern to search for.
        replacement (str): The text to replace matches with.

    Returns:
        str: Transformed content with replacements.

    Raises:
        re.error: If the regex pattern is invalid.
    """
    try:
        return re.sub(pattern, replacement, content)
    except re.error as regex_error:
        raise re.error(f"Invalid regex pattern: {pattern}") from regex_error

def write_file(file_path, content):
    """
    Writes content to a file.

    Args:
        file_path (str): Path to the output file.
        content (str): Content to write into the file.

    Raises:
        IOError: If there is an error writing to the file.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except IOError as io_error:
        raise IOError(f"Error writing to file: {file_path}") from io_error

def process_file(input_path, output_path, pattern, replacement):
    """
    Reads a file, replaces text matching a pattern, and writes to another file.

    Args:
        input_path (str): Path to the input file.
        output_path (str): Path to the output file.
        pattern (str): Regex pattern to search for.
        replacement (str): Replacement text for the matched pattern.

    Raises:
        Exception: Propagates exceptions from file operations or regex errors.
    """
    try:
        content = read_file(input_path)
        transformed_content = search_and_replace(content, pattern, replacement)
        write_file(output_path, transformed_content)
    except Exception as e:
        raise Exception(f"Error processing file: {e}") from e

if __name__ == "__main__":
    # Example usage
    try:
        input_file = "input.txt"
        output_file = "output.txt"
        search_pattern = r"hello"
        replacement_text = "hi"

        process_file(input_file, output_file, search_pattern, replacement_text)
        print(f"File processed successfully. Transformed content written to {output_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")
