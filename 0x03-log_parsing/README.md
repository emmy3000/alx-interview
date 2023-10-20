# 0x03. Log Parsing

The Log Parsing Script named `0.stats.py` processes log lines from standard input (stdin) and calculates metrics for various HTTP status codes and the total file size.

### Features
- Computes the count of various HTTP status codes, such as 200, 301, 400, and more.
- Calculates the total file size.
- Provides a summary of metrics at the end of processing.

### Usage
1. Ensure you have Python 3 installed on your system.
2. Pipe log data into the script using the following command:
```shell
# Script can accept a log file containing various status codes to be measured.
cat some_log_file.txt | ./0-statspy

# Scripts also accepts stdout from another script generating HTTP codes.
./0-generator.py | ./0-stats.py
```

### Example Output
```shell
File size: 1234567
200: 450
301: 25
400: 12
404: 8
500: 2
...
```

### Author
Emeka Emodi
