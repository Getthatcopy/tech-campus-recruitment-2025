import os
import sys
import zipfile

def extract_logs(input_file, search_date):
    """Extracts logs for a given date from a large log file."""
    
    # Ensure output directory exists
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Define the path for the extracted log file
    extracted_log_file = "logs_2024.log"

    # Check if the file is a ZIP archive
    if input_file.endswith(".zip"):
        try:
            with zipfile.ZipFile(input_file, 'r') as zip_ref:
                zip_ref.extractall()  # Extract the contents in the current directory
                print(f"Successfully extracted {input_file} to the current directory.")
        except Exception as e:
            print(f"Error extracting zip file: {e}")
            return

    # Define the output file for the logs of the specified date
    output_file = f"{output_dir}/output_{search_date}.txt"
    
    try:
        with open(extracted_log_file, "r") as infile, open(output_file, "w") as outfile:
            match_count = 0
            for line in infile:
                if line.startswith(search_date):  # Efficiently check first 10 chars (YYYY-MM-DD)
                    outfile.write(line)
                    match_count += 1

        print(f"Extraction complete: {match_count} log entries saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: Log file '{extracted_log_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ensure correct usage
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)

    search_date = sys.argv[1]  # Get the date from command line argument
    input_file = r"C:\Users\himan\Downloads\logs_2024.log.zip"  # Log ZIP file path

    extract_logs(input_file, search_date)
