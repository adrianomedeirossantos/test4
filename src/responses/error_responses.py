from chalice.app import Response


class ErrorResponse(Response):

    headers = {"Content-Type": "application/json"}

    def __init__(self, errors, exception=Exception):
        body = {
            "status": "error",
            "errors": self.format_errors(errors)
            if errors
            else [self.format_exception(exception)],
        }

        super().__init__(body=body, status_code=self.status_code, headers=self.headers)

    @staticmethod
    def format_exception(exception):
        try:
            message = exception.msg
        except AttributeError:
            message = "no message"

        try:
            error_name = exception.__name__
        except AttributeError:  # exception is instantiated
            error_name = exception.__class__.__name__

        return {"error": error_name, "message": message}

    @staticmethod
    def format_errors(errors):
        ret = []
        for field, error in errors.items():
            ret.append({"error": field + "-error", "message": error})

        return ret


class InternalServerErrorResponse(ErrorResponse):
    status_code = 500


class GatewayTimeoutResponse(ErrorResponse):
    status_code = 504


class BadResponse(ErrorResponse):
    status_code = 400


class UnprocessableEntityResponse(ErrorResponse):
    status_code = 422


class NotFoundResponse(ErrorResponse):
    status_code = 404


class UnauthorizedResponse(ErrorResponse):
    status_code = 401


class ConflictResponse(ErrorResponse):
    status_code = 409
