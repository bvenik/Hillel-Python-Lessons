import asyncio
import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in ["https://google.com","https://www.python.org/", "https://gemini.google.com"] * 10:
            task = asyncio.create_task(fetch(session, url))
            tasks.append(task)

        results = await asyncio.gather(*tasks)
        for res in results:
            print(res[:50])

asyncio.run(main())