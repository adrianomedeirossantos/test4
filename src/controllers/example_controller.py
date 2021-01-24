from goustologger import Logger
from responses.ok_response import OkResponse

log = Logger().logger


def example_response():
    return OkResponse(body={"message": "ok"})
