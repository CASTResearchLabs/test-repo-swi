import os
import re
from file_processing import read_file, search_and_replace, write_file

def process_directory(input_dir, output_dir, pattern, replacement):
    """
    Processes all files in a directory by reading, replacing text patterns, and saving to another directory.

    Args:
        input_dir (str): Path to the input directory containing files.
        output_dir (str): Path to the output directory to save transformed files.
        pattern (str): Regex pattern to search for.
        replacement (str): Replacement text for the matched pattern.

    Raises:
        FileNotFoundError: If the input directory does not exist.
        Exception: If any other error occurs during processing.
    """
    if not os.path.isdir(input_dir):
        raise FileNotFoundError(f"Input directory not found: {input_dir}")

    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        input_file_path = os.path.join(input_dir, filename)
        output_file_path = os.path.join(output_dir, filename)

        if os.path.isfile(input_file_path):
            try:
                content = read_file(input_file_path)
                transformed_content = search_and_replace(content, pattern, replacement)
                write_file(output_file_path, transformed_content)
                print(f"Processed file: {filename}")
            except Exception as e:
                print(f"Error processing file {filename}: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        input_directory = "input_files"
        output_directory = "output_files"
        search_pattern = r"example"
        replacement_text = "sample"

        process_directory(input_directory, output_directory, search_pattern, replacement_text)
        print("All files processed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
