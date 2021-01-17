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
