# Comprare CSV Reader

## Description

This project is designed to read large CSV files using different methods and compare their performance. It generates a CSV file with fake data and then reads it using various techniques to measure the time taken for each method.

## Features

- Generate a CSV file with fake data
- Read CSV files using:
  - Python's built-in `csv` module
  - Pandas with chunksize
  - Pandas with an iterator
- Compare the performance of each method

## Requirements

- Python 3.9 or higher
- `pandas==2.2.2`
- `faker==28.4.1`
- `rich==13.8.1`
- `black==23.9.1`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your_username/read_csv_compare.git
    cd read_csv_compare
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the script to generate the CSV file and compare the performance of different reading methods:
    ```sh
    python read_csv_large_files.py
    ```

2. The results will be displayed in a table format in the console.

## Configuration

The project uses `black` for code formatting. You can configure it in the `pyproject.toml` file.

## License

This project is licensed under the MIT License.