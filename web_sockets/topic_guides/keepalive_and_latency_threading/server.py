import logging

from websockets.sync.server import serve

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)


def hello(websocket):
    """Обработчик, который управляет соединением.
    Когда клиент подключается, websockets вызывает hello с соединением в
    аргументе.
    Когда hello завершается, websockets закрывает соединение.
    """
    name = websocket.recv()
    print(f"<<< {name}")

    greeting = f"Hello {name}!"

    websocket.send(greeting)
    print(f">>> {greeting}")


def main():
    with serve(
        hello,
        "localhost",
        8765,
        ping_interval=10,
        ping_timeout=10,
    ) as server:
        server.serve_forever()


if __name__ == "__main__":
    main()
