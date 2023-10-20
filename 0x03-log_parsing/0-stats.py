#!/usr/bin/python3
'''
A script that reads input from stdin line by line
and computes HTTP status code metrics.

It processes log lines and calculates the count of various HTTP status codes
(e.g., 200, 301, 400), and the total file size from the input stream.
The computed metrics are printed at the end of processing.

Usage:
    $ ./0-generator.py | ./0-stats.py
'''

import sys

cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])
            if code in cache:
                cache[code] += 1
            total_size += size
            counter += 1

        if counter == 10:
            counter = 0
            print('File size: {}'.format(total_size))
            for key, value in sorted(cache.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
