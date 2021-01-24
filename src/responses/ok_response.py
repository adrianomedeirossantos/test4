from chalice.app import Response


class OkResponse(Response):
    status_code = 200

    headers = {"Content-Type": "application/json"}

    def __init__(self, body=None, status_code=status_code):
        formatted_body = {"status": "ok", "data": body}

        super().__init__(
            body=formatted_body, status_code=status_code, headers=self.headers
        )
