EXAMPLE 1
python extract_logs.py 2024-12-01
Successfully extracted logs_2024.log.zip to the current directory.
Extraction complete: 226025 log entries saved to output/output_2024-12-01.txt

EXAMPLE 2
python extract_logs.py 2024-12-08
Successfully extracted logs_2024.log.zip to the current directory.
Extraction complete: 227188 log entries saved to output/output_2024-12-01.txt

Solutions Considered:
Direct Parsing of Large Log Files:

Approach: Open the log file directly and iterate through it line by line. For each line, check if the timestamp matches the given date, then write the matching lines to the output file.
Pros: Simple approach with minimal complexity.
Cons: Not feasible for large files (1 TB), as reading the entire file sequentially would take a long time and consume excessive resources.
Indexed Search:

Approach: Create an index for each log entry where the index maps dates to the lines containing that date. When a search query is made, the program can refer to the index for quick retrieval of matching lines.
Pros: Faster retrieval for multiple queries.
Cons: Requires additional disk space and time to create and maintain the index. Also, not suitable for large, unindexed log files already in production.
Chunking:

Approach: Split the log file into manageable chunks (e.g., by day, week, or month). Read through the chunks in parallel to efficiently process the logs.
Pros: Makes the task manageable by working on smaller chunks of data at a time.
Cons: Requires complex logic to handle parallel processing and might still lead to inefficiency when dealing with an entire 1 TB file.
ZIP Extraction and Direct Search (Final Solution Chosen):

Approach: If the log file is compressed in a ZIP archive, first extract the file, and then read it line by line. For each line, check if the timestamp matches the specified date and save matching lines to a separate file.
Pros:
Simple and effective for extracting logs when the file is compressed.
Efficient memory usage: It reads one line at a time, so it doesn't need to load the entire file into memory.
No need for additional indexing or complex chunking logic.
Cons: Requires initial extraction of the ZIP file, which could be time-consuming for extremely large ZIP archives. However, this step is only performed once.
Final Solution Summary:
The final solution was chosen because it:
Simplicity: It is straightforward, uses basic file handling and string matching, and leverages Python's built-in libraries like zipfile for extraction and efficient file reading.
Memory Efficiency: It processes the log file line by line, which is memory efficient and works well even for large files (e.g., 1 TB).
Practicality: It handles the case where the log file is compressed in a ZIP format and extracts it only when needed. Once extracted, it processes the log entries efficiently without excessive memory or CPU usage.
Scalability: This solution can handle large files without loading the entire file into memory, making it more scalable compared to approaches that require indexing or chunking.
Thus, the combination of ZIP extraction followed by line-by-line reading and matching was considered the most efficient approach given the constraints.

Steps to Run:
Ensure Python is Installed:

Verify that Python is installed on your machine. You can check by running the command:

python --version
Prepare the Log File:

Download the logs_2024.log.zip file and ensure it is available at the specified location: C:\Users\himan\Downloads\logs_2024.log.zip.
Save the Script:

Save the Python script (with the updated logic for ZIP extraction and log extraction) as extract_logs.py on your local machine.
Run the Script:

Open the command line and navigate to the directory where the script is saved.

Run the script using the following command (replace YYYY-MM-DD with the actual date you want to search for):

python extract_logs.py 2024-12-01
Check the Output:

After running the script, the logs for the specified date (2024-12-01 in this example) will be saved to the output/output_2024-12-01.txt file.
The command line will display the number of log entries found and saved.
Verify the Output:

Open the output/output_2024-12-01.txt file and verify that it contains the correct log entries from the specified date.


