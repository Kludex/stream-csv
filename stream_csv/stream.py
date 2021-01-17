from typing import List


def quoted(value: str) -> str:
    return f'"{value}"'


def list_to_row(values: list, delimiter: str) -> str:
    return f"{delimiter} ".join([quoted(value) for value in values])


def dict_to_row(data: dict, headers: List[str], delimiter: str) -> str:
    return list_to_row([data[header] for header in headers], delimiter)


def stream_data(dict_data: List[dict], headers: List[str], delimiter: str = ","):
    yield list_to_row(headers, delimiter) + "\n"
    for data in dict_data:
        yield dict_to_row(data, headers, delimiter) + "\n"
