import asyncio
import os
import aiohttp
import requests
from dotenv import load_dotenv

# Environment variables load kar rahe hain (.env se)
load_dotenv()


class BaseAPIClient:
  """OOP: Base class with Encapsulated private attribute (__base_url)"""

  def __init__(self):
    self.__base_url = os.getenv("API_BASE_URL")

  def get_base_url(self):
    return self.__base_url


class UserAPIClient(BaseAPIClient):
  """OOP: Inheritance (Child class inheriting from BaseAPIClient)"""

  def fetch_users(self):
    url = f"{self.get_base_url()}/users"
    try:
      # Synchronous HTTP GET request using requests library
      response = requests.get(url, timeout=10)
      response.raise_for_status()  # Exception handling for HTTP errors
      return response.json()
    except requests.exceptions.RequestException as e:
      print(f"[Error] Network error occurred: {e}")
      return None


class AsyncAPIClient:
  """Concurrency: Async/Await using aiohttp and asyncio"""

  async def fetch_endpoint(self, session, url):
    async with session.get(url) as response:
      return await response.json()

  async def fetch_multiple(self, urls):
    async with aiohttp.ClientSession() as session:
      tasks = [self.fetch_endpoint(session, url) for url in urls]
      results = await asyncio.gather(*tasks)
      return results