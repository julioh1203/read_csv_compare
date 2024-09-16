import csv
import timeit

import pandas as pd
from faker import Faker
from rich.console import Console
from rich.table import Table


def get_data(range_size: int = 16000):
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
    with open("data.csv", "w", newline="") as csvfile:
        fieldnames = ["id", "email"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_dict)


def read_csv(file_name):
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            yield row


def get_csv_rows_with_python():
    start = timeit.default_timer()
    result = [row for row in read_csv("data.csv")]
    return ["Python CSV", len(result), timeit.default_timer() - start]


def read_csv_pandas_chunksize(file_name):
    for chunk in pd.read_csv(file_name, chunksize=10000):
        yield chunk


def get_csv_rows_with_pandas_and_chunk():
    start = timeit.default_timer()
    result = [df for df in read_csv("data.csv")]
    return ["Pandas CSV Chunksize", len(result), timeit.default_timer() - start]


def read_csv_with_pandas_iterator(file_name):
    for row in pd.read_csv(file_name, iterator=True):
        yield row


def get_csv_rows_pandas_iterator():
    start = timeit.default_timer()
    result = [df for df in read_csv("data.csv")]
    return ["Pandas CSV Iterator", len(result), timeit.default_timer() - start]


def get_results():

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
    data_dict = get_data(32000)
    generate_csv(data_dict)
    get_results()
