import csv
import timeit

import pandas as pd
from faker import Faker
from rich.console import Console
from rich.table import Table


def get_data(range_size: int = 32000):
    """Return a list of dictionaries with fake data."""
    fake_data = Faker("en_US")

    data_dict = [
        {
            "id": i + 1,
            "email": fake_data.email(),
        }
        for i in range(range_size)
    ]

    return data_dict


def generate_csv(data_dict):
    """Generate a CSV file with the data provided."""
    with open("data.csv", "w", newline="") as csvfile:
        fieldnames = ["id", "email"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_dict)


def read_csv(file_name):
    """Read a CSV file and return a generator with the rows."""
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            yield row


def get_csv_rows_with_python():
    """Read the CSV file with Python and return the amount of rows and the elapsed time."""
    start = timeit.default_timer()
    result = [row for row in read_csv("data.csv")]
    return ["Python CSV", len(result), timeit.default_timer() - start]


def read_csv_pandas_chunksize(file_name):
    """Read a CSV file with Pandas with chunksize=10000 and return a generator with the rows."""
    for chunk in pd.read_csv(file_name, chunksize=10000):
        yield chunk


def get_csv_rows_with_pandas_and_chunk():
    """Read the CSV file with Pandas with chunksize=10000 and return the amount of rows and the elapsed time."""
    start = timeit.default_timer()
    result = [df for df in read_csv("data.csv")]
    return ["Pandas CSV Chunksize", len(result), timeit.default_timer() - start]


def read_csv_with_pandas_iterator(file_name):
    """Read a CSV file with Pandas and return a generator with the rows."""
    for row in pd.read_csv(file_name, iterator=True):
        yield row


def get_csv_rows_pandas_iterator():
    """Read the CSV file with Pandas iterator and return the amount of rows and the elapsed time."""
    start = timeit.default_timer()
    result = [df for df in read_csv("data.csv")]
    return ["Pandas CSV Iterator", len(result), timeit.default_timer() - start]


def get_results():
    """Print the results in a table."""
    results = []
    console = Console()

    results.append(get_csv_rows_with_python())
    results.append(get_csv_rows_with_pandas_and_chunk())
    results.append(get_csv_rows_pandas_iterator())

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Type", justify="left")
    table.add_column("Amount of Data", justify="right")
    table.add_column("Elapsed Time", justify="right")

    results.sort(key=lambda x: x[2])

    for result in results:
        table.add_row(result[0], str(result[1]), str(round(result[2], 5)))

    console.print(table)


if __name__ == "__main__":
    data_dict = get_data(64000)
    generate_csv(data_dict)
    get_results()
