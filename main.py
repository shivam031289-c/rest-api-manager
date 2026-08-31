import asyncio
from api_client import AsyncAPIClient, UserAPIClient
from file_manager import FileManager


def main():
  # Objects initialization
  file_mgr = FileManager()
  user_client = UserAPIClient()
  async_client = AsyncAPIClient()

  # Loops: Infinite while loop for CLI menu
  while True:
    print("\n==============================")
    print("    SMART API DASHBOARD       ")
    print("==============================")
    print("1. Fetch Users (Sync) & Save JSON")
    print("2. Fetch Multiple Posts Concurrently (Async)")
    print("3. Exit")

    choice = input("\nApna option chuniye (1-3): ")

    # Exception Handling
    try:
      if choice == "1":
        print("\n[Info] Fetching users synchronously...")
        data = user_client.fetch_users()
        if data:
          file_mgr.save_json("users.json", data)
          # Optional: Agar CSV mein bhi save karna ho
          file_mgr.save_csv("users.csv", data)

      elif choice == "2":
        urls = [
            "https://jsonplaceholder.typicode.com/posts/1",
            "https://jsonplaceholder.typicode.com/posts/2",
            "https://jsonplaceholder.typicode.com/posts/3",
        ]
        print("\n[Info] Fetching multiple endpoints asynchronously...")
        results = asyncio.run(async_client.fetch_multiple(urls))
        file_mgr.save_json("async_posts.json", results)

      elif choice == "3":
        print("\nProgram band ho raha hai. Goodbye!")
        break
      else:
        print("\n[Warning] Galat choice! Kripya 1, 2 ya 3 hi dalein.")

    except Exception as e:
      print(f"\n[Critical Error] Ek unexpected error aa gayi: {e}")


if __name__ == "__main__":
  main()