# Most Active Cookie Analyzer

## Overview

The Most Active Cookie Analyzer is an command-line application that processes a cookie log file to identify the most active cookie(s) for a specified date.

## Directory Structure

```plaintext
.
├── data/                        # Scripts and sample data
│   ├── cookie_gen.py            # Cookie data generation script
│   └── cookie_log.csv           # Example cookie log file
├── docs/                        # Documentation and assignment details
│   └── assignment.pdf           # Detailed project assignment
├── src/                         # Source code for core functionality
│   ├── __init__.py              # Package initializer
│   └── cookie_analyzer.py       # Primary logic for cookie analysis
├── tests/                       # Comprehensive test suite
│   ├── data/                    # Test datasets for various scenarios
│   ├── __init__.py              # Test package initializer
│   └── test_cookie_analyzer.py  # Unit tests for the cookie analyzer
├── README.md                    # Project documentation (this file)
├── main.py                      # Application entry point
├── requirements.txt             # Project dependencies
└── setup.py                     # Application setup script
```

## Installation

Clone the repository:
```bash
$ git clone https://github.com/joshfinney/most-active-cookie
```

Navigate to the cloned directory:

```bash
$ cd most_active_cookie
```

Install dependencies:

```bash
$ pip install -r requirements.txt
```

## Usage

Run the Most Active Cookie Analyzer with the following command at the project root:

```bash
$ ./main.py -f cookie_log.csv -d 2023-12-28
```

## Features

* **Efficient Data Processing**: Implements optimised algorithms for fast and accurate processing of large datasets.
* **Robust Testing Framework**: Comprehensive test suite covering a wide array of scenarios, including edge cases, to ensure reliability and correctness.
* **Clean Code Design**: Codebase adheres to clean coding practices with meaningful naming conventions and clear abstractions.
* **Detailed Logging and Error Handling**: Logging for tracking processing steps and issues, alongside robust error handling mechanisms.
* **User-Centric CLI**: Intuitive command-line interface with efficient argument parsing.
* **Scalability and Maintainability**: Code structure designed for easy maintainability and scalability.

## Testing

Execute the test suite with the following command at the project root or tests directory:

```bash
$ pytest
```

The tests encompass scenarios such as basic functionality, boundary conditions, large file processing, and error handling, ensuring a reliable and robust application.
