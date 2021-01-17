from typing import List, TypeVar

from stream_csv.stream import stream_data

sqlalchemy_error_message = (
    "This module requires sqlalchemy, please install it with\n\n"
    "pip install sqlalchemy"
)

starlette_error_message = (
    "This module requires starlette, please install it with:\n\n"
    "pip install starlette"
)

try:
    from starlette.background import BackgroundTask
    from starlette.responses import StreamingResponse
except ImportError:
    raise RuntimeError(starlette_error_message)


try:
    from sqlalchemy import inspect
except ImportError:
    raise RuntimeError(sqlalchemy_error_message)

Model = TypeVar("Model", bound="Base")


class StreamingCSVResponse(StreamingResponse):
    def __init__(
        self,
        content: List[Model],
        status_code: int = 200,
        headers: dict = None,
        media_type: str = None,
        background: BackgroundTask = None,
    ) -> None:
        columns = [c.key for c in inspect(type(content[0])).mapper.column_attrs]
        generator = stream_data(
            [{column: getattr(row, column) for column in columns} for row in content]
        )
        super().__init__(
            content=generator,
            status_code=status_code,
            headers=headers,
            media_type=media_type,
            background=background,
        )
