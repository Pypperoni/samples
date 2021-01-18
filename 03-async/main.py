import asyncio

class HelloAsync():
    async def __aenter__(self):
        return 'Hello!'

    async def __aexit__(self, exc_type, exc, tb):
        pass

async def triggerHello():
    async with HelloAsync() as hello:
        yield hello

async def main():
    async for hello in triggerHello():
        print(hello)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
