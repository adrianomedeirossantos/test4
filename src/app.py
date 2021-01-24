import json
from typing import Any, Dict

from chalice import Chalice
from goustoconfig import Config
from goustologger import Logger
from mexanger import Messenger
from handler import example_handler

app = Chalice(app_name="my-beautiful-function-name")

log = Logger().logger
config = Config().doc


def unwrap(message: Any) -> Any:
    raw_sns_message = message["Records"][0]["body"]
    parsed_sns_message = json.loads(raw_sns_message)
    raw_gousto_message = parsed_sns_message["Message"]
    parsed_gousto_message = json.loads(raw_gousto_message)
    return parsed_gousto_message["payload"]


@app.route("/")  # type: ignore
def index() -> Any:
    return example_handler(app.current_request)


@app.lambda_function()  # type: ignore
def handle_lambda_event(
    event: Dict[str, Any], context: Any
) -> Any:  # pylint: disable=unused-argument
    try:
        log.info("Received event: {event}", {"event": event})

        if context and context.aws_request_id:
            log.info("Request ID: {id}", {"id": context.aws_request_id})

        Messenger.set_defaults(config["messages"]["defaults"])
        Messenger.set_arn(config["messages"]["arn"])
    except Exception as e:
        log.error("Unhandled exception")
        raise e
