import socket

from httpResponse import HTTPResponse
from responseType import HTMLResponse, JsonResponse


class App:
    def __init__(self):
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.routes = {}

    def setup(
        self,
        host: str = "127.0.0.1",
        port: int = 80,
        queue: int = 8,
        chunk_size: int = 1024,
    ):
        self.serversocket.bind((host, port))
        self.serversocket.listen(queue)
        self.chunk_size = chunk_size

        print(f"Listening on {host}:{port}")

    def run(self):
        while True:
            (clientsocket, address) = self.serversocket.accept()

            data = clientsocket.recv(self.chunk_size)

            lines = data.decode("utf-8").split("\r\n")
            method, path, protocol = lines[0].split(" ")

            status = 200

            controller = self.routes.get(path, HTMLResponse)
            response_type = controller.__annotations__.get(
                "return",
            )

            if response_type not in [HTMLResponse, JsonResponse]:
                raise TypeError("Invalid return type")

            if controller is None:
                try:
                    clientsocket.send(HTTPResponse.http_404())
                except Exception as e:
                    print(e + "\n")
                    clientsocket.send(HTTPResponse.http_500())
                    status = 500
                clientsocket.close()
                status = 404
            else:
                clientsocket.send(
                    HTTPResponse.http_200(
                        headers=response_type.headers(),
                        data=response_type(controller()),
                    )
                )
                status = 200

            print(f"{method} {path} {protocol} {status}")

            clientsocket.close()

    def get(self, path: str) -> callable:
        def inner(func: callable) -> callable:
            self.routes[path] = func

        return inner
