import pprint
import traceback
from pydoc import locate
import re

from starlette.responses import JSONResponse
from starlette.types import Scope, Receive, Send


class ExceptionHandlerMiddleware:
    def __init__(
            self,
            app,
    ):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        try:
            await self.app(scope, receive, send)
        except Exception as err:
            response = {
                "result": "error"
            }
            status_code = 500
            message = f"{err}"
            if re.match(r"\d\d\d,", message):
                x_sc, message = message.split(",", maxsplit=1)
                status_code = int(x_sc)
                try:
                    if tags := re.findall(r"@([\w:]+)=([\"'].*?[\"'])|@([\w:]+)=([\w\+\/=\.]+)$|@([\w:]+)=(.*?) ", message):
                        tags = [[z for z in x if z != ''] for x in tags]
                        for tag in tags:
                            key, value = tag
                            message = message.replace(f"@{key}={value}", "")
                            value = value.replace("\"", "").replace("'", "")
                            key_type = key.split(":")
                            if len(key_type) == 2 and type(locate(key_type[1])) is type:
                                value = locate(key_type[1])(value)
                            response[key_type[0]] = value
                except Exception as e:
                    print(f'puppy bork this: {e}')
                    ...

            response["message"] = f"{message.strip()}"
            traceback.print_exc()
            if status_code == 500:
                print("Uploading error log")
                message = f"Scope: {pprint.pformat(scope)}\n\n"
                message += traceback.format_exc()
                print(message)

            # Change here to LOGGER
            return await JSONResponse(status_code=status_code,
                                      content=response)(scope, receive, send)
