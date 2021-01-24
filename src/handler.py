from goustoconfig import Config
from goustologger import Logger
from controllers.example_controller import example_response

default_config = Config().doc
log = Logger().logger


def example_handler(request, config=default_config):
    log.info("request headers: %s", request.headers)
    log.info("request body: %s", request.json_body)
    log.info("config: %s", config)
    return example_response()
