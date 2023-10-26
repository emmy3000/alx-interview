# 0x04. UTF-8 Validation

This repository contains a Python script to determine if a given dataset represents a valid UTF-8 encoding. UTF-8 is a character encoding standard that is widely used in computing to represent text in various languages. Ensuring the validity of UTF-8 encoded data is crucial when processing text to avoid errors and maintain data integrity.


## Table of Contents
- [Overview](#overview)
- [Understanding UTF-8 Encoding](#understanding-utf-8-encoding)
- [Validation with the `validUTF8` Function](#validation-with-the-validutf8-function)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Prerequisites](#prerequisites)
- [Author](#author)

## Overview

UTF-8 is a variable-width character encoding that can represent all possible characters (code points) in the Unicode standard. It uses one to four bytes to represent a character, making it versatile for encoding text in different languages.

This project offers a Python script, `validUTF8`, which validates whether a given list of integers represents valid UTF-8 encoded characters.

## Understanding UTF-8 Encoding

UTF-8 is a character encoding that assigns a unique number, called a code point, to each character in the Unicode standard. These code points are then encoded into a variable number of bytes. Here's a brief overview of how UTF-8 encoding works:

- Characters in the ASCII character set (code points 0-127) are represented using one byte.
- Characters in the extended ASCII range (code points 128-255) are also represented using one byte.
- Characters with code points from 256 to 2047 are represented using two bytes.
- Characters with code points from 2048 to 65535 are represented using three bytes.
- Characters with code points from 65536 to 1114111 are represented using four bytes.

UTF-8 encoding ensures that text can be represented in a space-efficient manner while accommodating a wide range of characters.

## Validation with the `validUTF8` Function

The `validUTF8` function checks if a given list of integers represents valid UTF-8 encoded characters. Here's how it works:

1. It iterates through the list of integers, each representing 1 byte of data.
2. It checks the binary representation of each integer to ensure it follows UTF-8 rules.
3. If the input data adheres to the UTF-8 encoding rules, the function returns `True`; otherwise, it returns `False`.

## Getting Started

### Prerequisites

- Python 3.7

### Installation

- Create & navigate to the project directory:

```bash
mkdir 0-validate_utf8.py
cd 0-validate_utf8.py
```

## Usage

- In a test module(`0-main.py`) import the `validUTF8` function.

```python
validUTF8 = __import__('0-validate_utf8').validUTF8
```

- Provide a list of integers, where each integer represents 1 byte of data:

```python
data = [197, 130, 1]  # Replace with your data
```

- Call the validUTF8 function and check the result:

```python
result = validUTF8(data)
print(result)  # True if data is valid UTF-8, False otherwise
```

## Author

Emeka Emodi
