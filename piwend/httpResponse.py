class HTTPResponse:
    @staticmethod
    def http_200(data: str = "200 OK", headers=None) -> str:
        if headers is not None:
            headers = "\r\n" + "\r\n".join([f"{k}: {v}" for k, v in headers.items()])
        return f"HTTP/1.1 200 OK{headers}\r\n\r\n{data}".encode("utf-8")

    @staticmethod
    def http_404(data: str = "404 Not Found") -> str:
        return f"HTTP/1.1 404 Not Found\r\n\r\n{data}".encode("utf-8")

    @staticmethod
    def http_500(data: str) -> str:
        return f"HTTP/1.1 500 Internal Server Error\r\n\r\n{data}".encode("utf-8")
