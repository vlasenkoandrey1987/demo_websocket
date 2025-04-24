import asyncio
import logging

from websockets.asyncio.server import serve

from web_sockets.quick_examples.server_py_client.server import hello

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)


async def main():
    async with serve(
        hello,
        "localhost",
        8765,
        ping_interval=10,
        ping_timeout=10,
    ) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
