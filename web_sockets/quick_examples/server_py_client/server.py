import asyncio

from websockets.asyncio.server import serve


async def hello(websocket):
    """Сопрограмма, которая управляет соединением.
    Когда клиент подключается, websockets вызывает hello с соединением в
    аргументе.
    Когда hello завершается, websockets закрывает соединение.
    """
    name = await websocket.recv()
    print(f"<<< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f">>> {greeting}")


async def main():
    async with serve(hello, "localhost", 8765) as server:
        # Вызов serve() в качестве асинхронного менеджера контекста в блоке
        # async with гарантирует корректное завершение работы сервера при
        # завершении программы.
        await server.serve_forever()


if __name__ == "__main__":
    """Создает цикл событий asyncio, запускает сопрограмму main() и завершает 
    цикл.
    """
    asyncio.run(main())
