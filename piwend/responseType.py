import orjson


class Response:
    def __init__(self, values):
        self.value = values

    @staticmethod
    def headers() -> dict:
        return {}


class JsonResponse:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def headers() -> dict:
        return {"Content-Type": "application/json"}

    def __str__(self):
        data: str | dict | list | tuple = ""

        if isinstance(self.value, dict):
            data = self.value
        elif isinstance(self.value, list) or isinstance(self.value, tuple):
            data = {idx: v for idx, v in enumerate(self.value)}
        elif isinstance(self.value, str):
            data = {"data": self.value}
        else:
            data = {"data": str(self.value)}

        return orjson.dumps(data).decode("utf-8")


class HTMLResponse(Response):
    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return self.value
