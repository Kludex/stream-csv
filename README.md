<h1 align="center">
    <strong>stream-csv</strong>
</h1>
<p align="center">
    <a href="https://github.com/Kludex/stream-csv" target="_blank">
        <img src="https://img.shields.io/github/last-commit/Kludex/stream-csv" alt="Latest Commit">
    </a>
        <img src="https://img.shields.io/github/workflow/status/Kludex/stream-csv/Test">
        <img src="https://img.shields.io/codecov/c/github/Kludex/stream-csv">
    <br />
    <a href="https://pypi.org/project/stream-csv" target="_blank">
        <img src="https://img.shields.io/pypi/v/stream-csv" alt="Package version">
    </a>
    <img src="https://img.shields.io/pypi/pyversions/stream-csv">
    <img src="https://img.shields.io/github/license/Kludex/stream-csv">
</p>


## Installation

``` bash
pip install stream-csv
```

## Usage

```python
from fastapi import FastAPI
from starlette.responses import StreamingResponse

from stream_csv.stream import stream_data

app = FastAPI()


@app.get("/")
def get_csv():
    headers = ["type", "color", "size"]
    dict_data = [
        {"type": "potato", "color": "blue", "size": 1},
        {"type": "banana", "color": "red", "size": 2},
        {"type": "potato", "size": 3, "color": "yellow"},
    ]
    return StreamingResponse(
        stream_data(dict_data, headers),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=data.csv"},
    )
```

## License

This project is licensed under the terms of the MIT license.
