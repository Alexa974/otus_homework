"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import asyncio

from aiohttp import ClientSession

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(session: ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()


async def fetch_users_data():
    async with ClientSession() as session:
        user_data = await fetch_json(session, USERS_DATA_URL)
        # print(user_data)
    return user_data


async def fetch_posts_data():
    async with ClientSession() as session:
        post_data = await fetch_json(session, POSTS_DATA_URL)
        # print(post_data)
    return post_data


async def main():
    await fetch_users_data()
    await fetch_posts_data()


if __name__ == "__main__":
    asyncio.run(main())

